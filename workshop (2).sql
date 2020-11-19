-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 19 nov. 2020 à 16:10
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `workshop`
--

-- --------------------------------------------------------

--
-- Structure de la table `materials`
--

DROP TABLE IF EXISTS `materials`;
CREATE TABLE IF NOT EXISTS `materials` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `id_recycling` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Id_recycling` (`id_recycling`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `materials`
--

INSERT INTO `materials` (`id`, `name`, `id_recycling`) VALUES
(1, 'carton', 1),
(2, 'verre', 2),
(3, 'déchet non recyclable', 3),
(4, 'aluminium', 1),
(5, 'plastique', 1),
(6, 'papier', 1);

-- --------------------------------------------------------

--
-- Structure de la table `recycling`
--

DROP TABLE IF EXISTS `recycling`;
CREATE TABLE IF NOT EXISTS `recycling` (
  `id` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `recycling`
--

INSERT INTO `recycling` (`id`, `type`) VALUES
(1, 'jaune'),
(2, 'vert'),
(3, 'noir');

-- --------------------------------------------------------

--
-- Structure de la table `waste`
--

DROP TABLE IF EXISTS `waste`;
CREATE TABLE IF NOT EXISTS `waste` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `id_material` int(11) NOT NULL,
  `barcode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Id_material` (`id_material`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `waste`
--

INSERT INTO `waste` (`id`, `name`, `id_material`, `barcode`) VALUES
(1, 'pitch', 1, '5202462035'),
(2, 'boite_cereale', 1, '552362462035'),
(3, 'chouffe33', 4, '5554682462035'),
(4, 'jus innocent', 5, '5038862135443');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `materials`
--
ALTER TABLE `materials`
  ADD CONSTRAINT `materials_ibfk_1` FOREIGN KEY (`id_recycling`) REFERENCES `recycling` (`id`);

--
-- Contraintes pour la table `waste`
--
ALTER TABLE `waste`
  ADD CONSTRAINT `waste_ibfk_1` FOREIGN KEY (`id_material`) REFERENCES `materials` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
