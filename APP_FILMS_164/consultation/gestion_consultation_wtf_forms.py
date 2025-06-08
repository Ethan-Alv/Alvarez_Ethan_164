"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp
from datetime import datetime


class FormWTFAjouterconsultation(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    date_consult = DateField("Date de consultation", format='%Y-%m-%d', validators=[DataRequired()])
    motif_consult = StringField("Motif", validators=[DataRequired()])
    diagnostic_consult = StringField("Diagnostic", validators=[DataRequired()])
    notes_consult = TextAreaField("Notes")
    submit = SubmitField("Ajouter")


class FormWTFUpdateconsultation(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    date_consult = DateField("Date de consultation", format='%Y-%m-%d', validators=[DataRequired()])
    motif_consult = StringField("Motif", validators=[DataRequired()])
    diagnostic_consult = StringField("Diagnostic", validators=[DataRequired()])
    notes_consult = TextAreaField("Notes")
    submit = SubmitField("Mettre à jour")


class FormWTFDeleteconsultation(FlaskForm):
    patient = StringField("Patient")
    diagnostic_consult = StringField("Diagnostic")
    motif_consult = StringField("Motif de la consultation")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")
