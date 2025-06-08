from flask import render_template, request, redirect, url_for, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.rapport.gestion_rapport_wtf_forms import (
    FormWTFAjouterRapport, FormWTFUpdateRapport, FormWTFDeleteRapport
)

@app.route("/rapports_afficher/<string:order_by>/<int:id_rapport_sel>", methods=['GET', 'POST'])
def rapports_afficher(order_by, id_rapport_sel):
    data_rapports = []
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT
                    r.id_rapport,
                    p.nom_patient,
                    p.prenom_patient,
                    r.type_rapport
                FROM t_rapport r
                JOIN t_dossier_rapport dr ON r.id_rapport = dr.fk_rapport
                JOIN t_dossier d ON dr.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                ORDER BY r.id_rapport ASC
            """
            mc.execute(strsql)
            data_rapports = mc.fetchall()
    except Exception as e:
        flash("Erreur lors de l'affichage des rapports.", "danger")
        print(e)
    return render_template("rapport/rapport_afficher.html", data=data_rapports)

@app.route("/rapport_ajouter", methods=['GET', 'POST'])
def rapport_ajouter_wtf():
    with DBconnection() as mc:
        mc.execute("""
            SELECT p.id_patient, p.nom_patient, p.prenom_patient
            FROM t_patient p
            ORDER BY p.nom_patient, p.prenom_patient
        """)
        patients = mc.fetchall()
        patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]

    form = FormWTFAjouterRapport()
    form.patient_select.choices = patient_choices

    if request.method == "POST" and form.validate_on_submit():
        date_rapport = form.date_rapport.data
        type_rapport = form.type_rapport.data
        texte_rapport = form.texte_rapport.data
        fk_patient = form.patient_select.data

        try:
            with DBconnection() as mconn_bd:
                # Récupérer le dossier lié au patient sélectionné
                strsql_dossier = """
                    SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s LIMIT 1
                """
                mconn_bd.execute(strsql_dossier, (fk_patient,))
                dossier_row = mconn_bd.fetchone()
                if not dossier_row:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return render_template("rapport/rapport_ajouter_wtf.html", form=form)
                fk_dossier = dossier_row["fk_dossier"]

                # 1. Insérer le rapport
                strsql_insert = """
                    INSERT INTO t_rapport (date_rapport, type_rapport, texte_rapport)
                    VALUES (%s, %s, %s)
                """
                mconn_bd.execute(strsql_insert, (date_rapport, type_rapport, texte_rapport))
                id_rapport = mconn_bd.lastrowid

                # 2. Lier au dossier
                strsql_liaison = """
                    INSERT INTO t_dossier_rapport (fk_dossier, fk_rapport)
                    VALUES (%s, %s)
                """
                mconn_bd.execute(strsql_liaison, (fk_dossier, id_rapport))

            flash("Rapport ajouté avec succès !", "success")
            return redirect(url_for('rapports_afficher', order_by='ASC', id_rapport_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout du rapport.", "danger")
            print(e)
    return render_template("rapport/rapport_ajouter_wtf.html", form=form)

@app.route("/rapport_update/<int:id_rapport>", methods=['GET', 'POST'])
def rapport_update_wtf(id_rapport):
    form_update = FormWTFUpdateRapport()
    with DBconnection() as mc:
        mc.execute("""
            SELECT p.id_patient, p.nom_patient, p.prenom_patient
            FROM t_patient p
            ORDER BY p.nom_patient, p.prenom_patient
        """)
        patients = mc.fetchall()
        patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]
    form_update.patient_select.choices = patient_choices

    if request.method == "POST" and form_update.validate_on_submit():
        date_rapport = form_update.date_rapport.data
        type_rapport = form_update.type_rapport.data
        texte_rapport = form_update.texte_rapport.data
        fk_patient = form_update.patient_select.data

        try:
            with DBconnection() as mconn_bd:
                # Récupérer le dossier lié au patient sélectionné
                strsql_dossier = """
                    SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s LIMIT 1
                """
                mconn_bd.execute(strsql_dossier, (fk_patient,))
                dossier_row = mconn_bd.fetchone()
                if not dossier_row:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return render_template("rapport/rapport_update_wtf.html", form_update=form_update)
                fk_dossier = dossier_row["fk_dossier"]

                # 1. Mettre à jour le rapport
                strsql_update = """
                    UPDATE t_rapport
                    SET date_rapport=%s, type_rapport=%s, texte_rapport=%s
                    WHERE id_rapport=%s
                """
                mconn_bd.execute(strsql_update, (date_rapport, type_rapport, texte_rapport, id_rapport))

                # 2. Mettre à jour la liaison dossier
                strsql_update_liaison = """
                    UPDATE t_dossier_rapport
                    SET fk_dossier=%s
                    WHERE fk_rapport=%s
                """
                mconn_bd.execute(strsql_update_liaison, (fk_dossier, id_rapport))

            flash("Rapport modifié avec succès !", "success")
            return redirect(url_for('rapports_afficher', order_by='ASC', id_rapport_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification du rapport.", "danger")
            print(e)
    elif request.method == "GET":
        with DBconnection() as mc:
            strsql = """
                SELECT r.date_rapport, r.type_rapport, r.texte_rapport, dp.fk_patient
                FROM t_rapport r
                JOIN t_dossier_rapport dr ON r.id_rapport = dr.fk_rapport
                JOIN t_dossier_patient dp ON dr.fk_dossier = dp.fk_dossier
                WHERE r.id_rapport = %s
            """
            mc.execute(strsql, (id_rapport,))
            data = mc.fetchone()
            if data:
                form_update.date_rapport.data = data["date_rapport"]
                form_update.type_rapport.data = data["type_rapport"]
                form_update.texte_rapport.data = data["texte_rapport"]
                form_update.patient_select.data = str(data["fk_patient"])

    return render_template("rapport/rapport_update_wtf.html", form_update=form_update)

@app.route("/rapport_delete/<int:id_rapport>", methods=['GET', 'POST'])
def rapport_delete_wtf(id_rapport):
    form_delete = FormWTFDeleteRapport()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # Supprimer la liaison
                    mconn_bd.execute("DELETE FROM t_dossier_rapport WHERE fk_rapport = %(id_rapport)s", {"id_rapport": id_rapport})
                    # Supprimer le rapport
                    mconn_bd.execute("DELETE FROM t_rapport WHERE id_rapport = %(id_rapport)s", {"id_rapport": id_rapport})
                flash("Rapport supprimé avec succès.", "success")
                return redirect(url_for('rapports_afficher', order_by="ASC", id_rapport_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('rapports_afficher', order_by="ASC", id_rapport_sel=0))
    else:
        with DBconnection() as mc:
            str_sql = """
                SELECT p.nom_patient, p.prenom_patient, r.type_rapport, r.texte_rapport, r.date_rapport
                FROM t_rapport r
                JOIN t_dossier_rapport dr ON r.id_rapport = dr.fk_rapport
                JOIN t_dossier d ON dr.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                WHERE r.id_rapport = %(id_rapport)s
            """
            mc.execute(str_sql, {"id_rapport": id_rapport})
            data = mc.fetchone()
            if data:
                form_delete.nom_patient.data = data["nom_patient"]
                form_delete.prenom_patient.data = data["prenom_patient"]
                form_delete.type_rapport.data = data["type_rapport"]
                form_delete.texte_rapport.data = data["texte_rapport"]
                form_delete.date_rapport.data = str(data["date_rapport"])
    return render_template("rapport/rapport_delete_wtf.html", form_delete=form_delete)

@app.route("/rapport_info/<int:id_rapport>", methods=['GET'])
def rapport_info(id_rapport):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    r.id_rapport,
                    r.date_rapport,
                    r.type_rapport,
                    r.texte_rapport,
                    d.id_dossier,
                    p.nom_patient,
                    p.prenom_patient
                FROM t_rapport r
                JOIN t_dossier_rapport dr ON r.id_rapport = dr.fk_rapport
                JOIN t_dossier d ON dr.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                WHERE r.id_rapport = %(id_rapport)s
            """
            mc_info.execute(strsql_info, {"id_rapport": id_rapport})
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos du rapport.", "danger")
        print(e)
        return redirect(url_for('rapports_afficher', order_by="ASC", id_rapport_sel=0))
    return render_template("rapport/rapport_info.html", data=data_info)