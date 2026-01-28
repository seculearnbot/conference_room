# credential.py
import os

secret_key = os.environ.get('SECRET_KEY', 'development-secret-key-123')
student_file_path = "static/storage/student/"
file_path = "static/storage/teacher/"
GOOGLE_CLIENT_ID = "1050801722055-btcvqar75jhdt6shnop5esohpj5avd5c.apps.googleusercontent.com"

# PostgreSQL Configuration (از اطلاعات شما)
host = "dpg-d5sl1bn5r7bs73b3il50-a.virginia-postgres.render.com"
port = 5432
user = "daneshclass_db_user"
password = "fCE7pGDPy1NlpbDsvRkcsiVkD7XEJaT3"
databasename = "daneshclass_db"
