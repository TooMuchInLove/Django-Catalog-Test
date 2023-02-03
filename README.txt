¬ Django дл€ заполнени€ данных в базе данных мы можем выполнить команду:
	python manage.py loaddata <file>
* python manage.py loaddata seeder/position.json
* python manage.py loaddata seeder/users.json

‘айл - файл со спецификацией исходных данных, которые мы хотим сохранить в базе данных. ћы можем записать данные, которые вы хотите сохранить, в базу данных в формате XML, JSON или YAML.

OnlineCatalog/
| ----- media/
| ----- OnlineCatalog/
| ----- seeder/
| ---------- positions.json
| ---------- users.json
| ----- Staff/
| ----- db.sqlite3
| ----- manage.py
| ----- README
