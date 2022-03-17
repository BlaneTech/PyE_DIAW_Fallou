DROP DATABASE IF EXISTS PYTHON01;
CREATE DATABASE IF NOT EXISTS PYTHON01;
USE PYTHON01;
DROP TABLE IF EXISTS `MATIERE` ;
CREATE  TABLE   MATIERE  (
    id_MATIERE INT PRIMARY KEY AUTO_INCREMENT,
    nom_MATIERE VARCHAR(40)
    );
DROP TABLE IF EXISTS CLASSE ;
CREATE  TABLE   CLASSE(
    id_CLASSE INT PRIMARY KEY AUTO_INCREMENT,
    nom_CLASSE VARCHAR(40)
    );
DROP TABLE IF EXISTS ETUDIANT ;
CREATE  TABLE   ETUDIANT (
    id_ETUDIANT INT PRIMARY KEY AUTO_INCREMENT,
    numero_ETUDIANT VARCHAR(40),
    nom_ETUDIANT VARCHAR(40) NOT  NULL,
    prenom_ETUDIANT VARCHAR(40) NOT  NULL ,
    dateNais_ETUDIANT DATE,
    id_CLASSE INT
    );
DROP TABLE IF EXISTS NOTE ;
CREATE  TABLE   NOTE (
    id_NOTE INT PRIMARY KEY AUTO_INCREMENT,
    valeur FLOAT,
    type VARCHAR(20),
    id_ETUDIANT INT,
    id_MATIERE INT
    );
DROP TABLE IF EXISTS MOYENNE ;
CREATE  TABLE   MOYENNE (
    id_MOYENNE INT PRIMARY KEY AUTO_INCREMENT ,
    valeur_MOYENNE FLOAT ,
    id_ETUDIANT INT);

ALTER TABLE ETUDIANT ADD CONSTRAINT FK_id_CLASSE FOREIGN KEY (id_CLASSE) REFERENCES CLASSE(id_CLASSE);
ALTER TABLE NOTE ADD CONSTRAINT FK_id_MATIERE FOREIGN KEY (id_MATIERE) REFERENCES MATIERE(id_MATIERE);
ALTER TABLE NOTE ADD CONSTRAINT FK_id_ETUDIANT FOREIGN KEY (id_ETUDIANT) REFERENCES ETUDIANT(id_ETUDIANT);
ALTER TABLE MOYENNE ADD CONSTRAINT FK_id_ETUDIANT_moyenne FOREIGN KEY (id_ETUDIANT) REFERENCES ETUDIANT(id_ETUDIANT);