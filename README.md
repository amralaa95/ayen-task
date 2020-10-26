# ayen-task

Application can store pdf and power point files for each user and can search with text in all files for that user
only extinsions .pdf and .pttx
## Building local

virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements
python manage.py migrate
python manage.py runserver
