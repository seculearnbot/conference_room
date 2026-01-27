
import os


secret_key = os.environ.get('SECRET_KEY', 'development-secret-key-123')

student_file_path = "static/storage/student/"
file_path = "static/storage/teacher/"


GOOGLE_CLIENT_ID = "1050801722055-btcvqar75jhdt6shnop5esohpj5avd5c.apps.googleusercontent.com"


host = os.environ.get('DB_HOST', 'localhost')
port = int(os.environ.get('DB_PORT', 3306)) 
user = os.environ.get('DB_USER', 'root')
password = os.environ.get('DB_PASSWORD', '')
databasename = os.environ.get('DB_NAME', 'conference_room')  
