1. Create project folder
2. Open it in cmd line as admin
3. Create virtual environment as `python -m venv ./venv`
4. Activate it as `venv\scripts\activate` (Windows) or `source venv/bin/activate` (Mac)
5. You can deactivate as `venv\scripts\deactivate` (Windows) or `deactivate` (Mac)
6. Install Django as `pip install django`
7. Confirm using pip list
8. Running `django-admin` should now give you access to the Django commands
9. Create a new project as `django-admin startproject project-name .` - the period confirms you want it in the same folder
10. Run the server as `python [manage.py](http://manage.py/) runserver` - visible at localhost:8000
11. `CTRL + C` will stop the server

```bash
python manage.py dumpdata bikes blog contactus > ./data/fixtures.json 
```


## clean install
pull repository
python3 -m venv venv 
pip3 install -U virtualenv        
activate venv (virtual enviroment)
pip install -r requirements.txt  
python manage.py loaddata ./data/aifixtures.json (location of the json file)
python manage.py makemigrations bikes contactus blogs
python manage.py migrate      
python manage.py showmigrations  (check migrations ahve been made)
python manage.py createsuperuser (admin user creation)
python manage.py runserver     