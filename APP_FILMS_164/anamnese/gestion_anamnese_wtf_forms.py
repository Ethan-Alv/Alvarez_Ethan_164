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


class FormWTFAjouterAnamnese(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    histoire_de_vie_anamn = StringField("Histoire de vie", validators=[DataRequired()])
    antecedent_medicaux_anamn = StringField("Antécédents médicaux", validators=[DataRequired()])
    probleme_anamn = StringField("Problèmes", validators=[DataRequired()])
    allergies_anamn = StringField("Allergies", validators=[DataRequired()])
    submit = SubmitField("Ajouter")

class FormWTFUpdateAnamnese(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    histoire_de_vie_anamn = StringField("Histoire de vie", validators=[DataRequired()])
    antecedent_medicaux_anamn = StringField("Antécédents médicaux", validators=[DataRequired()])
    probleme_anamn = StringField("Problèmes", validators=[DataRequired()])
    allergies_anamn = StringField("Allergies", validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")


class FormWTFDeleteAnamnese(FlaskForm):
    patient = StringField("Patient")
    histoire_de_vie_anamn = StringField("Histoire de vie")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")
