-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 08 juin 2025 à 22:53
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `alvarez_ethan_deva_1a`
--
DROP DATABASE IF EXISTS `alvarez_ethan_deva_1a`;
CREATE DATABASE IF NOT EXISTS `alvarez_ethan_deva_1a` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `alvarez_ethan_deva_1a`;

-- --------------------------------------------------------

--
-- Structure de la table `t_anamnese`
--

CREATE TABLE IF NOT EXISTS `t_anamnese` (
  `id_anamnese` int(10) NOT NULL AUTO_INCREMENT,
  `histoire_de_vie_anamn` text DEFAULT NULL,
  `antecedent_medicaux_anamn` text DEFAULT NULL,
  `probleme_anamn` text DEFAULT NULL,
  `allergies_anamn` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_anamnese`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_anamnese`
--

INSERT INTO `t_anamnese` (`id_anamnese`, `histoire_de_vie_anamn`, `antecedent_medicaux_anamn`, `probleme_anamn`, `allergies_anamn`) VALUES
(1, 'Née à Genève, mariée, 2 enfants, travaille comme comptable', 'Appendicectomie à 25 ans', 'Migraines occasionnelles', 'Allergie au pollen'),
(2, 'Originaire de Lausanne, divorcé, 1 enfant, ingénieur', 'Fracture du bras gauche il y a 5 ans', 'Douleurs lombaires chroniques', 'Aucune allergie connue'),
(3, 'Immigrée d\'Allemagne il y a 15 ans, mariée, pas d\'enfants', 'Hypertension artérielle depuis 3 ans', 'Insomnies fréquentes', 'Allergie à la pénicilline'),
(4, 'Né à Berne, célibataire, entrepreneur', 'Asthme depuis l\'adolescence', 'Stress professionnel', 'Allergie aux arachides'),
(5, 'Originaire de Fribourg, mariée, 1 enfant, enseignante', 'Thyroïdectomie il y a 2 ans', 'Fatigue chronique', 'Intolérance au lactose'),
(6, 'Né à Bâle, marié, 3 enfants, médecin', 'Diabète de type 2 diagnostiqué récemment', 'Troubles du sommeil', 'Allergie au latex'),
(7, 'Originaire de Saint-Gall, célibataire, étudiante en droit', 'Myopie sévère, opération des yeux il y a 1 an', 'Anxiété liée aux examens', 'Allergie aux fruits de mer'),
(8, 'Né à Lucerne, veuf, 2 enfants, retraité', 'Pontage coronarien il y a 3 ans', 'Arthrose des hanches', 'Allergie à l\'iode'),
(9, 'Originaire de Winterthour, mariée, pas d\'enfants, architecte', 'Endométriose diagnostiquée à 25 ans', 'Douleurs pelviennes chroniques', 'Aucune allergie connue'),
(10, 'Né au Tessin, divorcé, 1 enfant, chef cuisinier', 'Ulcère gastrique traité il y a 5 ans', 'Reflux gastro-œsophagien', 'Allergie aux sulfites'),
(11, 'Originaire de Bienne, mariée, 2 enfants, infirmière', 'Dépression traitée depuis 1 an', 'Troubles anxieux', 'Allergie aux noix'),
(12, 'Né à Thoune, célibataire, informaticien', 'Appendicectomie à 18 ans', 'Maux de dos récurrents', 'Allergie au nickel'),
(13, 'Originaire de Coire, divorcée, 1 enfant, avocate', 'Cancer du sein en rémission depuis 2 ans', 'Lymphœdème du bras gauche', 'Allergie au kiwi'),
(14, 'Né à Neuchâtel, marié, 3 enfants, professeur', 'Hypertension, hypercholestérolémie', 'Acouphènes', 'Allergie aux acariens'),
(15, 'Originaire de Sion, veuve, 2 enfants, pharmacienne', 'Ostéoporose diagnostiquée récemment', 'Douleurs articulaires', 'Allergie au gluten'),
(16, 'Retraité, ancien mécanicien, célibataire', 'Prothèse de hanche gauche (2019)', 'Douleurs articulaires résiduelles', NULL),
(17, 'Étudiant en architecture, végétarien', NULL, 'Migraines ophtalmiques', 'Allergie aux sulfites (vin)'),
(18, 'Mère de famille, travaille dans la restauration', 'Hypertension traitée', NULL, 'Intolérance au lactose'),
(19, 'Sportif professionnel, vit à la montagne', 'Fracture de la clavicule (2020)', 'Essoufflement à l\'effort', 'Aucune allergie connue'),
(20, NULL, 'Diabète gestationnel (2022)', 'Fatigue persistante', 'Allergie aux anti-inflammatoires non stéroïdiens');

-- --------------------------------------------------------

--
-- Structure de la table `t_consultation`
--

CREATE TABLE IF NOT EXISTS `t_consultation` (
  `id_consultation` int(10) NOT NULL AUTO_INCREMENT,
  `date_consult` date DEFAULT NULL,
  `motif_consult` varchar(255) DEFAULT NULL,
  `diagnostic_consult` varchar(255) DEFAULT NULL,
  `notes_consult` text DEFAULT NULL,
  PRIMARY KEY (`id_consultation`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_consultation`
--

INSERT INTO `t_consultation` (`id_consultation`, `date_consult`, `motif_consult`, `diagnostic_consult`, `notes_consult`) VALUES
(1, '2025-04-15', 'Douleurs thoraciques', 'Angor stable', 'ECG normal, tension artérielle 130/85 mmHg. Suivi cardiologique recommandé.'),
(2, '2025-04-16', 'Suivi diabète', 'Diabète de type 2 équilibré', 'HbA1c à 6.8%. Adaptation du régime alimentaire discutée.'),
(3, '2025-04-17', 'Toux persistante', 'Bronchite aiguë', 'Rx thorax normal. Prescription d\'antitussifs et repos.'),
(4, '2025-04-18', 'Contrôle post-opératoire', NULL, 'Cicatrisation satisfaisante. Retrait des agrafes prévu dans 7 jours.'),
(5, '2025-04-19', 'Vertiges', 'Hypotension orthostatique', 'Vérification des traitements antihypertenseurs. Conseils hydratation.'),
(6, '2025-04-20', 'Douleurs abdominales', 'Gastrite légère', 'Endoscopie digestive planifiée. Prescription d\'IPP pour 4 semaines.'),
(7, '2025-04-21', 'Suivi grossesse', 'Grossesse 32 SA', 'Échographie fœtale normale. Compléments en fer maintenus.'),
(8, '2025-04-22', 'Fatigue chronique', 'Anémie ferriprive', 'Ferritine basse (12 µg/L). Supplémentation en fer prescrite.'),
(9, '2025-04-23', 'Éruption cutanée', 'Allergie médicamenteuse', 'Suspicion d\'allergie à la pénicilline. Tests cutanés demandés.'),
(10, '2025-04-24', 'Consultation psychiatrique', 'Trouble anxieux généralisé', 'Thérapie cognitivo-comportementale initiée.'),
(11, '2025-04-25', 'Suivi oncologique', 'Cancer du sein en rémission', 'Pas de signe de récidive à l\'IRM. Contrôle dans 6 mois.'),
(12, '2025-04-26', 'Douleurs articulaires', 'Arthrose du genou', 'Infiltration intra-articulaire réalisée. Kinésithérapie prescrite.'),
(13, '2025-04-27', 'Céphalées récurrentes', 'Migraine sans aura', 'Prescription de triptans. Journal des crises demandé.'),
(14, '2025-04-28', 'Dyspnée à l\'effort', 'Asthme d\'effort', 'Test de provocation positif. Adaptation du traitement de fond.'),
(15, '2025-04-29', 'Contrôle tensionnel', NULL, 'Tension normalisée sous traitement (125/80 mmHg). Pas de modification nécessaire.'),
(16, '2025-04-30', 'Bilan annuel', NULL, 'Aucun symptôme rapporté. Examen clinique normal.'),
(17, '2025-05-01', 'Douleurs musculaires', 'Tension musculaire', NULL),
(18, '2025-05-02', NULL, 'Reflux gastro-œsophagien', 'Conseils diététiques donnés. IPP prescrits.'),
(19, '2025-05-03', 'Vertiges positionnels', 'Vertige paroxystique bénin', 'Manœuvre d\'Epley réalisée avec succès'),
(20, NULL, 'Suivi hypertension', 'Hypertension contrôlée', 'Tension à 130/85 mmHg. Pas de modification du traitement.');

-- --------------------------------------------------------

--
-- Structure de la table `t_consultation_patient`
--

CREATE TABLE IF NOT EXISTS `t_consultation_patient` (
  `id_consultation_patient` int(10) NOT NULL AUTO_INCREMENT,
  `fk_consultation` int(10) NOT NULL,
  `fk_patient` int(10) NOT NULL,
  PRIMARY KEY (`id_consultation_patient`),
  KEY `fk_consultation` (`fk_consultation`),
  KEY `fk_patient` (`fk_patient`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_consultation_patient`
--

INSERT INTO `t_consultation_patient` (`id_consultation_patient`, `fk_consultation`, `fk_patient`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier`
--

CREATE TABLE IF NOT EXISTS `t_dossier` (
  `id_dossier` int(10) NOT NULL AUTO_INCREMENT,
  `ouverture_dossier` date DEFAULT NULL,
  `cloture_dossier` date DEFAULT NULL,
  `statut_dossier` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_dossier`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier`
--

INSERT INTO `t_dossier` (`id_dossier`, `ouverture_dossier`, `cloture_dossier`, `statut_dossier`) VALUES
(1, '2025-01-01', '2025-03-03', 'Actif'),
(2, '2024-11-03', '2025-02-28', 'Clôturé'),
(3, '2025-02-20', NULL, 'Actif'),
(4, '2024-12-05', '2025-01-10', 'Clôturé'),
(5, '2025-03-01', NULL, 'Actif'),
(6, '2024-10-18', '2025-03-15', 'Clôturé'),
(7, '2025-01-30', NULL, 'Actif'),
(8, '2024-09-22', '2025-02-05', 'Clôturé'),
(9, '2025-02-14', NULL, 'Actif'),
(10, '2024-11-29', NULL, 'En attente'),
(11, '2025-03-10', NULL, 'Actif'),
(12, '2024-12-20', '2025-03-18', 'Clôturé'),
(13, '2025-01-05', NULL, 'Actif'),
(14, '2024-10-30', '2025-01-25', 'Clôturé'),
(15, '2025-02-28', NULL, 'En attente'),
(16, '2025-01-10', '2025-04-20', 'Clôturé'),
(17, '2024-11-15', NULL, 'En cours'),
(18, '2025-02-01', '2025-03-30', NULL),
(19, '2024-09-22', NULL, 'Suspendu'),
(20, '2025-03-05', '2025-04-18', 'Archivé');

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_anamnese`
--

CREATE TABLE IF NOT EXISTS `t_dossier_anamnese` (
  `id_dossier_anamnese` int(10) NOT NULL AUTO_INCREMENT,
  `fk_dossier` int(10) NOT NULL,
  `fk_anamnese` int(10) NOT NULL,
  PRIMARY KEY (`id_dossier_anamnese`),
  KEY `fk_anamnese` (`fk_anamnese`),
  KEY `fk_dossier` (`fk_dossier`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier_anamnese`
--

INSERT INTO `t_dossier_anamnese` (`id_dossier_anamnese`, `fk_dossier`, `fk_anamnese`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_examen`
--

CREATE TABLE IF NOT EXISTS `t_dossier_examen` (
  `id_dossier_examen` int(10) NOT NULL AUTO_INCREMENT,
  `fk_dossier` int(10) NOT NULL,
  `fk_examen` int(10) NOT NULL,
  PRIMARY KEY (`id_dossier_examen`),
  KEY `fk_dossier` (`fk_dossier`),
  KEY `fk_examen` (`fk_examen`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier_examen`
--

INSERT INTO `t_dossier_examen` (`id_dossier_examen`, `fk_dossier`, `fk_examen`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_patient`
--

CREATE TABLE IF NOT EXISTS `t_dossier_patient` (
  `id_dossier_patient` int(10) NOT NULL AUTO_INCREMENT,
  `fk_dossier` int(10) NOT NULL,
  `fk_patient` int(10) NOT NULL,
  PRIMARY KEY (`id_dossier_patient`),
  KEY `fk_dossier` (`fk_dossier`),
  KEY `fk_patient` (`fk_patient`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier_patient`
--

INSERT INTO `t_dossier_patient` (`id_dossier_patient`, `fk_dossier`, `fk_patient`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_prescription`
--

CREATE TABLE IF NOT EXISTS `t_dossier_prescription` (
  `id_dossier_prescription` int(10) NOT NULL AUTO_INCREMENT,
  `fk_dossier` int(10) NOT NULL,
  `fk_prescription` int(10) NOT NULL,
  PRIMARY KEY (`id_dossier_prescription`),
  KEY `fk_dossier` (`fk_dossier`),
  KEY `fk_prescription` (`fk_prescription`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier_prescription`
--

INSERT INTO `t_dossier_prescription` (`id_dossier_prescription`, `fk_dossier`, `fk_prescription`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_rapport`
--

CREATE TABLE IF NOT EXISTS `t_dossier_rapport` (
  `id_dossier_rapport` int(10) NOT NULL AUTO_INCREMENT,
  `fk_dossier` int(10) NOT NULL,
  `fk_rapport` int(10) NOT NULL,
  PRIMARY KEY (`id_dossier_rapport`),
  KEY `fk_dossier` (`fk_dossier`),
  KEY `fk_rapport` (`fk_rapport`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier_rapport`
--

INSERT INTO `t_dossier_rapport` (`id_dossier_rapport`, `fk_dossier`, `fk_rapport`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(31, 16, 16),
(32, 17, 17),
(33, 18, 18),
(34, 19, 19),
(35, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_signe_vital`
--

CREATE TABLE IF NOT EXISTS `t_dossier_signe_vital` (
  `id_dossier_signe_vital` int(10) NOT NULL AUTO_INCREMENT,
  `fk_dossier` int(10) NOT NULL,
  `fk_signe_vital` int(10) NOT NULL,
  PRIMARY KEY (`id_dossier_signe_vital`),
  KEY `fk_dossier` (`fk_dossier`),
  KEY `fk_signe_vital` (`fk_signe_vital`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_dossier_signe_vital`
--

INSERT INTO `t_dossier_signe_vital` (`id_dossier_signe_vital`, `fk_dossier`, `fk_signe_vital`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_examen`
--

CREATE TABLE IF NOT EXISTS `t_examen` (
  `id_examen` int(10) NOT NULL AUTO_INCREMENT,
  `type_examen` varchar(100) DEFAULT NULL,
  `date_examen` date DEFAULT NULL,
  `resultats_examen` text DEFAULT NULL,
  PRIMARY KEY (`id_examen`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_examen`
--

INSERT INTO `t_examen` (`id_examen`, `type_examen`, `date_examen`, `resultats_examen`) VALUES
(1, 'Analyses de sang', '2025-02-18', 'Taux de cholestérol légèrement élevé, autres paramètres normaux'),
(2, 'IRM lombaire', '2025-03-17', 'Hernie discale L4-L5 confirmée, compression nerveuse modérée'),
(3, 'Mesure de la tension artérielle', '2025-03-16', 'Tension artérielle: 145/90 mmHg, hypertension légère'),
(4, 'Spirométrie', '2025-03-15', 'Capacité pulmonaire réduite de 15%, compatible avec l\'asthme'),
(5, 'Dosage hormones thyroïdiennes', '2025-03-14', 'TSH élevée, T4 basse, hypothyroïdie confirmée'),
(6, 'Test HbA1c', '2025-03-13', 'HbA1c à 7.2%, contrôle glycémique à améliorer'),
(7, 'Audiométrie', '2025-03-12', 'Perte auditive légère dans les hautes fréquences'),
(8, 'Radiographie thoracique', '2025-03-11', 'Pas d\'anomalies significatives détectées'),
(9, 'Échographie pelvienne', '2025-03-10', 'Kyste ovarien de 3 cm détecté sur l\'ovaire droit'),
(10, 'Endoscopie digestive haute', '2025-03-09', 'Gastrite légère, pas d\'ulcère visible'),
(11, 'Électrocardiogramme (ECG)', '2025-03-08', 'Rythme sinusal normal, pas d\'anomalies de conduction'),
(12, 'Scanner lombaire', '2025-03-07', 'Spondylolisthésis L5-S1 de grade I'),
(13, 'Mammographie', '2025-03-06', 'Tissu mammaire dense, pas de masses suspectes'),
(14, 'Test d\'effort cardiaque', '2025-03-05', 'Capacité d\'effort normale, pas de signes d\'ischémie'),
(15, 'Densitométrie osseuse', '2025-03-04', 'T-score -2.1, ostéopénie modérée'),
(16, 'Échographie abdominale', '2025-04-15', 'Foie normal, vésicule biliaire lithiasique'),
(17, 'IRM cérébrale', '2025-04-16', NULL),
(18, 'Test d\'effort', NULL, 'Capacité cardiaque réduite de 20%'),
(19, 'Dosage TSH', '2025-04-18', 'Hypothyroïdie compensée'),
(20, NULL, '2025-04-19', 'Densité osseuse T-score -1.8'),
(22, 'Sauvetage mort', '2025-02-12', 'Il est mort Zeubi');

-- --------------------------------------------------------

--
-- Structure de la table `t_medecin`
--

CREATE TABLE IF NOT EXISTS `t_medecin` (
  `id_medecin` int(10) NOT NULL AUTO_INCREMENT,
  `nom_medecin` varchar(100) DEFAULT NULL,
  `prenom_medecin` varchar(100) DEFAULT NULL,
  `telephone_medecin` varchar(20) DEFAULT NULL,
  `email_medecin` text NOT NULL,
  PRIMARY KEY (`id_medecin`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_medecin`
--

INSERT INTO `t_medecin` (`id_medecin`, `nom_medecin`, `prenom_medecin`, `telephone_medecin`, `email_medecin`) VALUES
(1, 'Dupont', 'Marie', '0223456789', 'Dupont.Marie@gmail.com'),
(2, 'Martin', 'Jean', '0334567890', 'Martin.Jean@gmail.com'),
(3, 'Bernard', 'Sophie', '0445678901', 'Bernard.Sophie@gmail.com'),
(4, 'Dubois', 'Pierre', '0556789012', 'Dubois.Pierre@gmail.com'),
(5, 'Moreau', 'Claire', '0667890123', 'Moreau.Claire@gmail.com'),
(6, 'Laurent', 'Thomas', '0778901234', 'Laurent.Thomas@gmail.com'),
(7, 'Leroy', 'Anne', '0889012345', 'Leroy.Anne@gmail.com'),
(8, 'Roux', 'Philippe', '0990123456', 'Roux.Philippe@gmail.com'),
(9, 'Petit', 'Isabelle', '0112345678', 'Petit.Isabelle@gmail.com'),
(10, 'Simon', 'François', '0123456789', 'Simon.Francois@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `t_medicament`
--

CREATE TABLE IF NOT EXISTS `t_medicament` (
  `id_medicament` int(10) NOT NULL AUTO_INCREMENT,
  `nom_medic` varchar(100) DEFAULT NULL,
  `dosage_medic` text DEFAULT NULL,
  `forme_medic` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_medicament`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_medicament`
--

INSERT INTO `t_medicament` (`id_medicament`, `nom_medic`, `dosage_medic`, `forme_medic`) VALUES
(1, 'Paracétamol', '500 mg', 'Comprimé'),
(2, 'Ibuprofène', '200 mg', 'Gélule'),
(3, 'Insuline glargine', '100 U/ml', 'Injection'),
(4, 'Zolpidem', '10 mg', 'Comprimé'),
(5, 'Amoxicilline', '500 mg', 'Capsule'),
(6, 'Fentanyl', '25 µg/h', 'Patch'),
(7, 'Fluticasone', '50 µg/dose', 'Spray nasal'),
(8, 'Vitamine C', '1 g', 'Comprimé effervescent'),
(9, 'Oméprazole', '20 mg', 'Sachet à diluer'),
(10, 'Diclofénac', '50 mg', 'Comprimé'),
(11, 'Suppositoire glycériné', '2 g', 'Suppositoire'),
(12, 'Sirop de guaifenesin', '100 mg/5 ml', 'Solution orale'),
(13, 'Loratadine', '10 mg', 'Comprimé à sucer'),
(14, 'Clotrimazole', '1%', 'Crème topique'),
(15, 'Fer ferreux', '80 mg', 'Capsule'),
(16, 'Levothyroxine', '75 µg', 'Comprimé'),
(17, 'Ibuprofène', NULL, 'Gélule'),
(18, 'Insuline glargine', '100 U/ml', NULL),
(19, 'Paracétamol', '500 mg', 'Comprimé effervescent'),
(20, NULL, '20 mg', 'Capsule');

-- --------------------------------------------------------

--
-- Structure de la table `t_patient`
--

CREATE TABLE IF NOT EXISTS `t_patient` (
  `id_patient` int(10) NOT NULL AUTO_INCREMENT,
  `nom_patient` varchar(255) DEFAULT NULL,
  `prenom_patient` varchar(255) DEFAULT NULL,
  `date_naissance_pers` date DEFAULT NULL,
  `localite_patient` varchar(100) DEFAULT NULL,
  `code_postal_patient` int(10) DEFAULT NULL,
  `nom_rue_patient` varchar(100) DEFAULT NULL,
  `numero_rue_patient` int(10) DEFAULT NULL,
  `telephone_patient` varchar(20) DEFAULT NULL,
  `email_patient` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_patient`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_patient`
--

INSERT INTO `t_patient` (`id_patient`, `nom_patient`, `prenom_patient`, `date_naissance_pers`, `localite_patient`, `code_postal_patient`, `nom_rue_patient`, `numero_rue_patient`, `telephone_patient`, `email_patient`) VALUES
(1, 'Dupont', 'Marie', '1985-03-15', 'Genève', 1201, 'Rue du Rhône', 12, '0223456789', 'marie.dupont@email.ch'),
(2, 'Martin', 'Jean', '1990-07-22', 'Lausanne', 1003, 'Avenue de la Gare', 45, '0219876543', 'jean.martin@email.ch'),
(3, 'Dubois', 'Sophie', '1978-11-10', 'Zurich', 8001, 'Bahnhofstrasse', 78, '0441234567', 'sophie.dubois@email.ch'),
(4, 'Leroy', 'Pierre', '1982-09-05', 'Berne', 3000, 'Kramgasse', 56, '0317654321', 'pierre.leroy@email.ch'),
(5, 'Moreau', 'Claire', '1995-12-30', 'Fribourg', 1700, 'Rue de Lausanne', 34, '0265432198', 'claire.moreau@email.ch'),
(6, 'Schmid', 'Thomas', '1988-06-18', 'Bâle', 4051, 'Freiestrasse', 23, '0612345678', 'thomas.schmid@email.ch'),
(7, 'Müller', 'Anna', '1992-04-07', 'Saint-Gall', 9000, 'Marktplatz', 9, '0712345678', 'anna.mueller@email.ch'),
(8, 'Keller', 'Marc', '1975-09-25', 'Lucerne', 6002, 'Pilatusstrasse', 67, '0412345678', 'marc.keller@email.ch'),
(9, 'Weber', 'Laura', '1998-02-14', 'Winterthour', 8400, 'Marktgasse', 15, '0522345678', 'laura.weber@email.ch'),
(10, 'Fischer', 'Daniel', '1980-11-03', 'Lugano', 6900, 'Via Nassa', 29, '0912345678', 'daniel.fischer@email.ch'),
(11, 'Brunner', 'Céline', '1993-08-20', 'Bienne', 2502, 'Rue Centrale', 41, '0322345678', 'celine.brunner@email.ch'),
(12, 'Meier', 'Nicolas', '1987-01-12', 'Thoune', 3600, 'Hauptgasse', 18, '0332345678', 'nicolas.meier@email.ch'),
(13, 'Schneider', 'Isabelle', '1976-05-29', 'Coire', 7000, 'Bahnhofstrasse', 33, '0812345678', 'isabelle.schneider@email.ch'),
(14, 'Steiner', 'Philippe', '1991-10-08', 'Neuchâtel', 2000, 'Rue du Seyon', 7, '0322345679', 'philippe.steiner@email.ch'),
(15, 'Gerber', 'Monique', '1984-07-17', 'Sion', 1950, 'Avenue de la Gare', 50, '0272345678', 'monique.gerber@email.ch'),
(16, 'Bianchi', 'Luca', '1992-09-14', 'Lugano', 6900, 'Via Nassa', 12, NULL, 'luca.bianchi@email.ch'),
(17, 'Roux', 'Émilie', NULL, 'Genève', 1201, 'Rue de la Corraterie', 8, '0228765432', 'emilie.roux@email.ch'),
(18, 'Meier', 'Felix', '1988-04-25', 'Zurich', 8001, NULL, 45, '0449876543', 'felix.meier@email.ch'),
(19, 'Fontana', 'Alessia', '2001-11-03', 'Lausanne', 0, 'Avenue de la Gare', 22, '0212345678', NULL),
(20, 'Koller', 'Hans', '1975-06-18', NULL, 4001, 'Rheingasse', 17, '0613456789', 'hans.koller@email.ch'),
(23, 'Alvarez', 'Ethan', '2005-02-12', 'Le Pâquier-Montbarry', 1661, 'Chemin de La Fin', 5, '078 789 03 93', 'ethan.alvarez@hotmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `t_prescription`
--

CREATE TABLE IF NOT EXISTS `t_prescription` (
  `id_prescription` int(10) NOT NULL AUTO_INCREMENT,
  `posologie_prescr` varchar(255) DEFAULT NULL,
  `duree_traitement_prescr` varchar(255) DEFAULT NULL,
  `debut_prescr` date DEFAULT NULL,
  `fin_prescr` date DEFAULT NULL,
  PRIMARY KEY (`id_prescription`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_prescription`
--

INSERT INTO `t_prescription` (`id_prescription`, `posologie_prescr`, `duree_traitement_prescr`, `debut_prescr`, `fin_prescr`) VALUES
(1, '1 comprimé 3 fois par jour', '14 jours', '2025-03-19', '2025-04-02'),
(2, '2 gélules le matin', '30 jours', '2025-03-20', '2025-04-19'),
(3, '1 injection par semaine', '8 semaines', '2025-03-21', '2025-05-16'),
(4, '1 comprimé le soir au coucher', '60 jours', '2025-03-22', '2025-05-21'),
(5, '1 cuillère à café 2 fois par jour', '10 jours', '2025-03-23', '2025-04-02'),
(6, '1 patch toutes les 24 heures', '28 jours', '2025-03-24', '2025-04-21'),
(7, '2 pulvérisations dans chaque narine matin et soir', '7 jours', '2025-03-25', '2025-04-01'),
(8, '1 comprimé effervescent par jour', '90 jours', '2025-03-26', '2025-06-24'),
(9, '1 sachet à diluer dans un verre d\'eau 3 fois par jour', '5 jours', '2025-03-27', '2025-04-01'),
(10, '1 comprimé matin et soir', '21 jours', '2025-03-28', '2025-04-18'),
(11, '1 suppositoire au coucher', '7 jours', '2025-03-29', '2025-04-05'),
(12, '1 cuillère à soupe 3 fois par jour avant les repas', '14 jours', '2025-03-30', '2025-04-13'),
(13, '1 comprimé à sucer toutes les 4 heures si besoin', '10 jours', '2025-03-31', '2025-04-10'),
(14, '1 application locale 2 fois par jour', '21 jours', '2025-04-01', '2025-04-22'),
(15, '2 gélules matin et soir pendant les repas', '30 jours', '2025-04-02', '2025-05-02'),
(16, '1 comprimé le matin', '30 jours', '2025-04-15', '2025-05-15'),
(17, '2 gélules/jour', NULL, '2025-04-16', '2025-04-30'),
(18, '1 injection sous-cutanée', '7 jours', NULL, '2025-04-23'),
(19, NULL, '10 jours', '2025-04-18', '2025-04-28'),
(20, '1 suppositoire au coucher', '5 jours', '2025-04-19', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `t_prescription_medecin`
--

CREATE TABLE IF NOT EXISTS `t_prescription_medecin` (
  `id_prescription_medecin` int(10) NOT NULL AUTO_INCREMENT,
  `fk_prescription` int(10) NOT NULL,
  `fk_medecin` int(10) NOT NULL,
  PRIMARY KEY (`id_prescription_medecin`),
  KEY `fk_medecin` (`fk_medecin`),
  KEY `fk_prescription` (`fk_prescription`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_prescription_medecin`
--

INSERT INTO `t_prescription_medecin` (`id_prescription_medecin`, `fk_prescription`, `fk_medecin`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 1),
(12, 12, 2),
(13, 13, 3),
(14, 14, 4),
(15, 15, 5),
(16, 16, 5),
(17, 17, 2),
(18, 18, 9),
(19, 19, 1),
(20, 20, 10);

-- --------------------------------------------------------

--
-- Structure de la table `t_prescription_medicament`
--

CREATE TABLE IF NOT EXISTS `t_prescription_medicament` (
  `id_prescription_medicament` int(10) NOT NULL AUTO_INCREMENT,
  `fk_prescription` int(10) NOT NULL,
  `fk_medicament` int(10) NOT NULL,
  PRIMARY KEY (`id_prescription_medicament`),
  KEY `fk_medicament` (`fk_medicament`),
  KEY `fk_prescription` (`fk_prescription`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_prescription_medicament`
--

INSERT INTO `t_prescription_medicament` (`id_prescription_medicament`, `fk_prescription`, `fk_medicament`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20);

-- --------------------------------------------------------

--
-- Structure de la table `t_rapport`
--

CREATE TABLE IF NOT EXISTS `t_rapport` (
  `id_rapport` int(10) NOT NULL AUTO_INCREMENT,
  `date_rapport` date DEFAULT NULL,
  `type_rapport` varchar(100) DEFAULT NULL,
  `texte_rapport` text DEFAULT NULL,
  PRIMARY KEY (`id_rapport`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_rapport`
--

INSERT INTO `t_rapport` (`id_rapport`, `date_rapport`, `type_rapport`, `texte_rapport`) VALUES
(1, '2025-03-15', 'Rapport médical initial', 'Patient admis pour douleurs lombaires chroniques. Examen clinique réalisé. IRM prescrite.'),
(2, '2025-03-17', 'Rapport d\'imagerie', 'Résultats de l\'IRM : hernie discale confirmée au niveau L4-L5. Traitement conservateur recommandé.'),
(3, '2025-03-20', 'Rapport de suivi', 'Amélioration des symptômes après 2 semaines de physiothérapie. Douleurs réduites.'),
(4, '2025-03-22', 'Rapport d\'urgence', 'Patient admis pour crise d\'asthme sévère. Traitement d\'urgence administré avec succès.'),
(5, '2025-03-24', 'Rapport endocrinologique', 'Résultats des analyses : hypothyroïdie confirmée. Traitement par lévothyroxine instauré.'),
(6, '2025-03-26', 'Rapport de consultation', 'Consultation de suivi pour diabète. HbA1c stable à 7,2%. Rappel sur le régime alimentaire.'),
(7, '2025-03-28', 'Rapport psychologique', 'Évaluation psychologique : anxiété modérée liée au stress professionnel. Thérapie cognitive recommandée.'),
(8, '2025-03-30', 'Rapport post-opératoire', 'Cicatrisation satisfaisante après pontage coronarien. Reprise progressive des activités autorisée.'),
(9, '2025-04-01', 'Rapport gynécologique', 'Échographie pelvienne : kyste ovarien détecté, suivi recommandé dans 3 mois.'),
(10, '2025-04-02', 'Rapport gastro-entérologique', 'Endoscopie digestive : gastrite légère observée, traitement par IPP prescrit pour 4 semaines.'),
(11, '2025-04-04', 'Rapport cardiologique', 'ECG normal, absence de signes d\'ischémie myocardique. Contrôle dans 6 mois recommandé.'),
(12, '2025-04-06', 'Rapport orthopédique', 'IRM lombaire : spondylolisthésis de grade I confirmé, kinésithérapie prescrite.'),
(13, '2025-04-08', 'Rapport oncologique', 'Mammographie : aucune anomalie détectée, suivi annuel recommandé.'),
(14, '2025-04-10', 'Rapport d\'effort physique', 'Test d\'effort cardiaque : capacité normale, absence de signes pathologiques détectés.'),
(15, '2025-04-12', 'Rapport densitométrique', 'Densitométrie osseuse : ostéopénie modérée détectée, supplémentation en calcium et vitamine D prescrite.'),
(16, '2025-04-15', 'Rapport chirurgical', 'Suivi post-opératoire sans complications'),
(17, '2025-04-16', NULL, 'Résultats IRM cérébrale : pas d\'anomalies détectées'),
(18, '2025-04-17', 'Rapport cardiologique', NULL),
(19, NULL, 'Rapport de biologie', 'CRP élevée à 45 mg/L'),
(20, '2025-04-19', 'Rapport allergologique', 'Tests positifs aux acariens et pollens');

-- --------------------------------------------------------

--
-- Structure de la table `t_signe_vital`
--

CREATE TABLE IF NOT EXISTS `t_signe_vital` (
  `id_signe_vital` int(10) NOT NULL AUTO_INCREMENT,
  `date_signe` date DEFAULT NULL,
  `type_signe` varchar(50) DEFAULT NULL,
  `valeurs_signe` text DEFAULT NULL,
  PRIMARY KEY (`id_signe_vital`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_signe_vital`
--

INSERT INTO `t_signe_vital` (`id_signe_vital`, `date_signe`, `type_signe`, `valeurs_signe`) VALUES
(1, '2025-03-15', 'Fréquence cardiaque', '78 bpm'),
(2, '2025-03-16', 'Température corporelle', '37.2 °C'),
(3, '2025-03-17', 'Tension artérielle', '120/80 mmHg'),
(4, '2025-03-18', 'Fréquence respiratoire', '16 cycles/min'),
(5, '2025-03-19', 'Saturation en oxygène', '98 %'),
(6, '2025-03-20', 'Fréquence cardiaque', '85 bpm'),
(7, '2025-03-21', 'Température corporelle', '38.0 °C'),
(8, '2025-03-22', 'Tension artérielle', '140/90 mmHg'),
(9, '2025-03-23', 'Fréquence respiratoire', '20 cycles/min'),
(10, '2025-03-24', 'Saturation en oxygène', '95 %'),
(11, '2025-03-25', 'Fréquence cardiaque', '60 bpm'),
(12, '2025-03-26', 'Température corporelle', '36.8 °C'),
(13, '2025-03-27', 'Tension artérielle', '130/85 mmHg'),
(14, '2025-03-28', 'Fréquence respiratoire', '18 cycles/min'),
(15, '2025-03-29', 'Saturation en oxygène', '97 %'),
(16, '2025-04-15', 'Température', '36.8 °C'),
(17, '2025-04-16', NULL, '120/80 mmHg'),
(18, '2025-04-17', 'Fréquence cardiaque', NULL),
(19, NULL, 'Saturation O2', '97%'),
(20, '2025-04-19', 'Poids', '68.5 kg'),
(21, '2025-06-08', 'test', 'test');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `t_consultation_patient`
--
ALTER TABLE `t_consultation_patient`
  ADD CONSTRAINT `t_consultation_patient_ibfk_1` FOREIGN KEY (`fk_consultation`) REFERENCES `t_consultation` (`id_consultation`),
  ADD CONSTRAINT `t_consultation_patient_ibfk_2` FOREIGN KEY (`fk_patient`) REFERENCES `t_patient` (`id_patient`);

--
-- Contraintes pour la table `t_dossier_anamnese`
--
ALTER TABLE `t_dossier_anamnese`
  ADD CONSTRAINT `t_dossier_anamnese_ibfk_1` FOREIGN KEY (`fk_anamnese`) REFERENCES `t_anamnese` (`id_anamnese`),
  ADD CONSTRAINT `t_dossier_anamnese_ibfk_2` FOREIGN KEY (`fk_dossier`) REFERENCES `t_dossier` (`id_dossier`);

--
-- Contraintes pour la table `t_dossier_examen`
--
ALTER TABLE `t_dossier_examen`
  ADD CONSTRAINT `t_dossier_examen_ibfk_1` FOREIGN KEY (`fk_dossier`) REFERENCES `t_dossier` (`id_dossier`),
  ADD CONSTRAINT `t_dossier_examen_ibfk_2` FOREIGN KEY (`fk_examen`) REFERENCES `t_examen` (`id_examen`);

--
-- Contraintes pour la table `t_dossier_patient`
--
ALTER TABLE `t_dossier_patient`
  ADD CONSTRAINT `t_dossier_patient_ibfk_1` FOREIGN KEY (`fk_dossier`) REFERENCES `t_dossier` (`id_dossier`),
  ADD CONSTRAINT `t_dossier_patient_ibfk_2` FOREIGN KEY (`fk_patient`) REFERENCES `t_patient` (`id_patient`);

--
-- Contraintes pour la table `t_dossier_prescription`
--
ALTER TABLE `t_dossier_prescription`
  ADD CONSTRAINT `t_dossier_prescription_ibfk_1` FOREIGN KEY (`fk_dossier`) REFERENCES `t_dossier` (`id_dossier`),
  ADD CONSTRAINT `t_dossier_prescription_ibfk_2` FOREIGN KEY (`fk_prescription`) REFERENCES `t_prescription` (`id_prescription`);

--
-- Contraintes pour la table `t_dossier_rapport`
--
ALTER TABLE `t_dossier_rapport`
  ADD CONSTRAINT `t_dossier_rapport_ibfk_1` FOREIGN KEY (`fk_dossier`) REFERENCES `t_dossier` (`id_dossier`),
  ADD CONSTRAINT `t_dossier_rapport_ibfk_2` FOREIGN KEY (`fk_rapport`) REFERENCES `t_rapport` (`id_rapport`);

--
-- Contraintes pour la table `t_dossier_signe_vital`
--
ALTER TABLE `t_dossier_signe_vital`
  ADD CONSTRAINT `t_dossier_signe_vital_ibfk_1` FOREIGN KEY (`fk_dossier`) REFERENCES `t_dossier` (`id_dossier`),
  ADD CONSTRAINT `t_dossier_signe_vital_ibfk_2` FOREIGN KEY (`fk_signe_vital`) REFERENCES `t_signe_vital` (`id_signe_vital`);

--
-- Contraintes pour la table `t_prescription_medecin`
--
ALTER TABLE `t_prescription_medecin`
  ADD CONSTRAINT `t_prescription_medecin_ibfk_1` FOREIGN KEY (`fk_medecin`) REFERENCES `t_medecin` (`id_medecin`),
  ADD CONSTRAINT `t_prescription_medecin_ibfk_2` FOREIGN KEY (`fk_prescription`) REFERENCES `t_prescription` (`id_prescription`);

--
-- Contraintes pour la table `t_prescription_medicament`
--
ALTER TABLE `t_prescription_medicament`
  ADD CONSTRAINT `t_prescription_medicament_ibfk_1` FOREIGN KEY (`fk_medicament`) REFERENCES `t_medicament` (`id_medicament`),
  ADD CONSTRAINT `t_prescription_medicament_ibfk_2` FOREIGN KEY (`fk_prescription`) REFERENCES `t_prescription` (`id_prescription`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
