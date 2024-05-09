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