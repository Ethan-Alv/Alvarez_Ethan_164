from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class FormWTFAjouterPatient(FlaskForm):
    nom_patient = StringField("Nom", validators=[DataRequired()])
    prenom_patient = StringField("Prénom", validators=[DataRequired()])
    date_naissance_pers = DateField("Date de naissance", format='%Y-%m-%d', validators=[DataRequired()])
    localite_patient = StringField("Localité", validators=[DataRequired()])
    code_postal_patient = StringField("Code postal", validators=[DataRequired()])
    nom_rue_patient = StringField("Nom de rue", validators=[DataRequired()])
    numero_rue_patient = StringField("Numéro de rue", validators=[DataRequired()])
    telephone_patient = StringField("Téléphone", validators=[DataRequired()])
    email_patient = StringField("Email", validators=[DataRequired()])  # <-- Retirer Email()
    submit = SubmitField("Ajouter")

class FormWTFUpdatePatient(FormWTFAjouterPatient):
    nom_patient = StringField("Nom", validators=[DataRequired()])
    prenom_patient = StringField("Prénom", validators=[DataRequired()])
    date_naissance_pers = DateField("Date de naissance", format='%Y-%m-%d', validators=[DataRequired()])
    localite_patient = StringField("Localité", validators=[DataRequired()])
    code_postal_patient = StringField("Code postal", validators=[DataRequired()])
    nom_rue_patient = StringField("Nom de rue", validators=[DataRequired()])
    numero_rue_patient = StringField("Numéro de rue", validators=[DataRequired()])
    telephone_patient = StringField("Téléphone", validators=[DataRequired()])
    email_patient = StringField("Email", validators=[DataRequired()])  # <-- Retirer Email()
    submit = SubmitField("Mettre à jour")

class FormWTFDeletePatient(FlaskForm):
    nom_patient = StringField("Nom")
    prenom_patient = StringField("Prénom")
    telephone_patient = StringField("Téléphone")
    submit_btn_conf_del = SubmitField("Supprimer toutes les données de ce patient?")
    submit_btn_annuler = SubmitField("Annuler")
