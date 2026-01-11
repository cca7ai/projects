-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 26 oct. 2023 à 23:14
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `cinema`
--
CREATE DATABASE IF NOT EXISTS `cinema` ;
USE `cinema`;

-- --------------------------------------------------------

--
-- Structure de la table `acteur`
--

DROP TABLE IF EXISTS `acteur`;
CREATE TABLE IF NOT EXISTS `acteur` (
  `codeActeur` varchar(50) NOT NULL,
  `nomActeur` varchar(50) DEFAULT NULL,
  `prenomActeur` varchar(50) DEFAULT NULL,
  `dateNaissanceActeur` date DEFAULT NULL,
  `genreActeur` varchar(50) DEFAULT NULL,
  `dateDecesActeur` date DEFAULT NULL,
  PRIMARY KEY (`codeActeur`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `acteur`
--

INSERT INTO `acteur` (`codeActeur`, `nomActeur`, `prenomActeur`, `dateNaissanceActeur`, `genreActeur`, `dateDecesActeur`) VALUES
('WAHY', 'WANGRAWA', 'Hyppolite', '1956-12-31', 'Homme', NULL),
('YODI', 'YODA', 'Dieudonné', '1972-07-15', 'Homme', NULL),
('KOAB', 'KOMBOUDRI', 'Abdoulaye', '1959-05-03', 'Homme', NULL),
('OUDE', 'OUATTARA', 'Delphine', '1967-04-29', 'Femme', NULL),
('HESE', 'HENRY', 'Serge', '1960-12-31', 'Homme', NULL),
('BAEU', 'BAYALA', 'Eugène', '1966-12-31', 'Homme', NULL),
('DIAM', 'DIALLO', 'Aminata', '1972-12-31', 'Femme', NULL),
('OURA', 'OUEDRAOGO', 'Rasmané', '1966-12-31', 'Homme', NULL),
('MEIL', 'MEDA', 'Ildevert', '1966-05-27', 'Homme', NULL),
('SAIS', 'SAWADOGO', 'Issaka', '1966-05-18', 'Homme', NULL),
('KOSO', 'KOUYATE', 'Sotigui', '1936-07-19', 'Homme', '2010-04-17'),
('BOAM', 'BOUROU', 'Amadou', '1951-10-14', 'Homme', '2010-01-08'),
('SAAL', 'SAWADOGO', 'Alidou', '1955-12-31', 'Homme', NULL),
('SOGU', 'SORGHO', 'Gustave', '1953-03-25', 'Homme', NULL),
('NDMA', 'NDIAYE', 'Maïmouna', '1970-12-31', 'Femme', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `festival`
--

DROP TABLE IF EXISTS `festival`;
CREATE TABLE IF NOT EXISTS `festival` (
  `codeFestival` varchar(50) NOT NULL,
  `nomFestival` varchar(50) DEFAULT NULL,
  `paysFestival` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`codeFestival`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `festival`
--

INSERT INTO `festival` (`codeFestival`, `nomFestival`, `paysFestival`) VALUES
('FES', 'Festival Panafricain du Cinema de Ouagadougou (FES', 'Burkina Faso'),
('FC', 'Festival de Cannes', 'France'),
('FIT', 'Festival international du film de Tokyo', 'Japon'),
('FB', 'Festival International du Film de Berlin', 'Allemagne'),
('OS', 'Les Oscars (Academy Awards)', 'Etats-Unis'),
('CES', 'Les César du cinéma', 'France');

-- --------------------------------------------------------

--
-- Structure de la table `film`
--

DROP TABLE IF EXISTS `film`;
CREATE TABLE IF NOT EXISTS `film` (
  `codeFilm` varchar(50) NOT NULL,
  `titre` varchar(50) DEFAULT NULL,
  `duree` int DEFAULT NULL,
  `anneeProduction` varchar(50) DEFAULT NULL,
  `budget` varchar(50) DEFAULT NULL,
  `codeRealisateur` varchar(50) NOT NULL,
  PRIMARY KEY (`codeFilm`),
  KEY `codeRealisateur` (`codeRealisateur`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `film`
--

INSERT INTO `film` (`codeFilm`, `titre`, `duree`, `anneeProduction`, `budget`, `codeRealisateur`) VALUES
('DESTA', 'Desrances', 105, '2019', '710819952', 'TA'),
('SIRTA', 'SIRA', 122, '2023', '800000000', 'TA'),
('ENAHM', 'En attendant le vote', 100, '2011', '250000000', 'HM'),
('SIAKD', 'Sia, le rêve du python', 96, '2001', '1400000000', 'KD'),
('EPIDA', 'Epines du Sahel', 91, '2023', '230000000', 'DA'),
('LESDA', 'Les trois lascars', 122, '2023', '170000000', 'DA'),
('CODDA', 'Code Phénix', 90, '2005', '90000000', 'DA'),
('YAAOI', 'Yaaba', 90, '1989', '180000000', 'OI'),
('LACOI', 'La Colère des dieux', 95, '2003', '200000000', 'OI'),
('SAMOI', 'Samba Traoré', 97, '1993', '350000', 'OI');

-- --------------------------------------------------------

--
-- Structure de la table `jouer`
--

DROP TABLE IF EXISTS `jouer`;
CREATE TABLE IF NOT EXISTS `jouer` (
  `codeActeur` varchar(50) NOT NULL,
  `codeFilm` varchar(50) NOT NULL,
  PRIMARY KEY (`codeActeur`,`codeFilm`),
  KEY `codeFilm` (`codeFilm`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `jouer`
--

INSERT INTO `jouer` (`codeActeur`, `codeFilm`) VALUES
('HESE', 'ENAHM'),
('KOAB', 'SAMOI'),
('KOAB', 'SIAKD'),
('KOSO', 'SIAKD'),
('NDMA', 'LESDA'),
('OUDE', 'CODDA'),
('OUDE', 'DESTA'),
('OURA', 'LACOI'),
('OURA', 'YAAOI'),
('SAIS', 'LESDA'),
('WAHY', 'SAMOI'),
('YODI', 'CODDA'),
('YODI', 'LESDA');

-- --------------------------------------------------------

--
-- Structure de la table `nominer`
--

DROP TABLE IF EXISTS `nominer`;
CREATE TABLE IF NOT EXISTS `nominer` (
  `codeFilm` varchar(50) NOT NULL,
  `codeFestival` varchar(50) NOT NULL,
  `anneeNomination` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`codeFilm`,`codeFestival`),
  KEY `codeFestival` (`codeFestival`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `nominer`
--

INSERT INTO `nominer` (`codeFilm`, `codeFestival`, `anneeNomination`) VALUES
('SIRTA', 'FB', '2023'),
('SIRTA', 'FES', '2023'),
('YAAOI', 'FES', '1989'),
('YAAOI', 'FIT', '1989'),
('YAAOI', 'FC', '1989'),
('ENAHM', 'FES', '2011'),
('DESTA', 'FES', '2019'),
('SIAKD', 'FES', '2001'),
('LESDB', 'FES', '2021');

-- --------------------------------------------------------

--
-- Structure de la table `realisateur`
--

DROP TABLE IF EXISTS `realisateur`;
CREATE TABLE IF NOT EXISTS `realisateur` (
  `codeRealisateur` varchar(50) NOT NULL,
  `nomRealisateur` varchar(50) DEFAULT NULL,
  `prenomRealisateur` varchar(50) DEFAULT NULL,
  `dateNaissanceRealisateur` date DEFAULT NULL,
  `genreRealisateur` varchar(50) DEFAULT NULL,
  `dateDecesRealisateur` date DEFAULT NULL,
  PRIMARY KEY (`codeRealisateur`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `realisateur`
--

INSERT INTO `realisateur` (`codeRealisateur`, `nomRealisateur`, `prenomRealisateur`, `dateNaissanceRealisateur`, `genreRealisateur`, `dateDecesRealisateur`) VALUES
('OI', 'OUEDRAOGO', 'Idrissa', '1954-01-21', 'Homme', '2018-01-18'),
('KG', 'KABORE', 'Gaston', '1951-04-23', 'Homme', NULL),
('NF', 'NACRO', 'Fanta Regina', '1962-09-04', 'Femme', NULL),
('KD', 'KOUYATE', 'Dani', '1961-06-04', 'Homme', NULL),
('DA', 'DIALLO', 'Aminata', '1972-12-31', 'Femme', NULL),
('DB', 'DIALLO', 'Boubakar', '1962-12-31', 'Homme', NULL),
('TA', 'TRAORE', 'Appoline', '1976-12-31', 'Femme', NULL),
('HM', 'HEBIE', 'Missa', '1951-12-31', 'Homme', '2018-09-26'),
('YP', 'YAMEOGO', 'Pierre', '1955-05-31', 'Homme', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
