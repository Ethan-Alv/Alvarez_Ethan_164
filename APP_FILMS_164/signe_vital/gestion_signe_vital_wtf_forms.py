from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterSigneVital(FlaskForm):
    date_signe = DateField("Date du signe vital", validators=[DataRequired()])
    type_signe = StringField("Type de signe", validators=[DataRequired(), Length(min=2, max=50)])
    valeurs_signe = StringField("Valeurs", validators=[DataRequired(), Length(min=1, max=100)])
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    submit = SubmitField("Ajouter")

class FormWTFUpdateSigneVital(FlaskForm):
    date_signe = DateField("Date du signe vital", validators=[DataRequired()])
    type_signe = StringField("Type de signe", validators=[DataRequired(), Length(min=2, max=50)])
    valeurs_signe = StringField("Valeurs", validators=[DataRequired(), Length(min=1, max=100)])
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")

class FormWTFDeleteSigneVital(FlaskForm):
    type_signe = StringField("Type de signe")
    valeurs_signe = StringField("Valeurs")
    date_signe = StringField("Date du signe vital")
    patient = StringField("Patient")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")