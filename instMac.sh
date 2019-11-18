cd esv3
pip3 install -r requirements.txt
pip3 install --pre xhtml2pdf
virtualenv virtenv 
source virtenv/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver