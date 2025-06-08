from flask import render_template, request, redirect, url_for, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.prescription.gestion_prescription_wtf_forms import (
    FormWTFAjouterPrescription, FormWTFUpdatePrescription, FormWTFDeletePrescription
)

# Afficher
@app.route("/prescriptions_afficher/<string:order_by>/<int:id_prescription_sel>", methods=['GET', 'POST'])
def prescriptions_afficher(order_by, id_prescription_sel):
    data_prescriptions = []
    try:
        with DBconnection() as mc:
            strsql = """
                SELECT
                    p.id_prescription,
                    pat.nom_patient,
                    pat.prenom_patient,
                    p.posologie_prescr
                FROM t_prescription p
                JOIN t_dossier_prescription dp ON p.id_prescription = dp.fk_prescription
                JOIN t_dossier d ON dp.fk_dossier = d.id_dossier
                JOIN t_dossier_patient dp2 ON d.id_dossier = dp2.fk_dossier
                JOIN t_patient pat ON dp2.fk_patient = pat.id_patient
                ORDER BY p.id_prescription ASC
            """
            mc.execute(strsql)
            data_prescriptions = mc.fetchall()
    except Exception as e:
        flash("Erreur lors de l'affichage des prescriptions.", "danger")
        print(e)
    return render_template("prescription/prescription_afficher.html", data=data_prescriptions)

# Ajouter
@app.route("/prescription_ajouter", methods=['GET', 'POST'])
def prescription_ajouter_wtf():
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient")
        patients = mc.fetchall()
        patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]
        mc.execute("SELECT id_medecin, nom_medecin, prenom_medecin FROM t_medecin")
        medecins = mc.fetchall()
        medecin_choices = [(str(row["id_medecin"]), f"{row['nom_medecin']} {row['prenom_medecin']}") for row in medecins]
        mc.execute("SELECT id_medicament, nom_medic, dosage_medic, forme_medic FROM t_medicament")
        medicaments = mc.fetchall()
        medicament_choices = [
            (str(row["id_medicament"]), f"{row['nom_medic']} {row['dosage_medic']} {row['forme_medic']}")
            for row in medicaments
        ]

    form = FormWTFAjouterPrescription()
    form.patient_select.choices = patient_choices
    form.medecin_select.choices = medecin_choices
    form.medicament_select.choices = medicament_choices

    if request.method == "POST" and form.validate_on_submit():
        fk_patient = form.patient_select.data
        fk_medecin = form.medecin_select.data
        fk_medicament = form.medicament_select.data
        posologie = form.posologie_prescr.data
        duree = form.duree_traitement_prescr.data
        debut = form.debut_prescr.data
        fin = form.fin_prescr.data

        try:
            with DBconnection() as mconn_bd:
                # 1. Trouver le dossier du patient
                strsql_dossier = """
                    SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s LIMIT 1
                """
                mconn_bd.execute(strsql_dossier, (fk_patient,))
                dossier_row = mconn_bd.fetchone()
                if not dossier_row:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return render_template("prescription/prescription_ajouter_wtf.html", form=form)
                fk_dossier = dossier_row["fk_dossier"]

                # 2. Insérer la prescription
                strsql_insert = """
                    INSERT INTO t_prescription
                    (posologie_prescr, duree_traitement_prescr, debut_prescr, fin_prescr)
                    VALUES (%s, %s, %s, %s)
                """
                mconn_bd.execute(strsql_insert, (posologie, duree, debut, fin))
                id_prescription = mconn_bd.lastrowid

                # 3. Lier prescription au dossier
                strsql_liaison_dossier = """
                    INSERT INTO t_dossier_prescription (fk_dossier, fk_prescription)
                    VALUES (%s, %s)
                """
                mconn_bd.execute(strsql_liaison_dossier, (fk_dossier, id_prescription))

                # 4. Lier prescription au médecin
                strsql_liaison_medecin = """
                    INSERT INTO t_prescription_medecin (fk_prescription, fk_medecin)
                    VALUES (%s, %s)
                """
                mconn_bd.execute(strsql_liaison_medecin, (id_prescription, fk_medecin))

                # 5. Lier prescription au médicament
                strsql_liaison_medicament = """
                    INSERT INTO t_prescription_medicament (fk_prescription, fk_medicament)
                    VALUES (%s, %s)
                """
                mconn_bd.execute(strsql_liaison_medicament, (id_prescription, fk_medicament))

            flash("Prescription ajoutée avec succès !", "success")
            return redirect(url_for('prescriptions_afficher', order_by='ASC', id_prescription_sel=0))
        except Exception as e:
            flash("Erreur lors de l'ajout de la prescription.", "danger")
            print(e)
            return render_template("prescription/prescription_ajouter_wtf.html", form=form)
    # Affichage du formulaire en GET ou si POST non valide
    return render_template("prescription/prescription_ajouter_wtf.html", form=form)

