"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp
from datetime import datetime

def get_years(start=1900, end=None):
    if end is None:
        end = datetime.now().year + 1
    return [(str(y), str(y)) for y in range(end, start - 1, -1)]

def get_months():
    return [(str(m).zfill(2), str(m).zfill(2)) for m in range(1, 13)]

def get_days():
    return [(str(d).zfill(2), str(d).zfill(2)) for d in range(1, 32)]

class FormWTFAjouterGenres(FlaskForm):
    nom_genre_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ouverture_jour = SelectField("Jour d'ouverture", choices=get_days())
    ouverture_mois = SelectField("Mois d'ouverture", choices=get_months())
    ouverture_annee = SelectField("Année d'ouverture", choices=get_years(1900))
    cloture_jour = SelectField("Jour de clôture", choices=[('', '')] + get_days(), default='')
    cloture_mois = SelectField("Mois de clôture", choices=[('', '')] + get_months(), default='')
    cloture_annee = SelectField("Année de clôture", choices=[('', '')] + get_years(1900), default='')
    statut_dossier = SelectField("Statut du dossier", choices=[('Actif', 'Actif'), ('Clôturé', 'Clôturé'), ('En attente', 'En attente')])
    patient = SelectField("Patient", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Ajouter")

class FormWTFUpdateGenre(FlaskForm):
    ouverture_jour = SelectField("Jour d'ouverture", choices=get_days())
    ouverture_mois = SelectField("Mois d'ouverture", choices=get_months())
    ouverture_annee = SelectField("Année d'ouverture", choices=get_years(1900))
    cloture_jour = SelectField("Jour de clôture", choices=[('', '')] + get_days(), default='')
    cloture_mois = SelectField("Mois de clôture", choices=[('', '')] + get_months(), default='')
    cloture_annee = SelectField("Année de clôture", choices=[('', '')] + get_years(1900), default='')
    statut_dossier = SelectField("Statut du dossier", choices=[('Actif', 'Actif'), ('Clôturé', 'Clôturé'), ('En attente', 'En attente')])
    patient = SelectField("Patient", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")


class FormWTFDeleteDossier(FlaskForm):
    ouverture = StringField("Date d'ouverture")
    cloture = StringField("Date de clôture")
    statut = StringField("Statut du dossier")
    patient = StringField("Patient")
    submit_btn_del = SubmitField("Effacer dossier")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
