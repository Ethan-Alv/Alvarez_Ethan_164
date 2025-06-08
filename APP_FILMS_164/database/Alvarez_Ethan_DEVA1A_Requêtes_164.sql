-- Entre consultation et patient
SELECT consult.*, patient.* FROM t_consultation AS consult
LEFT JOIN t_consultation_patient AS consult_patient ON consult.id_consultation = consult_patient.fk_consultation
LEFT JOIN t_patient AS patient ON patient.id_patient = consult_patient.fk_patient;

SELECT consult.*, patient.* FROM t_consultation AS consult
RIGHT JOIN t_consultation_patient AS consult_patient ON consult.id_consultation = consult_patient.fk_consultation
RIGHT JOIN t_patient AS patient ON patient.id_patient = consult_patient.fk_patient;

SELECT consult.*, patient.* FROM t_consultation AS consult
INNER JOIN t_consultation_patient AS consult_patient ON consult.id_consultation = consult_patient.fk_consultation
INNER JOIN t_patient AS patient ON patient.id_patient = consult_patient.fk_patient;

-- Entre dossier et anamnèse
SELECT dossier.*, anamn.* FROM t_dossier AS dossier
LEFT JOIN t_dossier_anamnese AS dossier_anamn ON dossier.id_dossier = dossier_anamn.fk_dossier
LEFT JOIN t_anamnese AS anamn ON anamn.id_anamnese = dossier_anamn.fk_anamnese;

SELECT dossier.*, anamn.* FROM t_dossier AS dossier
RIGHT JOIN t_dossier_anamnese AS dossier_anamn ON dossier.id_dossier = dossier_anamn.fk_dossier
RIGHT JOIN t_anamnese AS anamn ON anamn.id_anamnese = dossier_anamn.fk_anamnese;

SELECT dossier.*, anamn.* FROM t_dossier AS dossier
INNER JOIN t_dossier_anamnese AS dossier_anamn ON dossier.id_dossier = dossier_anamn.fk_dossier
INNER JOIN t_anamnese AS anamn ON anamn.id_anamnese = dossier_anamn.fk_anamnese;

-- Entre dossier et examen
SELECT dossier.*, examen.* FROM t_dossier AS dossier
LEFT JOIN t_dossier_examen AS dossier_examen ON dossier.id_dossier = dossier_examen.fk_dossier
LEFT JOIN t_examen AS examen ON examen.id_examen = dossier_examen.fk_examen;

SELECT dossier.*, examen.* FROM t_dossier AS dossier
RIGHT JOIN t_dossier_examen AS dossier_examen ON dossier.id_dossier = dossier_examen.fk_dossier
RIGHT JOIN t_examen AS examen ON examen.id_examen = dossier_examen.fk_examen;

SELECT dossier.*, examen.* FROM t_dossier AS dossier
INNER JOIN t_dossier_examen AS dossier_examen ON dossier.id_dossier = dossier_examen.fk_dossier
INNER JOIN t_examen	 AS examen ON examen.id_examen = dossier_examen.fk_examen;

-- Entre dossier et patient
SELECT dossier.*, patient.* FROM t_dossier AS dossier
LEFT JOIN t_dossier_patient AS dossier_patient ON dossier.id_dossier = dossier_patient.fk_dossier
LEFT JOIN t_patient AS patient ON patient.id_patient = dossier_patient.fk_patient;

SELECT dossier.*, patient.* FROM t_dossier AS dossier
RIGHT JOIN t_dossier_patient AS dossier_patient ON dossier.id_dossier = dossier_patient.fk_dossier
RIGHT JOIN t_patient AS patient ON patient.id_patient = dossier_patient.fk_patient;

SELECT dossier.*, patient.* FROM t_dossier AS dossier
INNER JOIN t_dossier_patient AS dossier_patient ON dossier.id_dossier = dossier_patient.fk_dossier
INNER JOIN t_patient	 AS patient ON patient.id_patient = dossier_patient.fk_patient;

-- Entre dossier et prescription
SELECT dossier.*, prescription.* FROM t_dossier AS dossier
LEFT JOIN t_dossier_prescription AS dossier_prescription ON dossier.id_dossier = dossier_prescription.fk_dossier
LEFT JOIN t_prescription AS prescription ON prescription.id_prescription = dossier_prescription.fk_prescription;

SELECT dossier.*, prescription.* FROM t_dossier AS dossier
RIGHT JOIN t_dossier_prescription AS dossier_prescription ON dossier.id_dossier = dossier_prescription.fk_dossier
RIGHT JOIN t_prescription AS prescription ON prescription.id_prescription = dossier_prescription.fk_prescription;

