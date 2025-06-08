from flask import render_template, request, redirect, url_for, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.signe_vital.gestion_signe_vital_wtf_forms import (
    FormWTFAjouterSigneVital, FormWTFUpdateSigneVital, FormWTFDeleteSigneVital
)

@app.route("/signes_vitaux_afficher/<string:order_by>/<int:id_signe_vital_sel>", methods=['GET', 'POST'])
def signes_vitaux_afficher(order_by, id_signe_vital_sel):
    data_signes = []
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT
                    sv.id_signe_vital,
                    sv.date_signe,
                    sv.type_signe,
                    sv.valeurs_signe,
                    pat.nom_patient,
                    pat.prenom_patient
                FROM t_signe_vital sv
                JOIN t_dossier_signe_vital dsv ON sv.id_signe_vital = dsv.fk_signe_vital
                JOIN t_dossier d ON dsv.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient pat ON dp.fk_patient = pat.id_patient
                ORDER BY sv.id_signe_vital ASC
            """
            mc.execute(strsql)
            data_signes = mc.fetchall()
    except Exception as e:
        flash("Erreur lors de l'affichage des signes vitaux.", "danger")
        print(e)
    return render_template("signe_vital/signe_vital_afficher.html", data=data_signes)

@app.route("/signe_vital_ajouter", methods=['GET', 'POST'])
def signe_vital_ajouter_wtf():
    # Récupérer les patients pour la liste déroulante
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient ORDER BY nom_patient ASC, prenom_patient ASC")
        patients = mc.fetchall()
        patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]

    form = FormWTFAjouterSigneVital()
    form.patient_select.choices = patient_choices

    if request.method == "POST" and form.validate_on_submit():
        date_signe = form.date_signe.data
        type_signe = form.type_signe.data
        valeurs_signe = form.valeurs_signe.data
        fk_patient = form.patient_select.data

        try:
            with DBconnection() as mconn_bd:
                # Trouver le dossier du patient
                strsql_dossier = "SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s LIMIT 1"
                mconn_bd.execute(strsql_dossier, (fk_patient,))
                dossier_row = mconn_bd.fetchone()
                if not dossier_row:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return render_template("signe_vital/signe_vital_ajouter_wtf.html", form=form)
                fk_dossier = dossier_row["fk_dossier"]

                # 1. Insérer le signe vital
                strsql_insert = """
                    INSERT INTO t_signe_vital (date_signe, type_signe, valeurs_signe)
                    VALUES (%s, %s, %s)
                """
                mconn_bd.execute(strsql_insert, (date_signe, type_signe, valeurs_signe))
                id_signe_vital = mconn_bd.lastrowid

                # 2. Lier au dossier
                strsql_liaison = """
                    INSERT INTO t_dossier_signe_vital (fk_dossier, fk_signe_vital)
                    VALUES (%s, %s)
                """
                mconn_bd.execute(strsql_liaison, (fk_dossier, id_signe_vital))

            flash("Signe vital ajouté avec succès !", "success")
            return redirect(url_for('signes_vitaux_afficher', order_by='ASC', id_signe_vital_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout du signe vital.", "danger")
            print(e)
    return render_template("signe_vital/signe_vital_ajouter_wtf.html", form=form)

@app.route("/signe_vital_update/<int:id_signe_vital>", methods=['GET', 'POST'])
def signe_vital_update_wtf(id_signe_vital):
    form_update = FormWTFUpdateSigneVital()
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient ORDER BY nom_patient ASC, prenom_patient ASC")
        patients = mc.fetchall()
        patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]
    form_update.patient_select.choices = patient_choices

    if request.method == "POST" and form_update.validate_on_submit():
        date_signe = form_update.date_signe.data
        type_signe = form_update.type_signe.data
        valeurs_signe = form_update.valeurs_signe.data
        fk_patient = form_update.patient_select.data

        try:
            with DBconnection() as mconn_bd:
                # Trouver le dossier du patient
                strsql_dossier = "SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s LIMIT 1"
                mconn_bd.execute(strsql_dossier, (fk_patient,))
                dossier_row = mconn_bd.fetchone()
                if not dossier_row:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return render_template("signe_vital/signe_vital_update_wtf.html", form_update=form_update)
                fk_dossier = dossier_row["fk_dossier"]

                # 1. Mettre à jour le signe vital
                strsql_update = """
                    UPDATE t_signe_vital
                    SET date_signe=%s, type_signe=%s, valeurs_signe=%s
                    WHERE id_signe_vital=%s
                """
                mconn_bd.execute(strsql_update, (date_signe, type_signe, valeurs_signe, id_signe_vital))

                # 2. Mettre à jour la liaison dossier
                strsql_update_liaison = """
                    UPDATE t_dossier_signe_vital
                    SET fk_dossier=%s
                    WHERE fk_signe_vital=%s
                """
                mconn_bd.execute(strsql_update_liaison, (fk_dossier, id_signe_vital))

            flash("Signe vital modifié avec succès !", "success")
            return redirect(url_for('signes_vitaux_afficher', order_by='ASC', id_signe_vital_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification du signe vital.", "danger")
            print(e)
    elif request.method == "GET":
        with DBconnection() as mc:
            strsql = """
                SELECT sv.date_signe, sv.type_signe, sv.valeurs_signe, dp.fk_patient
                FROM t_signe_vital sv
                JOIN t_dossier_signe_vital dsv ON sv.id_signe_vital = dsv.fk_signe_vital
                JOIN t_dossier d ON dsv.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                WHERE sv.id_signe_vital = %s
            """
            mc.execute(strsql, (id_signe_vital,))
            data = mc.fetchone()
            if data:
                form_update.date_signe.data = data["date_signe"]
                form_update.type_signe.data = data["type_signe"]
                form_update.valeurs_signe.data = data["valeurs_signe"]
                form_update.patient_select.data = str(data["fk_patient"])

    return render_template("signe_vital/signe_vital_update_wtf.html", form_update=form_update)

@app.route("/signe_vital_delete/<int:id_signe_vital>", methods=['GET', 'POST'])
def signe_vital_delete_wtf(id_signe_vital):
    form_delete = FormWTFDeleteSigneVital()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # Supprimer la liaison
                    mconn_bd.execute("DELETE FROM t_dossier_signe_vital WHERE fk_signe_vital = %(id_signe_vital)s", {"id_signe_vital": id_signe_vital})
                    # Supprimer le signe vital
                    mconn_bd.execute("DELETE FROM t_signe_vital WHERE id_signe_vital = %(id_signe_vital)s", {"id_signe_vital": id_signe_vital})
                flash("Signe vital supprimé avec succès.", "success")
                return redirect(url_for('signes_vitaux_afficher', order_by="ASC", id_signe_vital_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('signes_vitaux_afficher', order_by="ASC", id_signe_vital_sel=0))
    else:
        with DBconnection() as mc:
            str_sql = """
                SELECT sv.type_signe, sv.valeurs_signe, sv.date_signe, pat.nom_patient, pat.prenom_patient
                FROM t_signe_vital sv
                JOIN t_dossier_signe_vital dsv ON sv.id_signe_vital = dsv.fk_signe_vital
                JOIN t_dossier d ON dsv.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient pat ON dp.fk_patient = pat.id_patient
                WHERE sv.id_signe_vital = %(id_signe_vital)s
            """
            mc.execute(str_sql, {"id_signe_vital": id_signe_vital})
            data = mc.fetchone()
            if data:
                form_delete.type_signe.data = data["type_signe"]
                form_delete.valeurs_signe.data = data["valeurs_signe"]
                form_delete.date_signe.data = data["date_signe"]
                form_delete.patient.data = f"{data['nom_patient']} {data['prenom_patient']}"
        return render_template("signe_vital/signe_vital_delete_wtf.html", form_delete=form_delete)

@app.route("/signe_vital_info/<int:id_signe_vital>", methods=['GET'])
def signe_vital_info(id_signe_vital):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    sv.id_signe_vital,
                    sv.date_signe,
                    sv.type_signe,
                    sv.valeurs_signe,
                    pat.nom_patient,
                    pat.prenom_patient
                FROM t_signe_vital sv
                JOIN t_dossier_signe_vital dsv ON sv.id_signe_vital = dsv.fk_signe_vital
                JOIN t_dossier d ON dsv.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient pat ON dp.fk_patient = pat.id_patient
                WHERE sv.id_signe_vital = %(id_signe_vital)s
            """
            mc_info.execute(strsql_info, {"id_signe_vital": id_signe_vital})
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos du signe vital.", "danger")
        print(e)
        return redirect(url_for('signes_vitaux_afficher', order_by="ASC", id_signe_vital_sel=0))
    return render_template("signe_vital/signe_vital_info.html", data=data_info)