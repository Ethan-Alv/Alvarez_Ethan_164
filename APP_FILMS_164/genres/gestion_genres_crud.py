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
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteDossier
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT
                                                    dp.fk_dossier AS id_dossier,
                                                    p.nom_patient,
                                                    p.prenom_patient,
                                                    d.statut_dossier
                                                FROM
                                                    t_dossier_patient dp
                                                JOIN
                                                    t_patient p ON dp.fk_patient = p.id_patient
                                                JOIN
                                                    t_dossier d ON dp.fk_dossier = d.id_dossier
                                                ORDER BY
                                                    dp.fk_dossier, p.nom_patient, p.prenom_patient;"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    valeur_id_genre_selected_dictionnaire = {"id_dossier": id_genre_sel}
                    strsql_genres_afficher = """SELECT
                                                    dp.fk_dossier AS id_dossier,
                                                    p.nom_patient,
                                                    p.prenom_patient,
                                                    d.statut_dossier
                                                FROM
                                                    t_dossier_patient dp
                                                JOIN
                                                    t_patient p ON dp.fk_patient = p.id_patient
                                                JOIN
                                                    t_dossier d ON dp.fk_dossier = d.id_dossier
                                                WHERE
                                                    dp.fk_dossier = %(id_dossier)s
                                                ORDER BY
                                                    dp.fk_dossier, p.nom_patient, p.prenom_patient;"""
                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT
                                                    dp.fk_dossier AS id_dossier,
                                                    p.nom_patient,
                                                    p.prenom_patient,
                                                    d.statut_dossier
                                                FROM
                                                    t_dossier_patient dp
                                                JOIN
                                                    t_patient p ON dp.fk_patient = p.id_patient
                                                JOIN
                                                    t_dossier d ON dp.fk_dossier = d.id_dossier
                                                ORDER BY
                                                    dp.fk_dossier, p.nom_patient, p.prenom_patient;"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_dossier ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données genres affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


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


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    # Remplir la liste déroulante des patients sans dossier
    with DBconnection() as mconn_bd:
        mconn_bd.execute("""
            SELECT id_patient, nom_patient, prenom_patient
            FROM t_patient
            WHERE id_patient NOT IN (SELECT fk_patient FROM t_dossier_patient WHERE fk_patient IS NOT NULL)
        """)
        patients = mconn_bd.fetchall()
        form.patient.choices = [(row["id_patient"], f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]

    if request.method == "POST":
        print("POST reçu")
        print(form.errors)
        print("submit.data =", form.submit.data)
        try:
            if form.validate_on_submit():
                print(">>> DANS LE BLOC VALIDATE_ON_SUBMIT")
                # Recompose la date d'ouverture
                ouverture = f"{form.ouverture_annee.data}-{form.ouverture_mois.data}-{form.ouverture_jour.data}"
                # Recompose la date de cloture si tous les champs sont remplis, sinon None
                if form.cloture_jour.data and form.cloture_mois.data and form.cloture_annee.data:
                    cloture = f"{form.cloture_annee.data}-{form.cloture_mois.data}-{form.cloture_jour.data}"
                else:
                    cloture = None
                statut = form.statut_dossier.data
                patient_id = form.patient.data

                # Si cloture n'est pas une date valide (None ou format incorrect), on force à None
                if not cloture or str(cloture) in ["", "None", "jj.mm.aaaa"]:
                    cloture = None

                # Validation personnalisée
                if statut != "Actif" and not cloture:
                    flash("La date de clôture est obligatoire si le dossier n'est pas Actif.", "danger")
                    return render_template("genres/genres_ajouter_wtf.html", form=form)

                valeurs_insertion_dictionnaire = {
                    "ouverture": ouverture,
                    "cloture": cloture,
                    "statut": statut,
                    "fk_patient": patient_id
                }
                strsql_insert_dossier = """
                    INSERT INTO t_dossier (ouverture_dossier, cloture_dossier, statut_dossier)
                    VALUES (%(ouverture)s, %(cloture)s, %(statut)s)
                """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_dossier, valeurs_insertion_dictionnaire)
                    id_dossier = mconn_bd.lastrowid

                    strsql_insert_dossier_patient = """
                        INSERT INTO t_dossier_patient (fk_patient, fk_dossier)
                        VALUES (%(fk_patient)s, %(fk_dossier)s)
                    """
                    valeurs_relation = {
                        "fk_patient": patient_id,
                        "fk_dossier": id_dossier
                    }
                    mconn_bd.execute(strsql_insert_dossier_patient, valeurs_relation)
                    
                flash(f"Dossier ajouté !", "success")
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))
        except Exception as Exception_genres_ajouter_wtf:
            print("ERREUR SQL/PYTHON :", Exception_genres_ajouter_wtf)  # <-- Ajoute ceci
            flash("Erreur lors de l'ajout du dossier.", "danger")
    return render_template("genres/genres_ajouter_wtf.html", form=form)


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