# Modifier
@app.route("/prescription_update/<int:id_prescription>", methods=['GET', 'POST'])
def prescription_update_wtf(id_prescription):
    with DBconnection() as mc:
        mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient")
        patients = mc.fetchall()
        patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]
        mc.execute("SELECT id_medecin, nom_medecin, prenom_medecin FROM t_medecin")
        medecins = mc.fetchall()
        medecin_choices = [(str(row["id_medecin"]), f"{row['nom_medecin']} {row['prenom_medecin']}") for row in medecins]
        mc.execute("SELECT id_medicament, nom_medic, dosage_medic, forme_medic FROM t_medicament")
        medicaments = mc.fetchall()
        medicament_choices = [
            (str(row["id_medicament"]), f"{row['nom_medic']} {row['dosage_medic']} {row['forme_medic']}")
            for row in medicaments
        ]

    form_update = FormWTFUpdatePrescription()
    form_update.patient_select.choices = patient_choices
    form_update.medecin_select.choices = medecin_choices
    form_update.medicament_select.choices = medicament_choices

    if request.method == "POST" and form_update.validate_on_submit():
        fk_patient = form_update.patient_select.data
        fk_medecin = form_update.medecin_select.data
        fk_medicament = form_update.medicament_select.data
        posologie = form_update.posologie_prescr.data
        duree = form_update.duree_traitement_prescr.data
        debut = form_update.debut_prescr.data
        fin = form_update.fin_prescr.data

        try:
            with DBconnection() as mconn_bd:
                strsql_dossier = """
                    SELECT fk_dossier FROM t_dossier_patient WHERE fk_patient = %s LIMIT 1
                """
                mconn_bd.execute(strsql_dossier, (fk_patient,))
                dossier_row = mconn_bd.fetchone()
                if not dossier_row:
                    flash("Aucun dossier trouvé pour ce patient.", "danger")
                    return render_template("prescription/prescription_update_wtf.html", form_update=form_update)
                fk_dossier = dossier_row["fk_dossier"]

                strsql_update = """
                    UPDATE t_prescription
                    SET posologie_prescr=%s, duree_traitement_prescr=%s, debut_prescr=%s, fin_prescr=%s
                    WHERE id_prescription=%s
                """
                mconn_bd.execute(strsql_update, (posologie, duree, debut, fin, id_prescription))

                strsql_update_dossier = """
                    UPDATE t_dossier_prescription
                    SET fk_dossier=%s
                    WHERE fk_prescription=%s
                """
                mconn_bd.execute(strsql_update_dossier, (fk_dossier, id_prescription))

                strsql_update_medecin = """
                    UPDATE t_prescription_medecin
                    SET fk_medecin=%s
                    WHERE fk_prescription=%s
                """
                mconn_bd.execute(strsql_update_medecin, (fk_medecin, id_prescription))

                strsql_update_medicament = """
                    UPDATE t_prescription_medicament
                    SET fk_medicament=%s
                    WHERE fk_prescription=%s
                """
                mconn_bd.execute(strsql_update_medicament, (fk_medicament, id_prescription))

            flash("Prescription modifiée avec succès !", "success")
            return redirect(url_for('prescriptions_afficher', order_by='ASC', id_prescription_sel=0))
        except Exception as e:
            flash("Erreur lors de la modification de la prescription.", "danger")
            print(e)
    elif request.method == "GET":
        with DBconnection() as mc:
            strsql = """
                SELECT
                    p.posologie_prescr, p.duree_traitement_prescr, p.debut_prescr, p.fin_prescr,
                    dp.fk_dossier, pm.fk_medecin, pmed.fk_medicament, dp2.fk_patient
                FROM t_prescription p
                JOIN t_dossier_prescription dp ON p.id_prescription = dp.fk_prescription
                JOIN t_dossier_patient dp2 ON dp.fk_dossier = dp2.fk_dossier
                JOIN t_prescription_medecin pm ON p.id_prescription = pm.fk_prescription
                JOIN t_prescription_medicament pmed ON p.id_prescription = pmed.fk_prescription
                WHERE p.id_prescription = %s
            """
            mc.execute(strsql, (id_prescription,))
            data = mc.fetchone()
            if data:
                form_update.posologie_prescr.data = data["posologie_prescr"]
                form_update.duree_traitement_prescr.data = data["duree_traitement_prescr"]
                form_update.debut_prescr.data = data["debut_prescr"]
                form_update.fin_prescr.data = data["fin_prescr"]
                form_update.patient_select.data = str(data["fk_patient"])
                form_update.dossier_select.data = str(data["fk_dossier"])
                form_update.medecin_select.data = str(data["fk_medecin"])
                form_update.medicament_select.data = str(data["fk_medicament"])

    return render_template("prescription/prescription_update_wtf.html", form_update=form_update)

