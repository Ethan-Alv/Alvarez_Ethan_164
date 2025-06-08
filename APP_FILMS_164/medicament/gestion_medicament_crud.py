# Imports
from flask import render_template, redirect, request, url_for, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.medicament.gestion_medicament_wtf_forms import (
    FormWTFAjouterMedicament, FormWTFUpdateMedicament, FormWTFDeleteMedicament
)

# Afficher
@app.route("/medicaments_afficher/<string:order_by>/<int:id_medicament_sel>", methods=['GET', 'POST'])
def medicaments_afficher(order_by, id_medicament_sel):
    data_medicaments = []
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT id_medicament, nom_medic, dosage_medic, forme_medic
                FROM t_medicament
                ORDER BY id_medicament ASC
            """
            mc.execute(strsql)
            data_medicaments = mc.fetchall()
    except Exception as e:
        flash("Erreur lors de l'affichage des médicaments.", "danger")
        print(e)
    return render_template("medicament/medicament_afficher.html", data=data_medicaments)

# Ajouter
@app.route("/medicament_ajouter", methods=['GET', 'POST'])
def medicament_ajouter_wtf():
    form = FormWTFAjouterMedicament()
    if request.method == "POST" and form.validate_on_submit():
        nom = form.nom_medic.data
        dosage = form.dosage_medic.data
        forme = form.forme_medic.data
        try:
            with DBconnection() as mconn_bd:
                strsql = "INSERT INTO t_medicament (nom_medic, dosage_medic, forme_medic) VALUES (%s, %s, %s)"
                mconn_bd.execute(strsql, (nom, dosage, forme))
            flash("Médicament ajouté avec succès !", "success")
            return redirect(url_for('medicaments_afficher', order_by='ASC', id_medicament_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout du médicament.", "danger")
            print(e)
    return render_template("medicament/medicament_ajouter_wtf.html", form=form)

# Modifier
@app.route("/medicament_update/<int:id_medicament>", methods=['GET', 'POST'])
def medicament_update_wtf(id_medicament):
    form_update = FormWTFUpdateMedicament()
    if request.method == "POST" and form_update.validate_on_submit():
        nom = form_update.nom_medic.data
        dosage = form_update.dosage_medic.data
        forme = form_update.forme_medic.data
        try:
            with DBconnection() as mconn_bd:
                strsql = "UPDATE t_medicament SET nom_medic=%s, dosage_medic=%s, forme_medic=%s WHERE id_medicament=%s"
                mconn_bd.execute(strsql, (nom, dosage, forme, id_medicament))
            flash("Médicament modifié avec succès !", "success")
            return redirect(url_for('medicaments_afficher', order_by='ASC', id_medicament_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification du médicament.", "danger")
            print(e)
    elif request.method == "GET":
        with DBconnection() as mc:
            strsql = "SELECT nom_medic, dosage_medic, forme_medic FROM t_medicament WHERE id_medicament=%s"
            mc.execute(strsql, (id_medicament,))
            data = mc.fetchone()
            if data:
                form_update.nom_medic.data = data["nom_medic"]
                form_update.dosage_medic.data = data["dosage_medic"]
                form_update.forme_medic.data = data["forme_medic"]
    return render_template("medicament/medicament_update_wtf.html", form_update=form_update)

# Supprimer
@app.route("/medicament_delete/<int:id_medicament>", methods=['GET', 'POST'])
def medicament_delete_wtf(id_medicament):
    form_delete = FormWTFDeleteMedicament()
    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    strsql = "DELETE FROM t_medicament WHERE id_medicament=%s"
                    mconn_bd.execute(strsql, (id_medicament,))
                flash("Médicament supprimé avec succès.", "success")
                return redirect(url_for('medicaments_afficher', order_by='ASC', id_medicament_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('medicaments_afficher', order_by='ASC', id_medicament_sel=0))
    else:
        with DBconnection() as mc:
            strsql = "SELECT nom_medic, dosage_medic, forme_medic FROM t_medicament WHERE id_medicament=%s"
            mc.execute(strsql, (id_medicament,))
            data = mc.fetchone()
            if data:
                form_delete.nom_medic.data = data["nom_medic"]
                form_delete.dosage_medic.data = data["dosage_medic"]
                form_delete.forme_medic.data = data["forme_medic"]
    return render_template("medicament/medicament_delete_wtf.html", form_delete=form_delete)
@app.route("/medicament_info/<int:id_medicament>", methods=['GET'])
def medicament_info(id_medicament):
    data_info = None
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT id_medicament, nom_medic, dosage_medic, forme_medic
                FROM t_medicament
                WHERE id_medicament = %s
            """
            mc.execute(strsql, (id_medicament,))
            data_info = mc.fetchone()
            if not data_info:
                flash("Médicament introuvable.", "danger")
                return redirect(url_for('medicaments_afficher', order_by='ASC', id_medicament_sel=0))
    except Exception as e:
        flash("Erreur lors de l'affichage des infos du médicament.", "danger")
        print(e)
        return redirect(url_for('medicaments_afficher', order_by='ASC', id_medicament_sel=0))
    return render_template("medicament/medicament_info.html", data=data_info)