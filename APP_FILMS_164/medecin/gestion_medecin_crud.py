from flask import render_template, request, redirect, url_for, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.medecin.gestion_medecin_wtf_forms import (
    FormWTFAjouterMedecin, FormWTFUpdateMedecin, FormWTFDeleteMedecin
)

@app.route("/medecins_afficher/<string:order_by>/<int:id_medecin_sel>", methods=['GET', 'POST'])
def medecins_afficher(order_by, id_medecin_sel):
    data_medecins = []
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT
                    m.id_medecin,
                    m.nom_medecin,
                    m.prenom_medecin,
                    m.telephone_medecin,
                    m.email_medecin
                FROM t_medecin m
                ORDER BY m.id_medecin ASC
            """
            mc.execute(strsql)
            data_medecins = mc.fetchall()
    except Exception as e:
        flash("Erreur lors de l'affichage des médecins.", "danger")
        print(e)
    return render_template("medecin/medecin_afficher.html", data=data_medecins)

@app.route("/medecin_ajouter", methods=['GET', 'POST'])
def medecin_ajouter_wtf():
    form = FormWTFAjouterMedecin()
    if request.method == "POST" and form.validate_on_submit():
        nom = form.nom_medecin.data
        prenom = form.prenom_medecin.data
        telephone = form.telephone_medecin.data
        email = form.email_medecin.data

        try:
            with DBconnection() as mconn_bd:
                strsql_insert = """
                    INSERT INTO t_medecin (nom_medecin, prenom_medecin, telephone_medecin, email_medecin)
                    VALUES (%s, %s, %s, %s)
                """
                mconn_bd.execute(strsql_insert, (nom, prenom, telephone, email))
            flash("Médecin ajouté avec succès !", "success")
            return redirect(url_for('medecins_afficher', order_by='ASC', id_medecin_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout du médecin.", "danger")
            print(e)
    return render_template("medecin/medecin_ajouter_wtf.html", form=form)

@app.route("/medecin_update/<int:id_medecin>", methods=['GET', 'POST'])
def medecin_update_wtf(id_medecin):
    form_update = FormWTFUpdateMedecin()
    if request.method == "POST" and form_update.validate_on_submit():
        nom = form_update.nom_medecin.data
        prenom = form_update.prenom_medecin.data
        telephone = form_update.telephone_medecin.data
        email = form_update.email_medecin.data

        try:
            with DBconnection() as mconn_bd:
                strsql_update = """
                    UPDATE t_medecin
                    SET nom_medecin=%s, prenom_medecin=%s, telephone_medecin=%s, email_medecin=%s
                    WHERE id_medecin=%s
                """
                mconn_bd.execute(strsql_update, (nom, prenom, telephone, email, id_medecin))
            flash("Médecin modifié avec succès !", "success")
            return redirect(url_for('medecins_afficher', order_by='ASC', id_medecin_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification du médecin.", "danger")
            print(e)
    elif request.method == "GET":
        with DBconnection() as mc:
            strsql = """
                SELECT nom_medecin, prenom_medecin, telephone_medecin, email_medecin
                FROM t_medecin
                WHERE id_medecin = %s
            """
            mc.execute(strsql, (id_medecin,))
            data = mc.fetchone()
            if data:
                form_update.nom_medecin.data = data["nom_medecin"]
                form_update.prenom_medecin.data = data["prenom_medecin"]
                form_update.telephone_medecin.data = data["telephone_medecin"]
                form_update.email_medecin.data = data["email_medecin"]

    return render_template("medecin/medecin_update_wtf.html", form_update=form_update)

@app.route("/medecin_delete/<int:id_medecin>", methods=['GET', 'POST'])
def medecin_delete_wtf(id_medecin):
    form_delete = FormWTFDeleteMedecin()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    # Supprimer la liaison dans t_prescription_medecin
                    mconn_bd.execute("DELETE FROM t_prescription_medecin WHERE fk_medecin = %(id_medecin)s", {"id_medecin": id_medecin})
                    # Supprimer le médecin
                    mconn_bd.execute("DELETE FROM t_medecin WHERE id_medecin = %(id_medecin)s", {"id_medecin": id_medecin})
                flash("Médecin supprimé avec succès.", "success")
                return redirect(url_for('medecins_afficher', order_by="ASC", id_medecin_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('medecins_afficher', order_by="ASC", id_medecin_sel=0))
    else:
        with DBconnection() as mc:
            str_sql = """
                SELECT nom_medecin, prenom_medecin, telephone_medecin, email_medecin
                FROM t_medecin
                WHERE id_medecin = %(id_medecin)s
            """
            mc.execute(str_sql, {"id_medecin": id_medecin})
            data = mc.fetchone()
            if data:
                form_delete.nom_medecin.data = data["nom_medecin"]
                form_delete.prenom_medecin.data = data["prenom_medecin"]
                form_delete.telephone_medecin.data = data["telephone_medecin"]
                form_delete.email_medecin.data = data["email_medecin"]
        if not data:
            flash("Prescription introuvable.", "danger")
            return redirect(url_for('prescriptions_afficher', order_by="ASC", id_prescription_sel=0))

@app.route("/medecin_info/<int:id_medecin>")
def medecin_info(id_medecin):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    m.id_medecin,
                    m.nom_medecin,
                    m.prenom_medecin,
                    m.telephone_medecin,
                    m.email_medecin
                FROM t_medecin m
                WHERE m.id_medecin = %(id_medecin)s
            """
            mc_info.execute(strsql_info, {"id_medecin": id_medecin})
            data_info = mc_info.fetchone()
    except Exception as e:
        flash("Erreur lors de la récupération des infos du médecin.", "danger")
        print(e)
        return redirect(url_for('medecins_afficher', order_by="ASC", id_medecin_sel=0))
    return render_template("medecin/medecin_info.html", data=data_info)