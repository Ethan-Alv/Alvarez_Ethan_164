from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterPrescription(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    medecin_select = SelectField("Médecin", choices=[], validators=[DataRequired()])
    medicament_select = SelectField("Médicament", choices=[], validators=[DataRequired()])
    posologie_prescr = StringField("Posologie", validators=[DataRequired(), Length(min=1, max=100)])
    duree_traitement_prescr = StringField("Durée du traitement", validators=[DataRequired(), Length(min=1, max=50)])
    debut_prescr = DateField("Début", validators=[DataRequired()])
    fin_prescr = DateField("Fin", validators=[DataRequired()])
    submit = SubmitField("Ajouter")

class FormWTFUpdatePrescription(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    posologie_prescr = StringField("Posologie", validators=[DataRequired(), Length(min=1, max=100)])
    duree_traitement_prescr = StringField("Durée du traitement", validators=[DataRequired(), Length(min=1, max=50)])
    debut_prescr = DateField("Début", validators=[DataRequired()])
    fin_prescr = DateField("Fin", validators=[DataRequired()])
    medecin_select = SelectField("Médecin", choices=[], validators=[DataRequired()])
    medicament_select = SelectField("Médicament", choices=[], validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")

class FormWTFDeletePrescription(FlaskForm):
    patient_select = SelectField("Patient", choices=[], validators=[DataRequired()])
    medecin = StringField("Médecin")
    medicament = StringField("Médicament")
    posologie_prescr = StringField("Posologie")
    duree_traitement_prescr = StringField("Durée du traitement")
    debut_prescr = StringField("Début")
    fin_prescr = StringField("Fin")
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")