@app.route("/dossier_update/<int:id_dossier>", methods=['GET', 'POST'])
def dossier_update_wtf(id_dossier):
    form = FormWTFUpdateGenre()
    # Remplir la liste déroulante des patients
    with DBconnection() as mconn_bd:
        mconn_bd.execute("""
            SELECT id_patient, nom_patient, prenom_patient
            FROM t_patient
        """)
        patients = mconn_bd.fetchall()
        form.patient.choices = [(row["id_patient"], f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]

    try:
        if request.method == "POST" and form.submit.data:
            ouverture = f"{form.ouverture_annee.data}-{form.ouverture_mois.data}-{form.ouverture_jour.data}"
            if form.cloture_jour.data and form.cloture_mois.data and form.cloture_annee.data:
                cloture = f"{form.cloture_annee.data}-{form.cloture_mois.data}-{form.cloture_jour.data}"
            else:
                cloture = None
            statut = form.statut_dossier.data
            patient_id = form.patient.data

            # Validation personnalisée
            if statut != "Actif" and not cloture:
                flash("La date de clôture est obligatoire si le dossier n'est pas Actif.", "danger")
                return render_template("genres/genre_update_wtf.html", form=form)

            valeurs_update = {
                "ouverture": ouverture,
                "cloture": cloture,
                "statut": statut,
                "id_dossier": id_dossier
            }
            str_sql_update_dossier = """
                UPDATE t_dossier
                SET ouverture_dossier = %(ouverture)s,
                    cloture_dossier = %(cloture)s,
                    statut_dossier = %(statut)s
                WHERE id_dossier = %(id_dossier)s
            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_dossier, valeurs_update)
                # Mettre à jour la liaison patient-dossier
                str_sql_update_liaison = """
                    UPDATE t_dossier_patient
                    SET fk_patient = %(fk_patient)s
                    WHERE fk_dossier = %(id_dossier)s
                """
                mconn_bd.execute(str_sql_update_liaison, {"fk_patient": patient_id, "id_dossier": id_dossier})

            flash("Dossier mis à jour !", "success")
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        elif request.method == "GET":
            # Charger les données existantes
            str_sql = """
                SELECT d.*, dp.fk_patient
                FROM t_dossier d
                JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                WHERE d.id_dossier = %(id_dossier)s
            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql, {"id_dossier": id_dossier})
                data = mconn_bd.fetchone()
            # Pré-remplir le formulaire
            if data:
                form.ouverture_jour.data = data["ouverture_dossier"].day
                form.ouverture_mois.data = str(data["ouverture_dossier"].month).zfill(2)
                form.ouverture_annee.data = str(data["ouverture_dossier"].year)
                if data["cloture_dossier"]:
                    form.cloture_jour.data = str(data["cloture_dossier"].day).zfill(2)
                    form.cloture_mois.data = str(data["cloture_dossier"].month).zfill(2)
                    form.cloture_annee.data = str(data["cloture_dossier"].year)
                form.statut_dossier.data = data["statut_dossier"]
                form.patient.data = data["fk_patient"]

    except Exception as e:
        flash("Erreur lors de la mise à jour du dossier.", "danger")
        print(e)

    return render_template("genres/genre_update_wtf.html", form=form)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""

