# Run app
## Clone repo
```
git clone https://github.com/Yukie-Billal/flask-studikasus.git
```

## install depedencies package
```
python3 -m venv venv

"venv/scripts/activate"

pip install -r requirements.txt
```

## database
make a new database in your mysql server. and customize in .env file

after make a database. You have to migrate the table
```
flask db migrate
flask db upgrade
```

## run the app
```
flask run
```
