from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterMedicament(FlaskForm):
    nom_medic = StringField("Nom du médicament", validators=[DataRequired(), Length(min=2, max=100)])
    dosage_medic = StringField("Dosage", validators=[DataRequired(), Length(min=1, max=50)])
    forme_medic = StringField("Forme", validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField("Ajouter")

class FormWTFUpdateMedicament(FlaskForm):
    nom_medic = StringField("Nom du médicament", validators=[DataRequired(), Length(min=2, max=100)])
    dosage_medic = StringField("Dosage", validators=[DataRequired(), Length(min=1, max=50)])
    forme_medic = StringField("Forme", validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField("Mettre à jour")

class FormWTFDeleteMedicament(FlaskForm):
    nom_medic = StringField("Nom du médicament")
    dosage_medic = StringField("Dosage")
    forme_medic = StringField("Forme")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")