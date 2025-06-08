from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterMedecin(FlaskForm):
    nom_medecin = StringField("Nom", validators=[DataRequired(), Length(min=2, max=50)])
    prenom_medecin = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=50)])
    telephone_medecin = StringField("Téléphone", validators=[DataRequired(), Length(min=8, max=20)])
    email_medecin = StringField("Email")
    submit = SubmitField("Ajouter")

class FormWTFUpdateMedecin(FlaskForm):
    nom_medecin = StringField("Nom", validators=[DataRequired(), Length(min=2, max=50)])
    prenom_medecin = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=50)])
    telephone_medecin = StringField("Téléphone", validators=[DataRequired(), Length(min=8, max=20)])
    email_medecin = StringField("Email")    
    submit = SubmitField("Mettre à jour")

class FormWTFDeleteMedecin(FlaskForm):
    nom_medecin = StringField("Nom")
    prenom_medecin = StringField("Prénom")
    telephone_medecin = StringField("Téléphone")
    email_medecin = StringField("Email")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")