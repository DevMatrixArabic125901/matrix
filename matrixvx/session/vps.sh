#!/bin/bash

MATRIX="\nMATRIX USERBOT DEPLOY ON VPS"
MATRIX+="\n "
MATRIX+="\n "
MATRIX+="\nChannel: @Matrix_Thon"
MATRIX+="\nSupport: @MatrixzSupport"
MATRIX+="\n "
MATR="\n "
echo -e $MATRIX
echo -e $MATR
echo "WAIT ..."
echo -e $MATR

# Update and install dependencies  :)
sudo apt update && upgrade -y
sudo apt install postgresql postgresql-contrib
sudo apt install --no-install-recommends -y \
curl \
git \
libffi-dev \
libjpeg-dev \
libwebp-dev \
python3-lxml \
python3-psycopg2 \
libpq-dev \
libcurl4-openssl-dev \
libxml2-dev \
libxslt1-dev \
python3-pip \
python3-sqlalchemy \
openssl \
wget \
python3 \
python3-dev \
libreadline-dev \
libyaml-dev \
gcc \
zlib1g \
ffmpeg \
libssl-dev \
libgconf-2-4 \
libxi6 \
unzip \
libopus0 \
libopus-dev \
python3-venv \
libmagickwand-dev \
pv \
tree \
mediainfo \
nano \
nodejs
clear
echo "⚙️ Github Installer"
echo -e $MATR
echo -e $MATRIX
echo -e $MATR
echo "Cloning MATRIX Userbot"
echo -e $MATR
git clone -b bro https://github.com/qithoniq/matrix
echo -e $MATRIX
echo -e $MATR
echo "runing MATRIX now"
echo -e $MATR
cd sbb_b0

# Rename sample_config.py to config.py
mv MATRIX.py config.py
echo "⚙️ Environment "
echo -e $MATR

# Generate a random password  - باسوورد عشوائي لقاعدة البيانات   xD
PASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

# Connect to the PostgreSQL interactive terminal
sudo su - postgres -c "psql" <<EOF

ALTER USER postgres WITH PASSWORD '$PASSWORD';

CREATE DATABASE MATRIX;

\q
exit
EOF

# database
DATABASE_URL="postgresql://postgres:$PASSWORD@localhost:5432/MATRIX"

# Ask the user for some environment variables and add them to .env
if [ ! -f .env ]; then
  touch .env
fi

echo "Enter your name:"
read alive_name
echo -e $MATR
echo "Enter app id:"
read app_id
echo -e $MATR
echo "Enter your api hash:"
read api_hash
echo -e $MATR
echo "Enter your session:"
read session
echo -e $MATR
echo "Enter your bot token:"
read token
echo -e $MATR

echo "ALIVE_NAME=$alive_name" >> .env
echo "APP_ID=$app_id" >> .env
echo "API_HASH=$api_hash" >> .env
echo "STRING_SESSION=$session" >> .env
echo "TG_BOT_TOKEN=$token" >> .env
echo "DATABASE_URL=$DATABASE_URL" >> .env
clear
echo -e $MATRIX
echo -e $MATR
