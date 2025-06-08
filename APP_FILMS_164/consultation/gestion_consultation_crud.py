
"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.consultation.gestion_consultation_wtf_forms import FormWTFAjouterconsultation
from APP_FILMS_164.consultation.gestion_consultation_wtf_forms import FormWTFDeleteconsultation
from APP_FILMS_164.consultation.gestion_consultation_wtf_forms import FormWTFUpdateconsultation


"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/consultations_afficher/<string:order_by>/<int:id_consultation_sel>", methods=['GET', 'POST'])
def consultations_afficher(order_by, id_consultation_sel):
    if request.method == "GET":
        data_consultations = []
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_consultation_sel == 0:
                    strsql_consultation_afficher = """SELECT
                                                    c.id_consultation,
                                                    p.nom_patient,
                                                    p.prenom_patient,
                                                    c.motif_consult
                                                FROM t_consultation c
                                                JOIN t_consultation_patient cp ON c.id_consultation = cp.fk_consultation
                                                JOIN t_patient p ON cp.fk_patient = p.id_patient
                                                ORDER BY c.id_consultation ASC;
                    """
                    mc_afficher.execute(strsql_consultation_afficher)
                elif order_by == "ASC":
                    valeur_id_consultation_selected_dictionnaire = {"id_consultation": id_consultation_sel}
                    strsql_consultation_afficher = """
                        SELECT
                            c.id_consultation,,
                            p.nom_patient,
                            p.prenom_patient,
                            c.motif_consult
                        FROM t_consultation c
                        JOIN t_consultation_patient cp ON c.id_consultation = cp.fk_consultation
                        JOIN t_patient p ON cp.fk_patient = p.id_patient
                        WHERE c.id_consultation = %(id_consultation)s
                        ORDER BY c.id_consultation ASC;
                    """
                    mc_afficher.execute(strsql_consultation_afficher, valeur_id_consultation_selected_dictionnaire)
                else:
                    strsql_consultation_afficher = """
                        SELECT
                            c.id_consultation,,
                            p.nom_patient,
                            p.prenom_patient,
                            c.motif_consult
                        FROM t_consultation c
                        JOIN t_consultation_patient cp ON c.id_consultation = cp.fk_consultation
                        JOIN t_patient p ON cp.fk_patient = p.id_patient
                        ORDER BY c.id_consultation ASC;
                    """
                    mc_afficher.execute(strsql_consultation_afficher)

                data_consultations = mc_afficher.fetchall()

                print("data_consultations ", data_consultations, " Type : ", type(data_consultations))

                # Différencier les messages si la table est vide.
                if not data_consultations and id_consultation_sel == 0:
                    flash("""La table "t_consultation" est vide. !!""", "warning")
                elif not data_consultations and id_consultation_sel > 0:
                    flash(f"L'consultation demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données consultations affichées !!", "success")

        except Exception as e:
            flash("Erreur lors de l'affichage des consultations.", "danger")
            data = []
    return render_template("consultation/consultation_afficher.html", data=data_consultations)

