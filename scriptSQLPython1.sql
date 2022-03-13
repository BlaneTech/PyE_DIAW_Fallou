DROP DATABASE IF EXISTS PYTHON01;
CREATE DATABASE IF NOT EXISTS PYTHON01;
USE PYTHON01;
DROP TABLE IF EXISTS ETUDIANT ;
 CREATE TABLE ETUDIANT (
     numero_ETUDIANT VARCHAR(255) NOT NULL, 
     nom_ETUDIANT VARCHAR(255), 
     prenom_ETUDIANT VARCHAR(255), 
     dateNais_ETUDIANT VARCHAR(255), 
     PRIMARY KEY (numero_ETUDIANT)) 
     ENGINE=InnoDB;  
DROP TABLE IF EXISTS DEVOIR ;     
CREATE TABLE DEVOIR (
    id_DEVOIR INT AUTO_INCREMENT NOT NULL,
    numero_DEVOIR INT, 
    note_DEVOIR FLOAT, 
    PRIMARY KEY (id_DEVOIR)) 
    ENGINE=InnoDB;       
DROP TABLE IF EXISTS MATIERE ; 
CREATE TABLE MATIERE (
    id_MATIERE INT AUTO_INCREMENT NOT NULL,
    nom_MATIERE VARCHAR(255) NOT NULL, 
    id_DEVOIR INT, 
    PRIMARY KEY (id_MATIERE)) 
    ENGINE=InnoDB;  
 

DROP TABLE IF EXISTS CLASSE ; 
CREATE TABLE CLASSE (
    id_CLASSE INT AUTO_INCREMENT NOT NULL,
    nom_CLASSE VARCHAR(255), 
    numero_ETUDIANT VARCHAR(255), 
    PRIMARY KEY (id_CLASSE)) 
    ENGINE=InnoDB;  
DROP TABLE IF EXISTS FAIRE ; 
CREATE TABLE FAIRE (
    numero_ETUDIANT VARCHAR(255) NOT NULL, 
    id_DEVOIR INT, 
    PRIMARY KEY (numero_ETUDIANT,  id_DEVOIR)) 
    ENGINE=InnoDB;  
DROP TABLE IF EXISTS SUIVRE ; 
CREATE TABLE SUIVRE (
    numero_ETUDIANT VARCHAR(255) NOT NULL, 
    id_MATIERE INT NOT NULL, 
    noteExamen_CONCERNER INT, 
    PRIMARY KEY (numero_ETUDIANT,  id_MATIERE)) 
    ENGINE=InnoDB;  
ALTER TABLE MATIERE ADD CONSTRAINT FK_MATIERE_id_DEVOIR FOREIGN KEY (id_DEVOIR) REFERENCES DEVOIR (id_DEVOIR); 
ALTER TABLE CLASSE ADD CONSTRAINT FK_CLASSE_numero_ETUDIANT FOREIGN KEY (numero_ETUDIANT) REFERENCES ETUDIANT (numero_ETUDIANT); 
ALTER TABLE FAIRE ADD CONSTRAINT FK_FAIRE_numero_ETUDIANT FOREIGN KEY (numero_ETUDIANT) REFERENCES ETUDIANT (numero_ETUDIANT); ALTER TABLE FAIRE ADD CONSTRAINT FK_FAIRE_id_DEVOIR FOREIGN KEY (id_DEVOIR) REFERENCES DEVOIR (id_DEVOIR); 
ALTER TABLE SUIVRE ADD CONSTRAINT FK_SUIVRE_numero_ETUDIANT FOREIGN KEY (numero_ETUDIANT) REFERENCES ETUDIANT (numero_ETUDIANT); 
ALTER TABLE SUIVRE ADD CONSTRAINT FK_SUIVRE_id_MATIERE FOREIGN KEY (id_MATIERE) REFERENCES MATIERE (id_MATIERE); 