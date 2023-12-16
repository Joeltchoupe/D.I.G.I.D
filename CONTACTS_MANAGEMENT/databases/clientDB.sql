CREATE DATABASE Clients;

\c Clients;

CREATE TABLE PersonalDatas (
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
