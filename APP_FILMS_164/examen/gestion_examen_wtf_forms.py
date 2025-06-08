"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp
from datetime import datetime


class FormWTFAjouterExamen(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    type_examen = StringField("Type d'examen", validators=[DataRequired()])
    resultats_examen = StringField("Résultats de l'examen", validators=[DataRequired()])
    jour_examen = SelectField("Jour", choices=[(str(i), str(i)) for i in range(1, 32)], validators=[DataRequired()])
    mois_examen = SelectField("Mois", choices=[(str(i), str(i)) for i in range(1, 13)], validators=[DataRequired()])
    current_year = datetime.now().year
    annee_examen = SelectField(
        "Année",
        choices=[(str(i), str(i)) for i in range(current_year, 1999, -1)],  # Par exemple de 2025 à 2000
        validators=[DataRequired()]
    )
    submit = SubmitField("Ajouter")


class FormWTFUpdateExamen(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    type_examen = StringField("Type d'examen", validators=[DataRequired()])
    resultats_examen = StringField("Résultats de l'examen", validators=[DataRequired()])
    jour_examen = SelectField("Jour", choices=[(str(i), str(i)) for i in range(1, 32)], validators=[DataRequired()])
    mois_examen = SelectField("Mois", choices=[(str(i), str(i)) for i in range(1, 13)], validators=[DataRequired()])
    annee_examen = SelectField("Année", choices=[(str(i), str(i)) for i in range(datetime.now().year, 1999, -1)], validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")


class FormWTFDeleteExamen(FlaskForm):
    patient = StringField("Patient")
    type_examen = StringField("Type d'examen")
    resultats_examen = StringField("Résultat de l'examen")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")