# Supprimer
@app.route("/prescription_delete/<int:id_prescription>", methods=['GET', 'POST'])
def prescription_delete_wtf(id_prescription):
    form_delete = FormWTFDeletePrescription()

    if request.method == "POST":
        if form_delete.submit_btn_conf_del.data:
            try:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_dossier_prescription WHERE fk_prescription = %(id_prescription)s", {"id_prescription": id_prescription})
                    mconn_bd.execute("DELETE FROM t_prescription_medecin WHERE fk_prescription = %(id_prescription)s", {"id_prescription": id_prescription})
                    mconn_bd.execute("DELETE FROM t_prescription_medicament WHERE fk_prescription = %(id_prescription)s", {"id_prescription": id_prescription})
                    mconn_bd.execute("DELETE FROM t_prescription WHERE id_prescription = %(id_prescription)s", {"id_prescription": id_prescription})
                flash("Prescription supprimée avec succès.", "success")
                return redirect(url_for('prescriptions_afficher', order_by="ASC", id_prescription_sel=0))
            except Exception as e:
                flash("Erreur lors de la suppression.", "danger")
                print(e)
        elif form_delete.submit_btn_annuler.data:
            return redirect(url_for('prescriptions_afficher', order_by="ASC", id_prescription_sel=0))

    else:
        with DBconnection() as mc:
            str_sql = """
                SELECT
                    p.id_prescription, p.posologie_prescr, p.duree_traitement_prescr, p.debut_prescr, p.fin_prescr,
                    pat.id_patient, pat.nom_patient, pat.prenom_patient,
                    m.nom_medecin, med.nom_medic
                FROM t_prescription p
                LEFT JOIN t_dossier_prescription dp ON p.id_prescription = dp.fk_prescription
                LEFT JOIN t_dossier d ON dp.fk_dossier = d.id_dossier
                LEFT JOIN t_dossier_patient dp2 ON d.id_dossier = dp2.fk_dossier
                LEFT JOIN t_patient pat ON dp2.fk_patient = pat.id_patient
                LEFT JOIN t_prescription_medecin pm ON p.id_prescription = pm.fk_prescription
                LEFT JOIN t_medecin m ON pm.fk_medecin = m.id_medecin
                LEFT JOIN t_prescription_medicament pmed ON p.id_prescription = pmed.fk_prescription
                LEFT JOIN t_medicament med ON pmed.fk_medicament = med.id_medicament
                WHERE p.id_prescription = %(id_prescription)s
            """
            mc.execute(str_sql, {"id_prescription": id_prescription})
            data = mc.fetchone()
            if not data or data["id_prescription"] is None:
                flash("Prescription introuvable.", "danger")
                return redirect(url_for('prescriptions_afficher', order_by="ASC", id_prescription_sel=0))

            # Remplir la liste des patients pour le SelectField
            mc.execute("SELECT id_patient, nom_patient, prenom_patient FROM t_patient")
            patients = mc.fetchall()
            patient_choices = [(str(row["id_patient"]), f"{row['nom_patient']} {row['prenom_patient']}") for row in patients]
            form_delete.patient_select.choices = patient_choices
            form_delete.patient_select.data = str(data["id_patient"])

            form_delete.medecin.data = data["nom_medecin"] if data["nom_medecin"] else ""
            form_delete.medicament.data = data["nom_medic"] if data["nom_medic"] else ""
            form_delete.posologie_prescr.data = data["posologie_prescr"] if data["posologie_prescr"] else ""
            form_delete.duree_traitement_prescr.data = data["duree_traitement_prescr"] if data["duree_traitement_prescr"] else ""
            form_delete.debut_prescr.data = str(data["debut_prescr"]) if data["debut_prescr"] else ""
            form_delete.fin_prescr.data = str(data["fin_prescr"]) if data["fin_prescr"] else ""

        return render_template("prescription/prescription_delete_wtf.html", form_delete=form_delete)

