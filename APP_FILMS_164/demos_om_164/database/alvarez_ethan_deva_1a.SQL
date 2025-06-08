-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: MACCAUD_OLIVIER_INFO1X_FILMS_164_2023

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS alvarez_ethan_deva_1a;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS alvarez_ethan_deva_1a;

-- Utilisation de cette base de donnée

USE alvarez_ethan_deva_1a;
-- --------------------------------------------------------

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 05 mars 2025 à 08:36
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

-- --------------------------------------------------------

--
-- Structure de la table `t_anamnese`
--

CREATE TABLE `t_anamnese` (
  `id_anamnese` int(10) NOT NULL,
  `histoire_de_vie_anamn` text DEFAULT NULL,
  `antecedent_medicaux_anamn` text DEFAULT NULL,
  `probleme_anamn` text DEFAULT NULL,
  `allergies_anamn` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_consultation`
--

CREATE TABLE `t_consultation` (
  `id_consultation` int(10) NOT NULL,
  `date_consult` date DEFAULT NULL,
  `motif_consult` varchar(255) DEFAULT NULL,
  `diagnostic_consult` varchar(255) DEFAULT NULL,
  `notes_consult` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_consultation_patient`
--

CREATE TABLE `t_consultation_patient` (
  `id_consultation_patient` int(10) NOT NULL,
  `fk_consultation` int(10) NOT NULL,
  `fk_patient` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier`
--

CREATE TABLE `t_dossier` (
  `id_dossier` int(10) NOT NULL,
  `ouverture_dossier` date DEFAULT NULL,
  `cloture_dossier` date DEFAULT NULL,
  `statut_dossier` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_anamnese`
--

CREATE TABLE `t_dossier_anamnese` (
  `id_dossier_anamnese` int(10) NOT NULL,
  `fk_dossier` int(10) NOT NULL,
  `fk_anamnese` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_examen`
--

CREATE TABLE `t_dossier_examen` (
  `id_dossier_examen` int(10) NOT NULL,
  `fk_dossier` int(10) NOT NULL,
  `fk_examen` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_patient`
--

CREATE TABLE `t_dossier_patient` (
  `id_dossier_patient` int(10) NOT NULL,
  `fk_dossier` int(10) NOT NULL,
  `fk_patient` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_prescription`
--

CREATE TABLE `t_dossier_prescription` (
  `id_dossier_prescription` int(10) NOT NULL,
  `fk_dossier` int(10) NOT NULL,
  `fk_prescription` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_rapport`
--

CREATE TABLE `t_dossier_rapport` (
  `id_dossier_rapport` int(10) NOT NULL,
  `fk_dossier` int(10) NOT NULL,
  `fk_rapport` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dossier_signe_vital`
--

CREATE TABLE `t_dossier_signe_vital` (
  `id_dossier_signe_vital` int(10) NOT NULL,
  `fk_dossier` int(10) NOT NULL,
  `fk_signe_vital` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_examen`
--

CREATE TABLE `t_examen` (
  `id_examen` int(10) NOT NULL,
  `type_examen` varchar(100) DEFAULT NULL,
  `date_examen` date DEFAULT NULL,
  `resultats_examen` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_medecin`
--

CREATE TABLE `t_medecin` (
  `id_medecin` int(10) NOT NULL,
  `nom_medecin` varchar(100) DEFAULT NULL,
  `prenom_medecin` varchar(100) DEFAULT NULL,
  `telephone_medecin` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_medicament`
--

CREATE TABLE `t_medicament` (
  `id_medicament` int(10) NOT NULL,
  `nom_medic` varchar(100) DEFAULT NULL,
  `dosage_medic` int(10) DEFAULT NULL,
  `forme_medic` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_patient`
--

CREATE TABLE `t_patient` (
  `id_patient` int(10) NOT NULL,
  `nom_patient` varchar(255) DEFAULT NULL,
  `prenom_patient` varchar(255) DEFAULT NULL,
  `date_naissance_pers` date DEFAULT NULL,
  `localite_patient` varchar(100) DEFAULT NULL,
  `code_postal_patient` int(10) DEFAULT NULL,
  `nom_rue_patient` varchar(100) DEFAULT NULL,
  `numero_rue_patient` int(10) DEFAULT NULL,
  `telephone_patient` varchar(20) DEFAULT NULL,
  `e-mail_patient` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_prescription`
--

CREATE TABLE `t_prescription` (
  `id_prescription` int(10) NOT NULL,
  `posologie_prescr` int(255) DEFAULT NULL,
  `duree_traitement_prescr` decimal(5,2) DEFAULT NULL,
  `debut_prescr` date DEFAULT NULL,
  `fin_prescr` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_prescription_medecin`
--

CREATE TABLE `t_prescription_medecin` (
  `id_prescription_medecin` int(10) NOT NULL,
  `fk_prescription` int(10) NOT NULL,
  `fk_medecin` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_prescription_medicament`
--

CREATE TABLE `t_prescription_medicament` (
  `id_prescription_medicament` int(10) NOT NULL,
  `fk_prescription` int(10) NOT NULL,
  `fk_medicament` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_rapport`
--

CREATE TABLE `t_rapport` (
  `id_rapport` int(10) NOT NULL,
  `date_rapport` date DEFAULT NULL,
  `type_rapport` varchar(100) DEFAULT NULL,
  `texte_rapport` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_signe_vital`
--

CREATE TABLE `t_signe_vital` (
  `id_signe_vital` int(10) NOT NULL,
  `date_signe` date DEFAULT NULL,
  `type_signe` varchar(20) DEFAULT NULL,
  `valeurs_signe` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `t_anamnese`
--
ALTER TABLE `t_anamnese`
  ADD PRIMARY KEY (`id_anamnese`);

--
-- Index pour la table `t_consultation`
--
ALTER TABLE `t_consultation`
  ADD PRIMARY KEY (`id_consultation`);

--
-- Index pour la table `t_consultation_patient`
--
ALTER TABLE `t_consultation_patient`
  ADD PRIMARY KEY (`id_consultation_patient`),
  ADD KEY `fk_consultation` (`fk_consultation`),
  ADD KEY `fk_patient` (`fk_patient`);

--
-- Index pour la table `t_dossier`
--
ALTER TABLE `t_dossier`
  ADD PRIMARY KEY (`id_dossier`);

--
-- Index pour la table `t_dossier_anamnese`
--
ALTER TABLE `t_dossier_anamnese`
  ADD PRIMARY KEY (`id_dossier_anamnese`),
  ADD KEY `fk_anamnese` (`fk_anamnese`),
  ADD KEY `fk_dossier` (`fk_dossier`);

--
-- Index pour la table `t_dossier_examen`
--
ALTER TABLE `t_dossier_examen`
  ADD PRIMARY KEY (`id_dossier_examen`),
  ADD KEY `fk_dossier` (`fk_dossier`),
  ADD KEY `fk_examen` (`fk_examen`);

--
-- Index pour la table `t_dossier_patient`
--
ALTER TABLE `t_dossier_patient`
  ADD PRIMARY KEY (`id_dossier_patient`),
  ADD KEY `fk_dossier` (`fk_dossier`),
  ADD KEY `fk_patient` (`fk_patient`);

--
-- Index pour la table `t_dossier_prescription`
--
ALTER TABLE `t_dossier_prescription`
  ADD PRIMARY KEY (`id_dossier_prescription`),
  ADD KEY `fk_dossier` (`fk_dossier`),
  ADD KEY `fk_prescription` (`fk_prescription`);

--
-- Index pour la table `t_dossier_rapport`
--
ALTER TABLE `t_dossier_rapport`
  ADD PRIMARY KEY (`id_dossier_rapport`),
  ADD KEY `fk_dossier` (`fk_dossier`),
  ADD KEY `fk_rapport` (`fk_rapport`);

--
-- Index pour la table `t_dossier_signe_vital`
--
ALTER TABLE `t_dossier_signe_vital`
  ADD PRIMARY KEY (`id_dossier_signe_vital`),
  ADD KEY `fk_dossier` (`fk_dossier`),
  ADD KEY `fk_signe_vital` (`fk_signe_vital`);

--
-- Index pour la table `t_examen`
--
ALTER TABLE `t_examen`
  ADD PRIMARY KEY (`id_examen`);

--
-- Index pour la table `t_medecin`
--
ALTER TABLE `t_medecin`
  ADD PRIMARY KEY (`id_medecin`);

--
-- Index pour la table `t_medicament`
--
ALTER TABLE `t_medicament`
  ADD PRIMARY KEY (`id_medicament`);

--
-- Index pour la table `t_patient`
--
ALTER TABLE `t_patient`
  ADD PRIMARY KEY (`id_patient`);

--
-- Index pour la table `t_prescription`
--
ALTER TABLE `t_prescription`
  ADD PRIMARY KEY (`id_prescription`);

--
-- Index pour la table `t_prescription_medecin`
--
ALTER TABLE `t_prescription_medecin`
  ADD PRIMARY KEY (`id_prescription_medecin`),
  ADD KEY `fk_medecin` (`fk_medecin`),
  ADD KEY `fk_prescription` (`fk_prescription`);

--
-- Index pour la table `t_prescription_medicament`
--
ALTER TABLE `t_prescription_medicament`
  ADD PRIMARY KEY (`id_prescription_medicament`),
  ADD KEY `fk_medicament` (`fk_medicament`),
  ADD KEY `fk_prescription` (`fk_prescription`);

--
-- Index pour la table `t_rapport`
--
ALTER TABLE `t_rapport`
  ADD PRIMARY KEY (`id_rapport`);

--
-- Index pour la table `t_signe_vital`
--
ALTER TABLE `t_signe_vital`
  ADD PRIMARY KEY (`id_signe_vital`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `t_anamnese`
--
ALTER TABLE `t_anamnese`
  MODIFY `id_anamnese` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_consultation`
--
ALTER TABLE `t_consultation`
  MODIFY `id_consultation` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_consultation_patient`
--
ALTER TABLE `t_consultation_patient`
  MODIFY `id_consultation_patient` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier`
--
ALTER TABLE `t_dossier`
  MODIFY `id_dossier` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier_anamnese`
--
ALTER TABLE `t_dossier_anamnese`
  MODIFY `id_dossier_anamnese` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier_examen`
--
ALTER TABLE `t_dossier_examen`
  MODIFY `id_dossier_examen` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier_patient`
--
ALTER TABLE `t_dossier_patient`
  MODIFY `id_dossier_patient` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier_prescription`
--
ALTER TABLE `t_dossier_prescription`
  MODIFY `id_dossier_prescription` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier_rapport`
--
ALTER TABLE `t_dossier_rapport`
  MODIFY `id_dossier_rapport` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dossier_signe_vital`
--
ALTER TABLE `t_dossier_signe_vital`
  MODIFY `id_dossier_signe_vital` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_examen`
--
ALTER TABLE `t_examen`
  MODIFY `id_examen` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_medecin`
--
ALTER TABLE `t_medecin`
  MODIFY `id_medecin` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_medicament`
--
ALTER TABLE `t_medicament`
  MODIFY `id_medicament` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_patient`
--
ALTER TABLE `t_patient`
  MODIFY `id_patient` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_prescription`
--
ALTER TABLE `t_prescription`
  MODIFY `id_prescription` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_prescription_medecin`
--
ALTER TABLE `t_prescription_medecin`
  MODIFY `id_prescription_medecin` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_prescription_medicament`
--
ALTER TABLE `t_prescription_medicament`
  MODIFY `id_prescription_medicament` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_rapport`
--
ALTER TABLE `t_rapport`
  MODIFY `id_rapport` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_signe_vital`
--
ALTER TABLE `t_signe_vital`
  MODIFY `id_signe_vital` int(10) NOT NULL AUTO_INCREMENT;

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
