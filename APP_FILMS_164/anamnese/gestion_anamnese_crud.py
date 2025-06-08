from pathlib import Path

from flask import redirect, request, session, url_for, flash, render_template

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.anamnese.gestion_anamnese_wtf_forms import FormWTFAjouterAnamnese, FormWTFDeleteAnamnese, FormWTFUpdateAnamnese

@app.route("/anamneses_afficher/<string:order_by>/<int:id_anamnese_sel>", methods=['GET', 'POST'])
def anamneses_afficher(order_by, id_anamnese_sel):
    data_anamnese = []
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT
                    a.id_anamnese,
                    p.nom_patient,
                    p.prenom_patient,
                    a.allergies_anamn
                FROM t_anamnese a
                JOIN t_dossier_anamnese da ON a.id_anamnese = da.fk_anamnese
                JOIN t_dossier d ON da.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                ORDER BY a.id_anamnese ASC
            """
            mc.execute(strsql)
            data_anamnese = mc.fetchall()
    except Exception as e:
        flash("Erreur lors de l'affichage des anamnèses.", "danger")
        print(e)
    return render_template("anamnese/anamnese_afficher.html", data=data_anamnese)

@app.route("/anamnese_ajouter", methods=['GET', 'POST'])
def anamnese_ajouter_wtf():
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient ORDER BY nom_patient, prenom_patient")
        patients = mc.fetchall()
        patient_choices = [
            (str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}")
            for row in patients
        ]
    form = FormWTFAjouterAnamnese()
    form.patient_select.choices = patient_choices

    if request.method == "POST" and form.validate_on_submit():
        id_patient = form.patient_select.data
        histoire = form.histoire_de_vie_anamn.data
        antecedents = form.antecedent_medicaux_anamn.data
        probleme = form.probleme_anamn.data
        allergies = form.allergies_anamn.data

        try:
            with DBconnection() as mconn_bd:
                # 1. Insérer l'anamnèse
                strsql_insert = """
                    INSERT INTO t_anamnese (histoire_de_vie_anamn, antecedent_medicaux_anamn, probleme_anamn, allergies_anamn)
                    VALUES (%s, %s, %s, %s)
                """
                mconn_bd.execute(strsql_insert, (histoire, antecedents, probleme, allergies))
                id_anamnese = mconn_bd.lastrowid

                # 2. Trouver le dossier du patient
                strsql_dossier = "SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s"
                mconn_bd.execute(strsql_dossier, (id_patient,))
                dossier = mconn_bd.fetchone()
                if dossier:
                    fk_dossier = dossier["fk_dossier"]
                    # 3. Lier l'anamnèse au dossier
                    strsql_liaison = """
                        INSERT INTO t_dossier_anamnese (fk_dossier, fk_anamnese)
                        VALUES (%s, %s)
                    """
                    mconn_bd.execute(strsql_liaison, (fk_dossier, id_anamnese))
                else:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return redirect(url_for('anamneses_afficher', order_by='ASC', id_anamnese_sel=0))

            flash("Anamnèse ajoutée avec succès !", "success")
            return redirect(url_for('anamneses_afficher', order_by='ASC', id_anamnese_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout de l'anamnèse.", "danger")
            print(e)
    return render_template("anamnese/anamnese_ajouter_wtf.html", form=form)

@app.route("/anamnese_update/<int:id_anamnese>", methods=['GET', 'POST'])
def anamnese_update_wtf(id_anamnese):
    form_update = FormWTFUpdateAnamnese()
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient")
        patients = mc.fetchall()
        patient_choices = [
            (str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}")
            for row in patients
        ]
    form_update.patient_select.choices = patient_choices

    if request.method == "POST" and form_update.validate_on_submit():
        id_patient = form_update.patient_select.data
        histoire = form_update.histoire_de_vie_anamn.data
        antecedents = form_update.antecedent_medicaux_anamn.data
        probleme = form_update.probleme_anamn.data
        allergies = form_update.allergies_anamn.data

        try:
            with DBconnection() as mconn_bd:
                # 1. Mettre à jour l'anamnèse
                strsql_update = """
                    UPDATE t_anamnese
                    SET histoire_de_vie_anamn=%s, antecedent_medicaux_anamn=%s, probleme_anamn=%s, allergies_anamn=%s
                    WHERE id_anamnese=%s
                """
                mconn_bd.execute(strsql_update, (histoire, antecedents, probleme, allergies, id_anamnese))

                # 2. Trouver le dossier du patient
                strsql_dossier = "SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s"
                mconn_bd.execute(strsql_dossier, (id_patient,))
                dossier = mconn_bd.fetchone()
                if dossier:
                    fk_dossier = dossier["fk_dossier"]
                    # 3. Mettre à jour la liaison
                    strsql_update_liaison = """
                        UPDATE t_dossier_anamnese
                        SET fk_dossier=%s
                        WHERE fk_anamnese=%s
                    """
                    mconn_bd.execute(strsql_update_liaison, (fk_dossier, id_anamnese))
                else:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return redirect(url_for('anamneses_afficher', order_by='ASC', id_anamnese_sel=0))

            flash("Anamnèse modifiée avec succès !", "success")
            return redirect(url_for('anamneses_afficher', order_by='ASC', id_anamnese_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification de l'anamnèse.", "danger")
            print(e)
    elif request.method == "GET":
        with DBconnection() as mc:
            strsql = """
                SELECT a.histoire_de_vie_anamn, a.antecedent_medicaux_anamn, a.probleme_anamn, a.allergies_anamn, dp.fk_patient
                FROM t_anamnese a
                JOIN t_dossier_anamnese da ON a.id_anamnese = da.fk_anamnese
                JOIN t_dossier d ON da.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                WHERE a.id_anamnese = %s
            """
            mc.execute(strsql, (id_anamnese,))
            data = mc.fetchone()
            if data:
                form_update.histoire_de_vie_anamn.data = data["histoire_de_vie_anamn"]
                form_update.antecedent_medicaux_anamn.data = data["antecedent_medicaux_anamn"]
                form_update.probleme_anamn.data = data["probleme_anamn"]
                form_update.allergies_anamn.data = data["allergies_anamn"]
                form_update.patient_select.data = str(data["fk_patient"])

    return render_template("anamnese/anamnese_update_wtf.html", form_update=form_update)

@app.route("/anamnese_delete/<int:id_anamnese>", methods=['GET', 'POST'])
def anamnese_delete_wtf(id_anamnese):
    form_delete = FormWTFDeleteAnamnese()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # Supprimer la liaison
                    str_sql_delete_liaison = "DELETE FROM t_dossier_anamnese WHERE fk_anamnese = %(id_anamnese)s"
                    mconn_bd.execute(str_sql_delete_liaison, {"id_anamnese": id_anamnese})
                    # Supprimer l'anamnèse
                    str_sql_delete_anamnese = "DELETE FROM t_anamnese WHERE id_anamnese = %(id_anamnese)s"
                    mconn_bd.execute(str_sql_delete_anamnese, {"id_anamnese": id_anamnese})
                flash("Anamnèse supprimée avec succès.", "success")
                return redirect(url_for('anamneses_afficher', order_by="ASC", id_anamnese_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('anamneses_afficher', order_by="ASC", id_anamnese_sel=0))
    else:
        # Pré-remplir les champs pour affichage
        with DBconnection() as mc:
            str_sql = """
                SELECT p.nom_patient, p.prenom_patient, a.histoire_de_vie_anamn
                FROM t_anamnese a
                JOIN t_dossier_anamnese da ON a.id_anamnese = da.fk_anamnese
                JOIN t_dossier d ON da.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                WHERE a.id_anamnese = %(id_anamnese)s
            """
            mc.execute(str_sql, {"id_anamnese": id_anamnese})
            data = mc.fetchone()
            if data:
                form_delete.patient.data = f"{data['nom_patient']} {data['prenom_patient']}"
                form_delete.histoire_de_vie_anamn.data = data["histoire_de_vie_anamn"]
        return render_template("anamnese/anamnese_delete_wtf.html", form_delete=form_delete)

@app.route("/anamnese_info/<int:id_anamnese>", methods=['GET'])
def anamnese_info(id_anamnese):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    a.id_anamnese,
                    p.nom_patient,
                    p.prenom_patient,
                    a.histoire_de_vie_anamn,
                    a.antecedent_medicaux_anamn,
                    a.probleme_anamn,
                    a.allergies_anamn
                FROM t_anamnese a
                JOIN t_dossier_anamnese da ON a.id_anamnese = da.fk_anamnese
                JOIN t_dossier d ON da.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                WHERE a.id_anamnese = %(id_anamnese)s
            """
            mc_info.execute(strsql_info, {"id_anamnese": id_anamnese})
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos de l'anamnèse.", "danger")
        print(e)
        return redirect(url_for('anamneses_afficher', order_by="ASC", id_anamnese_sel=0))
    return render_template("anamnese/anamnese_info.html", data=data_info)