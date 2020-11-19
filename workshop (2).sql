-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  jeu. 19 nov. 2020 à 14:10
-- Version du serveur :  10.4.8-MariaDB
-- Version de PHP :  7.3.11

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

CREATE TABLE `materials` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `id_recycling` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `materials`
--

INSERT INTO `materials` (`id`, `name`, `id_recycling`) VALUES
(1, 'carton', 1),
(2, 'bouteille verre', 2),
(3, 'plastique souple', 3),
(4, 'aluminium', 3),
(5, 'bouteille plastique', 1);

-- --------------------------------------------------------

--
-- Structure de la table `recycling`
--

CREATE TABLE `recycling` (
  `id` int(11) NOT NULL,
  `type` varchar(50) NOT NULL
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

CREATE TABLE `waste` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `id_material` int(11) NOT NULL,
  `barcode` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `waste`
--

INSERT INTO `waste` (`id`, `name`, `id_material`, `barcode`) VALUES
(1, 'pitch', 3, '5202462035'),
(2, 'boite_cereale', 1, '552362462035'),
(3, 'chouffe33', 4, '5554682462035'),
(4, 'jus innocent', 5, '5038862135443');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Id_recycling` (`id_recycling`);

--
-- Index pour la table `recycling`
--
ALTER TABLE `recycling`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `waste`
--
ALTER TABLE `waste`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Id_material` (`id_material`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `waste`
--
ALTER TABLE `waste`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `materials`
--
ALTER TABLE `materials`
  ADD CONSTRAINT `materials_ibfk_1` FOREIGN KEY (`Id_recycling`) REFERENCES `recycling` (`Id`);

--
-- Contraintes pour la table `waste`
--
ALTER TABLE `waste`
  ADD CONSTRAINT `waste_ibfk_1` FOREIGN KEY (`Id_material`) REFERENCES `materials` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