# Info
@app.route("/prescription_info/<int:id_prescription>", methods=['GET'])
def prescription_info(id_prescription):
    data_info = None
    try:
        with DBconnection() as mc_info:
            strsql_info = """
                SELECT
                    p.id_prescription,
                    p.posologie_prescr,
                    p.duree_traitement_prescr,
                    p.debut_prescr,
                    p.fin_prescr,
                    pat.nom_patient,
                    pat.prenom_patient,
                    m.nom_medecin,
                    med.nom_medic,
                    med.dosage_medic,
                    med.forme_medic
                FROM t_prescription p
                LEFT JOIN t_dossier_prescription dp ON p.id_prescription = dp.fk_prescription
                LEFT JOIN t_dossier d ON dp.fk_dossier = d.id_dossier
                LEFT JOIN t_dossier_patient dp2 ON d.id_dossier = dp2.fk_dossier
                LEFT JOIN t_patient pat ON dp2.fk_patient = pat.id_patient
                LEFT JOIN t_prescription_medecin pm ON p.id_prescription = pm.fk_prescription
                LEFT JOIN t_medecin m ON pm.fk_medecin = m.id_medecin
                LEFT JOIN t_prescription_medicament pmed ON p.id_prescription = pmed.fk_prescription
                LEFT JOIN t_medicament med ON pmed.fk_medicament = med.id_medicament
                WHERE p.id_prescription = %(id_prescription)s
            """
            mc_info.execute(strsql_info, {"id_prescription": id_prescription})
            data_info = mc_info.fetchone()
            if not data_info or data_info["id_prescription"] is None:
                flash("Prescription introuvable.", "danger")
                return redirect(url_for('prescriptions_afficher', order_by="ASC", id_prescription_sel=0))
    except Exception as e:
        flash("Erreur lors de la récupération des infos de la prescription.", "danger")
        print(e)
        return redirect(url_for('prescriptions_afficher', order_by="ASC", id_prescription_sel=0))
    return render_template("prescription/prescription_info.html", data=data_info)