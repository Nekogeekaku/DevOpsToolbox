
python .\gitutilities.py 2>&1 >> result.txt

python .\newapp.py 2>&1 >> result.txt


# Initier un environnement python

python -m virtualenv .

./Scripts/activate

pip install flask
python.exe -m pip install --upgrade pip (ça marche)

pip freeze > requirements.txt
pip install -r requirements.txt (si j'ajoute des choses)

# olds à la bnp
python -m pip install --upgrade pip

pip install virtualenv

virtualenv venv -p python3.10

. venv/bin/activate