"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/consultation_ajouter", methods=['GET', 'POST'])
def consultation_ajouter_wtf():
    # Récupérer tous les patients pour la liste déroulante
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient ORDER BY nom_patient, prenom_patient")
        patients = mc.fetchall()
        patient_choices = [
            (str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}")
            for row in patients
        ]

    form = FormWTFAjouterconsultation()
    form.patient_select.choices = patient_choices

    if request.method == "POST" and form.validate_on_submit():
        id_patient = form.patient_select.data
        date_consult = form.date_consult.data
        motif_consult = form.motif_consult.data
        diagnostic_consult = form.diagnostic_consult.data
        notes_consult = form.notes_consult.data

        try:
            with DBconnection() as mconn_bd:
                # 1. Insérer la consultation
                strsql_insert_consultation = """
                    INSERT INTO t_consultation (date_consult, motif_consult, diagnostic_consult, notes_consult)
                    VALUES (%s, %s, %s, %s)
                """
                mconn_bd.execute(strsql_insert_consultation, (date_consult, motif_consult, diagnostic_consult, notes_consult))
                id_consultation = mconn_bd.lastrowid

                # 2. Lier la consultation au patient
                strsql_insert_consultation_patient = """
                    INSERT INTO t_consultation_patient (fk_patient, fk_consultation)
                    VALUES (%s, %s)
                """
                mconn_bd.execute(strsql_insert_consultation_patient, (id_patient, id_consultation))

            flash("Consultation ajoutée avec succès !", "success")
            return redirect(url_for('consultations_afficher', order_by='ASC', id_consultation_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout de la consultation.", "danger")
            print(e)
    return render_template("consultation/consultation_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/consultation_update/<int:id_consultation>", methods=['GET', 'POST'])
def consultation_update_wtf(id_consultation):
    form_update = FormWTFUpdateconsultation()

    # Récupérer tous les patients pour la liste déroulante
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
        date_consult = form_update.date_consult.data
        motif_consult = form_update.motif_consult.data
        diagnostic_consult = form_update.diagnostic_consult.data
        notes_consult = form_update.notes_consult.data

        try:
            with DBconnection() as mconn_bd:
                # 1. Mettre à jour t_consultation
                strsql_update_consultation = """
                    UPDATE t_consultation
                    SET date_consult=%s, motif_consult=%s, diagnostic_consult=%s, notes_consult=%s
                    WHERE id_consultation=%s
                """
                mconn_bd.execute(strsql_update_consultation, (date_consult, motif_consult, diagnostic_consult, notes_consult, id_consultation))

                # 2. Mettre à jour le patient lié via la table de liaison
                strsql_update_patient = """
                    UPDATE t_consultation_patient
                    SET fk_patient = %s
                    WHERE fk_consultation = %s
                """
                mconn_bd.execute(strsql_update_patient, (id_patient, id_consultation))

            flash("Consultation modifiée avec succès !", "success")
            return redirect(url_for('consultations_afficher', order_by='ASC', id_consultation_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification de la consultation.", "danger")
            print(e)
    elif request.method == "GET":
        # Pré-remplir le formulaire avec les données existantes
        with DBconnection() as mc:
            strsql = """
                SELECT c.date_consult, c.motif_consult, c.diagnostic_consult, c.notes_consult, cp.fk_patient
                FROM t_consultation c
                JOIN t_consultation_patient cp ON c.id_consultation = cp.fk_consultation
                WHERE c.id_consultation = %s
            """
            mc.execute(strsql, (id_consultation,))
            data = mc.fetchone()
            if data:
                form_update.date_consult.data = data["date_consult"]
                form_update.motif_consult.data = data["motif_consult"]
                form_update.diagnostic_consult.data = data["diagnostic_consult"]
                form_update.notes_consult.data = data["notes_consult"]
                form_update.patient_select.data = str(data["fk_patient"])

    return render_template("consultation/consultation_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/consultation_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/consultation_delete/<int:id_consultation>", methods=['GET', 'POST'])
def consultation_delete_wtf(id_consultation):
    form_delete = FormWTFDeleteconsultation()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # Supprimer la liaison dans t_consultation_patient
                    str_sql_delete_liaison = "DELETE FROM t_consultation_patient WHERE fk_consultation = %(id_consultation)s"
                    mconn_bd.execute(str_sql_delete_liaison, {"id_consultation": id_consultation})
                    # Supprimer l'consultation
                    str_sql_delete_consultation = "DELETE FROM t_consultation WHERE id_consultation = %(id_consultation)s"
                    mconn_bd.execute(str_sql_delete_consultation, {"id_consultation": id_consultation})
                flash("consultation supprimé avec succès.", "success")
                return redirect(url_for('consultations_afficher', order_by="ASC", id_consultation_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('consultations_afficher', order_by="ASC", id_consultation_sel=0))
    else:
        # Pré-remplir les champs pour affichage
        with DBconnection() as mc:
            str_sql = """
                SELECT e.diagnostic_consult, e.diagnostic_consult, p.nom_patient, p.prenom_patient
                FROM t_consultation e
                JOIN t_consultation_patient de ON e.id_consultation = de.fk_consultation
                JOIN t_patient p ON de.fk_patient = p.id_patient
                WHERE e.id_consultation = %(id_consultation)s
            """
            mc.execute(str_sql, {"id_consultation": id_consultation})
            data = mc.fetchone()
            if data:
                form_delete.patient.data = f"{data['nom_patient']} {data['prenom_patient']}"
                form_delete.diagnostic_consult.data = data["diagnostic_consult"]
        return render_template("consultation/consultation_delete_wtf.html", form_delete=form_delete)

@app.route("/consultation_info/<int:id_consultation>", methods=['GET'])
def consultation_info(id_consultation):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    e.id_consultation,
                    e.date_consult,
                    e.motif_consult,
                    e.diagnostic_consult,
                    e.notes_consult,
                    p.nom_patient,
                    p.prenom_patient
                FROM t_consultation e
                JOIN t_consultation_patient de ON e.id_consultation = de.fk_consultation
                JOIN t_patient p ON de.fk_patient = p.id_patient
                WHERE e.id_consultation = %(id_consultation)s
            """
            mc_info.execute(strsql_info, {"id_consultation": id_consultation})
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos de l'consultation.", "danger")
        print(e)
        return redirect(url_for('consultations_afficher', order_by="ASC", id_consultation_sel=0))
    return render_template("consultation/consultation_info.html", data=data_info)