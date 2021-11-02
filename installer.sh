#!/bin/bash
path=$(pwd)
echo $path
echo 'Downloading repository...'
wget -O $path/tempo.zip https://github.com/renatamoon/weather_app/archive/refs/heads/tempo.zip
echo 'unzip repository'
unzip $path/tempo.zip
echo 'removing repository .zip'
rm -r $path/tempo.zip
echo 'renaming the file'
mv $path/weather_app-tempo $path/weather_app
echo "criando novo virtual enviroment"
python3 -m venv $path/weather_app/venv-new
echo "ativando o venv"
source $path/weather_app/venv-new/bin/activate
echo "mostrando todas as libraries"
pip freeze
echo "instalando as libs do requirements"
pip install -r $path/weather_app/requirements.txt
echo "mostrando todas as libraries"
pip freeze