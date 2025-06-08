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
from APP_FILMS_164.examen.gestion_examen_wtf_forms import FormWTFAjouterExamen
from APP_FILMS_164.examen.gestion_examen_wtf_forms import FormWTFDeleteExamen
from APP_FILMS_164.examen.gestion_examen_wtf_forms import FormWTFUpdateExamen


"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/examens_afficher/<string:order_by>/<int:id_examen_sel>")
def examens_afficher(order_by, id_examen_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_examen_sel == 0:
                    strsql_examen_afficher = """SELECT
                                                    e.id_examen,
                                                    e.type_examen,
                                                    p.nom_patient,
                                                    p.prenom_patient
                                                FROM t_examen e
                                                JOIN t_dossier_examen de ON e.id_examen = de.fk_examen
                                                JOIN t_dossier d ON de.fk_dossier = d.id_dossier
                                                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                                                JOIN t_patient p ON dp.fk_patient = p.id_patient
                                                ORDER BY e.id_examen ASC;
                    """
                    mc_afficher.execute(strsql_examen_afficher)
                elif order_by == "ASC":
                    valeur_id_examen_selected_dictionnaire = {"id_examen": id_examen_sel}
                    strsql_examen_afficher = """
                        SELECT
                            e.id_examen,
                            e.nom_examen AS type_examen,
                            p.nom_patient,
                            p.prenom_patient
                        FROM t_examen e
                        JOIN t_dossier_examen de ON e.id_examen = de.fk_examen
                        JOIN t_dossier d ON de.fk_dossier = d.id_dossier
                        JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                        JOIN t_patient p ON dp.fk_patient = p.id_patient
                        WHERE e.id_examen = %(id_examen)s
                        ORDER BY e.id_examen ASC
                    """
                    mc_afficher.execute(strsql_examen_afficher, valeur_id_examen_selected_dictionnaire)
                else:
                    strsql_examen_afficher = """
                        SELECT
                            e.id_examen,
                            e.type_examen,
                            p.nom_patient,
                            p.prenom_patient
                        FROM t_examen e
                        JOIN t_dossier_examen de ON e.id_examen = de.fk_examen
                        JOIN t_dossier d ON de.fk_dossier = d.id_dossier
                        JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                        JOIN t_patient p ON dp.fk_patient = p.id_patient
                        ORDER BY e.id_examen ASC
                    """
                    mc_afficher.execute(strsql_examen_afficher)

                data_examens = mc_afficher.fetchall()

                print("data_examens ", data_examens, " Type : ", type(data_examens))

                # Différencier les messages si la table est vide.
                if not data_examens and id_examen_sel == 0:
                    flash("""La table "t_examen" est vide. !!""", "warning")
                elif not data_examens and id_examen_sel > 0:
                    flash(f"L'examen demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données examens affichées !!", "success")

        except Exception as e:
            flash("Erreur lors de l'affichage des examens.", "danger")
            print(e)

    return render_template("examen/examen_afficher.html", data=data_examens)


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


@app.route("/examen_ajouter", methods=['GET', 'POST'])
def examen_ajouter_wtf():
    # Récupérer les patients dont le fk_dossier n'est pas dans t_dossier_examen
    with DBconnection() as mc:
        strsql = """
            SELECT dp.fk_dossier, p.id_patient, p.nom_patient, p.prenom_patient
                FROM t_dossier_patient dp
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                ORDER BY p.nom_patient, p.prenom_patient
        """
        mc.execute(strsql)
        patients = mc.fetchall()
        # Format pour SelectField : (fk_dossier, "Nom Prénom (id_patient)")
        patient_choices = [
            (str(row["fk_dossier"]), f"{row['nom_patient']} {row['prenom_patient']} ")
            for row in patients
        ]

    form = FormWTFAjouterExamen()
    form.patient_select.choices = patient_choices

    if request.method == "POST" and form.validate_on_submit():
        fk_dossier = form.patient_select.data
        type_examen = form.type_examen.data
        resultats_examen = form.resultats_examen.data
        jour = form.jour_examen.data
        mois = form.mois_examen.data
        annee = form.annee_examen.data
        date_examen = f"{annee}-{mois.zfill(2)}-{jour.zfill(2)}"

        try:
            with DBconnection() as mconn_bd:
                # Insérer l'examen
                strsql_insert_examen = """INSERT INTO t_examen (type_examen, date_examen, resultats_examen)
                                          VALUES (%s, %s, %s)"""
                mconn_bd.execute(strsql_insert_examen, (type_examen, date_examen, resultats_examen))
                id_examen = mconn_bd.lastrowid

                # Lier l'examen au dossier
                strsql_insert_dossier_examen = """INSERT INTO t_dossier_examen (fk_dossier, fk_examen)
                                                  VALUES (%s, %s)"""
                mconn_bd.execute(strsql_insert_dossier_examen, (fk_dossier, id_examen))

            flash("Examen ajouté avec succès !", "success")
            return redirect(url_for('examens_afficher', order_by='ASC', id_examen_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout de l'examen.", "danger")
            print(e)
    return render_template("examen/examen_ajouter_wtf.html", form=form)


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


@app.route("/examen_update/<int:id_examen>", methods=['GET', 'POST'])
def examen_update_wtf(id_examen):
    form_update = FormWTFUpdateExamen()

    # Récupérer tous les patients pour la liste déroulante
    with DBconnection() as mc:
        mc.execute("SELECT p.id_patient, p.nom_patient, p.prenom_patient FROM t_patient p")
        patients = mc.fetchall()
        patient_choices = [
            (str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']} (ID:{row['id_patient']})")
            for row in patients
        ]
    form_update.patient_select.choices = patient_choices

    if request.method == "POST" and form_update.validate_on_submit():
        id_patient = form_update.patient_select.data
        type_examen = form_update.type_examen.data
        resultats_examen = form_update.resultats_examen.data
        jour = form_update.jour_examen.data
        mois = form_update.mois_examen.data
        annee = form_update.annee_examen.data
        date_examen = f"{annee}-{mois.zfill(2)}-{jour.zfill(2)}"

        try:
            with DBconnection() as mconn_bd:
                # Mettre à jour t_examen
                strsql_update_examen = """UPDATE t_examen SET type_examen=%s, date_examen=%s, resultats_examen=%s WHERE id_examen=%s"""
                mconn_bd.execute(strsql_update_examen, (type_examen, date_examen, resultats_examen, id_examen))

                # Mettre à jour le patient lié via la table de liaison
                strsql_update_patient = """
                    UPDATE t_dossier_patient dp
                    JOIN t_dossier_examen de ON dp.fk_dossier = de.fk_dossier
                    SET dp.fk_patient = %s
                    WHERE de.fk_examen = %s
                """
                mconn_bd.execute(strsql_update_patient, (id_patient, id_examen))

            flash("Examen modifié avec succès !", "success")
            return redirect(url_for('examens_afficher', order_by='ASC', id_examen_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification de l'examen.", "danger")
            print(e)
    elif request.method == "GET":
        # Pré-remplir le formulaire avec les données existantes
        with DBconnection() as mc:
            strsql = """
                SELECT e.type_examen, e.date_examen, e.resultats_examen, p.id_patient
                FROM t_examen e
                JOIN t_dossier_examen de ON e.id_examen = de.fk_examen
                JOIN t_dossier d ON de.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                WHERE e.id_examen = %s
            """
            mc.execute(strsql, (id_examen,))
            data = mc.fetchone()
            if data:
                form_update.type_examen.data = data["type_examen"]
                form_update.resultats_examen.data = data["resultats_examen"]
                form_update.patient_select.data = str(data["id_patient"])
                # Séparer la date
                if data["date_examen"]:
                    annee, mois, jour = str(data["date_examen"]).split("-")
                    form_update.jour_examen.data = jour
                    form_update.mois_examen.data = mois
                    form_update.annee_examen.data = annee

    return render_template("examen/examen_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/examen_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/examen_delete/<int:id_examen>", methods=['GET', 'POST'])
def examen_delete_wtf(id_examen):
    form_delete = FormWTFDeleteExamen()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # Supprimer la liaison dans t_dossier_examen
                    str_sql_delete_liaison = "DELETE FROM t_dossier_examen WHERE fk_examen = %(id_examen)s"
                    mconn_bd.execute(str_sql_delete_liaison, {"id_examen": id_examen})
                    # Supprimer l'examen
                    str_sql_delete_examen = "DELETE FROM t_examen WHERE id_examen = %(id_examen)s"
                    mconn_bd.execute(str_sql_delete_examen, {"id_examen": id_examen})
                flash("Examen supprimé avec succès.", "success")
                return redirect(url_for('examens_afficher', order_by="ASC", id_examen_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('examens_afficher', order_by="ASC", id_examen_sel=0))
    else:
        # Pré-remplir les champs pour affichage
        with DBconnection() as mc:
            str_sql = """
                SELECT e.type_examen, e.resultats_examen, p.nom_patient, p.prenom_patient
                FROM t_examen e
                JOIN t_dossier_examen de ON e.id_examen = de.fk_examen
                JOIN t_dossier d ON de.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                WHERE e.id_examen = %(id_examen)s
            """
            mc.execute(str_sql, {"id_examen": id_examen})
            data = mc.fetchone()
            if data:
                form_delete.patient.data = f"{data['nom_patient']} {data['prenom_patient']}"
                form_delete.type_examen.data = data["type_examen"]
                form_delete.resultats_examen.data = data["resultats_examen"]
        return render_template("examen/examen_delete_wtf.html", form_delete=form_delete)

@app.route("/examen_info/<int:id_examen>", methods=['GET'])
def examen_info(id_examen):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    e.id_examen,
                    e.type_examen,
                    e.date_examen,
                    e.resultats_examen,
                    p.nom_patient,
                    p.prenom_patient
                    FROM t_examen e
                    JOIN t_dossier_examen de ON e.id_examen = de.fk_examen
                    JOIN t_dossier d ON de.fk_dossier = d.id_dossier
                    JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                    JOIN t_patient p ON dp.fk_patient = p.id_patient
                    WHERE e.id_examen = %(id_examen)s
            """
            mc_info.execute(strsql_info, {"id_examen": id_examen})
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos de l'examen.", "danger")
        print(e)
        return redirect(url_for('examens_afficher', order_by="ASC", id_examen_sel=0))
    return render_template("examen/examen_info.html", data=data_info)