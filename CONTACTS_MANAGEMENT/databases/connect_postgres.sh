#!/bin/bash

# Remplacez ces informations par les détails de votre base de données PostgreSQL
DATABASE_NAME="Clients"
USER="votre_utilisateur"
PASSWORD="votre_mot_de_passe"
HOST="votre_hote"
PORT="votre_port"

# Connexion à la base de données
psql -h $HOST -d $DATABASE_NAME -U $USER -W
