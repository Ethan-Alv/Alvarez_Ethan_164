from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterRapport(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])  # Format: "id_patient", "Nom Prénom"
    date_rapport = DateField("Date du rapport", validators=[DataRequired()])
    type_rapport = StringField("Type de rapport", validators=[DataRequired(), Length(min=2, max=50)])
    texte_rapport = TextAreaField("Texte du rapport", validators=[DataRequired(), Length(min=2, max=1000)])
    submit = SubmitField("Ajouter")

class FormWTFUpdateRapport(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    date_rapport = DateField("Date du rapport", validators=[DataRequired()])
    type_rapport = StringField("Type de rapport", validators=[DataRequired(), Length(min=2, max=50)])
    texte_rapport = TextAreaField("Texte du rapport", validators=[DataRequired(), Length(min=2, max=1000)])
    submit = SubmitField("Mettre à jour")

class FormWTFDeleteRapport(FlaskForm):
    nom_patient = StringField("Nom du patient")
    prenom_patient = StringField("Prénom du patient")
    type_rapport = StringField("Type de rapport")
    texte_rapport = TextAreaField("Texte du rapport")
    date_rapport = StringField("Date du rapport")
    dossier = StringField("Dossier")  # Ajouté pour éviter l'AttributeError
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")