SELECT dossier.*, prescription.* FROM t_dossier AS dossier
INNER JOIN t_dossier_prescription AS dossier_prescription ON dossier.id_dossier = dossier_prescription.fk_dossier
INNER JOIN t_prescription	 AS prescription ON prescription.id_prescription = dossier_prescription.fk_prescription;

-- Entre dossier et rapport
SELECT dossier.*, rapport.* FROM t_dossier AS dossier
LEFT JOIN t_dossier_rapport AS dossier_rapport ON dossier.id_dossier = dossier_rapport.fk_dossier
LEFT JOIN t_rapport AS rapport ON rapport.id_rapport = dossier_rapport.fk_rapport;

SELECT dossier.*, rapport.* FROM t_dossier AS dossier
RIGHT JOIN t_dossier_rapport AS dossier_rapport ON dossier.id_dossier = dossier_rapport.fk_dossier
RIGHT JOIN t_rapport AS rapport ON rapport.id_rapport = dossier_rapport.fk_rapport;

SELECT dossier.*, rapport.* FROM t_dossier AS dossier
INNER JOIN t_dossier_rapport AS dossier_rapport ON dossier.id_dossier = dossier_rapport.fk_dossier
INNER JOIN t_rapport	 AS rapport ON rapport.id_rapport = dossier_rapport.fk_rapport;

-- Entre dossier et signe vital
SELECT dossier.*, signe_vital.* FROM t_dossier AS dossier
LEFT JOIN t_dossier_signe_vital AS dossier_signe_vital ON dossier.id_dossier = dossier_signe_vital.fk_dossier
LEFT JOIN t_signe_vital AS signe_vital ON signe_vital.id_signe_vital = dossier_signe_vital.fk_signe_vital;

SELECT dossier.*, signe_vital.* FROM t_dossier AS dossier
RIGHT JOIN t_dossier_signe_vital AS dossier_signe_vital ON dossier.id_dossier = dossier_signe_vital.fk_dossier
RIGHT JOIN t_signe_vital AS signe_vital ON signe_vital.id_signe_vital = dossier_signe_vital.fk_signe_vital;

SELECT dossier.*, signe_vital.* FROM t_dossier AS dossier
INNER JOIN t_dossier_signe_vital AS dossier_signe_vital ON dossier.id_dossier = dossier_signe_vital.fk_dossier
INNER JOIN t_signe_vital	 AS signe_vital ON signe_vital.id_signe_vital = dossier_signe_vital.fk_signe_vital;

-- Entre prescription et medecin
SELECT prescription.*, medecin.* FROM t_prescription AS prescription
LEFT JOIN t_prescription_medecin AS prescription_medecin ON prescription.id_prescription = prescription_medecin.fk_prescription
LEFT JOIN t_medecin AS medecin ON medecin.id_medecin = prescription_medecin.fk_medecin;

SELECT prescription.*, medecin.* FROM t_prescription AS prescription
RIGHT JOIN t_prescription_medecin AS prescription_medecin ON prescription.id_prescription = prescription_medecin.fk_prescription
RIGHT JOIN t_medecin AS medecin ON medecin.id_medecin = prescription_medecin.fk_medecin;

SELECT prescription.*, medecin.* FROM t_prescription AS prescription
INNER JOIN t_prescription_medecin AS prescription_medecin ON prescription.id_prescription = prescription_medecin.fk_prescription
INNER JOIN t_medecin	 AS medecin ON medecin.id_medecin = prescription_medecin.fk_medecin;

-- Entre prescription et medicament
SELECT prescription.*, medicament.* FROM t_prescription AS prescription
LEFT JOIN t_prescription_medicament AS prescription_medicament ON prescription.id_prescription = prescription_medicament.fk_prescription
LEFT JOIN t_medicament AS medicament ON medicament.id_medicament = prescription_medicament.fk_medicament;

SELECT prescription.*, medicament.* FROM t_prescription AS prescription
RIGHT JOIN t_prescription_medicament AS prescription_medicament ON prescription.id_prescription = prescription_medicament.fk_prescription
RIGHT JOIN t_medicament AS medicament ON medicament.id_medicament = prescription_medicament.fk_medicament;

SELECT prescription.*, medicament.* FROM t_prescription AS prescription
INNER JOIN t_prescription_medicament AS prescription_medicament ON prescription.id_prescription = prescription_medicament.fk_prescription
INNER JOIN t_medicament	 AS medicament ON medicament.id_medicament = prescription_medicament.fk_medicament;