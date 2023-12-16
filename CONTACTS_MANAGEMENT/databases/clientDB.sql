CREATE DATABASE IF NOT EXISTS  Clients;

\c Clients;

CREATE TABLE IF NOT EXISTS PersonalDatas (
    ClientID SERIAL PRIMARY KEY,
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL,
    DateNaissance DATE,
    Sexe CHAR(1),
    AdressePostale VARCHAR(255),
    AdresseEmail VARCHAR(100),
    NumeroTelephone VARCHAR(20),
    NumeroSecuriteSociale VARCHAR(20),
    EtatCivil VARCHAR(20),
    SituationFamiliale VARCHAR(50),
    Nationalite VARCHAR(50),
    Profession VARCHAR(50),
    Revenu DECIMAL(15, 2),
    SituationPatrimoniale TEXT
);
--------------------------------------------------
-- Création de la table Client
CREATE TABLE Client (
    ClientID SERIAL PRIMARY KEY,
    Nom VARCHAR(50),
    Prenom VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    MotDePasse VARCHAR(255), -- Utiliser un bon algorithme de hachage pour stocker les mots de passe
    QuestionSecrete VARCHAR(255),
    CodeConfidentiel INT,
    DateInscription DATE
    -- Ajoutez d'autres champs client selon les besoins
);

-- Création d'une table pour stocker les informations de contact du client
CREATE TABLE Contact (
    ContactID SERIAL PRIMARY KEY,
    ClientID INT REFERENCES Client(ClientID),
    Adresse VARCHAR(255),
    Ville VARCHAR(50),
    CodePostal VARCHAR(10),
    Pays VARCHAR(50),
    Telephone VARCHAR(20)
);

-- Création d'une table pour stocker les transactions du client
CREATE TABLE Transaction (
    TransactionID SERIAL PRIMARY KEY,
    ClientID INT REFERENCES Client(ClientID),
    Montant DECIMAL(10, 2),
    DateTransaction DATE,
    TypeTransaction VARCHAR(50)
);

-- Création d'une table pour stocker les données bancaires du client
CREATE TABLE DonneesBancaires (
    BanqueID SERIAL PRIMARY KEY,
    ClientID INT REFERENCES Client(ClientID),
    NumeroCompte VARCHAR(20),
    Solde DECIMAL(10, 2),
    TypeCompte VARCHAR(50)
);

-- Création d'une table pour stocker les données de géolocalisation du client
CREATE TABLE Geolocalisation (
    GeolocalisationID SERIAL PRIMARY KEY,
    ClientID INT REFERENCES Client(ClientID),
    Latitude DECIMAL(9, 6),
    Longitude DECIMAL(9, 6),
    AdresseIP VARCHAR(15)
);

-- Création d'une table pour stocker les données comportementales du client
CREATE TABLE Comportement (
    ComportementID SERIAL PRIMARY KEY,
    ClientID INT REFERENCES Client(ClientID),
    ActivitePrincipale VARCHAR(255),
    DerniereConnexion TIMESTAMPTZ
);

-- Ajoutez d'autres tables en fonction des besoins de votre application
