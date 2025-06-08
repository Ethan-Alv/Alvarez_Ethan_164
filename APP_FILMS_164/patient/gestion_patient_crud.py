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
from APP_FILMS_164.patient.gestion_patient_wtf_forms import FormWTFAjouterPatient
from APP_FILMS_164.patient.gestion_patient_wtf_forms import FormWTFDeletePatient
from APP_FILMS_164.patient.gestion_patient_wtf_forms import FormWTFUpdatePatient


"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/patient_afficher/<string:order_by>/<int:id_patient_sel>", methods=['GET', 'POST'])
def patient_afficher(order_by, id_patient_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_patient_sel == 0:
                    strsql_patient_afficher = """SELECT
                                                    id_patient,
                                                    nom_patient,
                                                    prenom_patient,
                                                    email_patient
                                                FROM t_patient
                                                ORDER BY id_patient ASC;"""
                    mc_afficher.execute(strsql_patient_afficher)
                elif order_by == "ASC":
                    valeur_id_patient_selected_dictionnaire = {"id_patient": id_patient_sel}
                    strsql_patient_afficher = """
                        SELECT
                            id_patient,
                            nom_patient,
                            prenom_patient,
                            email_patient
                            FROM t_patient
                        WHERE id_patient = %(id_patient)s
                        ORDER BY id_patient ASC
                    """
                    mc_afficher.execute(strsql_patient_afficher, valeur_id_patient_selected_dictionnaire)
                else:
                    strsql_patient_afficher = """
                        SELECT
                            id_patient,
                            nom_patient,
                            prenom_patient,
                            email_patient
                            FROM t_patient
                        ORDER BY e.id_patient ASC
                    """
                    mc_afficher.execute(strsql_patient_afficher)

                data_patient = mc_afficher.fetchall()

                print("data_patient ", data_patient, " Type : ", type(data_patient))

                # Différencier les messages si la table est vide.
                if not data_patient and id_patient_sel == 0:
                    flash("""La table "t_patient" est vide. !!""", "warning")
                elif not data_patient and id_patient_sel > 0:
                    flash(f"Le patient demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données patient affichées !!", "success")

        except Exception as e:
            flash("Erreur lors de l'affichage des patient.", "danger")
            print(e)

    return render_template("patient/patient_afficher.html", data=data_patient)


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


@app.route("/patient_ajouter", methods=['GET', 'POST'])
def patient_ajouter_wtf():
    form = FormWTFAjouterPatient()
    if request.method == "POST" and form.validate_on_submit():
        try:
            with DBconnection() as mc:
                strsql = """INSERT INTO t_patient
                    (nom_patient, prenom_patient, date_naissance_pers, localite_patient, code_postal_patient, nom_rue_patient, numero_rue_patient, telephone_patient, email_patient)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                mc.execute(strsql, (
                    form.nom_patient.data, form.prenom_patient.data, form.date_naissance_pers.data,
                    form.localite_patient.data, form.code_postal_patient.data, form.nom_rue_patient.data,
                    form.numero_rue_patient.data, form.telephone_patient.data, form.email_patient.data
                ))
            flash("Patient ajouté avec succès.", "success")
            return redirect(url_for('patient_afficher', order_by='ASC', id_patient_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout du patient.", "danger")
            print(e)
    return render_template("patient/patient_ajouter_wtf.html", form=form)


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


@app.route("/patient_update/<int:id_patient>", methods=['GET', 'POST'])
def patient_update_wtf(id_patient):
    form_update = FormWTFUpdatePatient()
    with DBconnection() as mc:
        mc.execute("SELECT * FROM t_patient WHERE id_patient = %s", (id_patient,))
        patient_data = mc.fetchone()
    if not patient_data:
        flash("Le patient demandé n'existe pas.", "warning")
        return redirect(url_for('patient_afficher', order_by='ASC', id_patient_sel=0))

    if request.method == "POST" and form_update.validate_on_submit():
        try:
            with DBconnection() as mconn_bd:
                strsql_update = """
                    UPDATE t_patient SET
                        nom_patient=%s,
                        prenom_patient=%s,
                        date_naissance_pers=%s,
                        localite_patient=%s,
                        code_postal_patient=%s,
                        nom_rue_patient=%s,
                        numero_rue_patient=%s,
                        telephone_patient=%s,
                        email_patient=%s
                    WHERE id_patient=%s
                """
                mconn_bd.execute(strsql_update, (
                    form_update.nom_patient.data,
                    form_update.prenom_patient.data,
                    form_update.date_naissance_pers.data,
                    form_update.localite_patient.data,
                    form_update.code_postal_patient.data,
                    form_update.nom_rue_patient.data,
                    form_update.numero_rue_patient.data,
                    form_update.telephone_patient.data,
                    form_update.email_patient.data,
                    id_patient
                ))
            flash("Patient modifié avec succès !", "success")
            return redirect(url_for('patient_afficher', order_by='ASC', id_patient_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification du patient.", "danger")
            print(e)
    elif request.method == "GET":
        # Pré-remplir le formulaire avec les données existantes
        form_update.nom_patient.data = patient_data["nom_patient"]
        form_update.prenom_patient.data = patient_data["prenom_patient"]
        form_update.date_naissance_pers.data = patient_data["date_naissance_pers"]
        form_update.localite_patient.data = patient_data["localite_patient"]
        form_update.code_postal_patient.data = patient_data["code_postal_patient"]
        form_update.nom_rue_patient.data = patient_data["nom_rue_patient"]
        form_update.numero_rue_patient.data = patient_data["numero_rue_patient"]
        form_update.telephone_patient.data = patient_data["telephone_patient"]
        form_update.email_patient.data = patient_data["email_patient"]

    return render_template("patient/patient_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/examen_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/patient_delete/<int:id_patient>", methods=['GET', 'POST'])
def patient_delete_wtf(id_patient):
    form_delete = FormWTFDeletePatient()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # 1. Récupérer les id_dossier liés à ce patient
                    str_sql_get_dossiers = "SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s"
                    mconn_bd.execute(str_sql_get_dossiers, (id_patient,))
                    dossiers = mconn_bd.fetchall()
                    # 2. Supprimer dans t_dossier_patient
                    str_sql_delete_dossier_patient = "DELETE FROM t_dossier_patient WHERE fk_patient = %s"
                    mconn_bd.execute(str_sql_delete_dossier_patient, (id_patient,))
                    # 3. Supprimer les dossiers liés (optionnel, si tu veux supprimer les dossiers orphelins)
                    for dossier in dossiers:
                        str_sql_delete_dossier = "DELETE FROM t_dossier WHERE id_dossier = %s"
                        mconn_bd.execute(str_sql_delete_dossier, (dossier["fk_dossier"],))
                    # 4. Supprimer le patient
                    str_sql_delete_patient = "DELETE FROM t_patient WHERE id_patient = %s"
                    mconn_bd.execute(str_sql_delete_patient, (id_patient,))
                flash("Patient et données associées supprimés avec succès.", "success")
                return redirect(url_for('patient_afficher', order_by="ASC", id_patient_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
                return redirect(url_for('patient_afficher', order_by="ASC", id_patient_sel=0))
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('patient_afficher', order_by="ASC", id_patient_sel=0))
    else:
        # Pré-remplir les champs pour affichage
        with DBconnection() as mc:
            mc.execute("SELECT nom_patient, prenom_patient, telephone_patient FROM t_patient WHERE id_patient = %s", (id_patient,))
            data = mc.fetchone()
            if data:
                form_delete.nom_patient.data = data["nom_patient"]
                form_delete.prenom_patient.data = data["prenom_patient"]
                form_delete.telephone_patient.data = data["telephone_patient"]
        return render_template("patient/patient_delete_wtf.html", form_delete=form_delete)

@app.route("/patient_info/<int:id_patient>", methods=['GET'])
def patient_info(id_patient):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT *
                FROM t_patient
                WHERE id_patient = %s
            """
            mc_info.execute(strsql_info, (id_patient,))
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos du patient.", "danger")
        print(e)
        return redirect(url_for('patient_afficher', order_by="ASC", id_patient_sel=0))
    return render_template("patient/patient_info.html", data=data_info)