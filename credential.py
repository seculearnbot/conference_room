
import os


secret_key = os.environ.get('SECRET_KEY', 'default-secret-key-for-development')


student_file_path = "static/storage/student/"
file_path = "static/storage/teacher/"


database_config = {
    "host": os.environ.get('DB_HOST', 'localhost'),
    "user": os.environ.get('DB_USER', 'root'),
    "password": os.environ.get('DB_PASSWORD', ''),
    "database": os.environ.get('DB_NAME', 'conference_room')
}


GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '1050801722055-btcvqar75jhdt6shnop5esohpj5avd5c.apps.googleusercontent.com')