@app.route("/dossier_info/<int:id_dossier>", methods=['GET'])
def dossier_info(id_dossier):
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    p.id_patient, p.nom_patient, p.prenom_patient, p.date_naissance_pers,
                    p.localite_patient, p.code_postal_patient, p.nom_rue_patient, p.numero_rue_patient,
                    p.telephone_patient, p.email_patient,
                    d.id_dossier, d.ouverture_dossier, d.cloture_dossier, d.statut_dossier
                FROM t_dossier_patient dp
                JOIN t_patient p ON dp.fk_patient = p.id_patient
                JOIN t_dossier d ON dp.fk_dossier = d.id_dossier
                WHERE d.id_dossier = %(id_dossier)s
            """
            mc_info.execute(strsql_info, {"id_dossier": id_dossier})
            data_info = mc_info.fetchone()
        return render_template("genres/dossier_info.html", data=data_info)
    except Exception as e:
        flash("Erreur lors de la récupération des infos du dossier.", "danger")
        return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

@app.route("/dossier_delete/<int:id_dossier>", methods=['GET', 'POST'])
def dossier_delete_wtf(id_dossier):
    form_delete = FormWTFDeleteDossier()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Affiche le bouton "Effacer dossier" pour confirmation
                return render_template("genres/dossier_delete_wtf.html", form_delete=form_delete, btn_submit_del=True)

            if form_delete.submit_btn_del.data:
                # Suppression réelle : supprimer toutes les références au dossier dans les tables liées
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_dossier_anamnese WHERE fk_dossier = %(id)s", {"id": id_dossier})
                    mconn_bd.execute("DELETE FROM t_dossier_examen WHERE fk_dossier = %(id)s", {"id": id_dossier})
                    mconn_bd.execute("DELETE FROM t_dossier_patient WHERE fk_dossier = %(id)s", {"id": id_dossier})
                    mconn_bd.execute("DELETE FROM t_dossier_prescription WHERE fk_dossier = %(id)s", {"id": id_dossier})
                    mconn_bd.execute("DELETE FROM t_dossier_rapport WHERE fk_dossier = %(id)s", {"id": id_dossier})
                    mconn_bd.execute("DELETE FROM t_dossier_signe_vital WHERE fk_dossier = %(id)s", {"id": id_dossier})
                    mconn_bd.execute("DELETE FROM t_dossier WHERE id_dossier = %(id)s", {"id": id_dossier})
                flash("Dossier supprimé !", "success")
                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        elif request.method == "GET":
            # Charger les infos du dossier et du patient
            with DBconnection() as mconn_bd:
                mconn_bd.execute("""
                    SELECT d.ouverture_dossier, d.cloture_dossier, d.statut_dossier,
                           p.nom_patient, p.prenom_patient
                    FROM t_dossier d
                    JOIN t_dossier_patient dp ON d.id_dossier = dp.fk_dossier
                    JOIN t_patient p ON dp.fk_patient = p.id_patient
                    WHERE d.id_dossier = %(id)s
                """, {"id": id_dossier})
                data = mconn_bd.fetchone()
            # Pré-remplir le formulaire en lecture seule
            if data:
                form_delete.ouverture.data = data["ouverture_dossier"]
                form_delete.cloture.data = data["cloture_dossier"] or "Non clôturé"
                form_delete.statut.data = data["statut_dossier"]
                form_delete.patient.data = f"{data['nom_patient']} {data['prenom_patient']}"

    except Exception as e:
        flash("Erreur lors de la suppression du dossier.", "danger")
        print(e)

    return render_template("genres/dossier_delete_wtf.html", form_delete=form_delete, btn_submit_del=False)