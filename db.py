import psycopg2
import credential

def get_connection():
    """Create connection to PostgreSQL database"""
    return psycopg2.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        database=credential.databasename
    )

def login_teacher(email, password):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT password FROM teacher WHERE email = %s"
            curr.execute(sql, (email,))
            output = curr.fetchone()
            if output:
                if password == output[0]:
                    return 1  # correct
                else:
                    return 0  # incorrect
            return -1  # does not exist
    except Exception as e:
        print(e)
        return -1
    finally:
        conn.close()

def login_student(email, password):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT password FROM student WHERE email = %s"
            curr.execute(sql, (email,))
            output = curr.fetchone()
            if output:
                if password == output[0]:
                    return 1  # correct
                else:
                    return 0  # incorrect
            return -1  # does not exist
    except Exception as e:
        print(e)
        return -1
    finally:
        conn.close()

def getStuId(email):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT student_id FROM student WHERE email = %s"
            curr.execute(sql, (email,))
            output = curr.fetchone()
            return output[0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def submitAss(student_id, content_id, submission_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO submission (student_id, content_id, submission_id) VALUES (%s, %s, %s)"
            curr.execute(sql, (student_id, content_id, submission_id))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def signup_teacher(name, email, password, phone_no, teacher_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO teacher (name, email, password, phone_no, teacher_id) VALUES (%s, %s, %s, %s, %s)"
            curr.execute(sql, (name, email, password, phone_no, teacher_id))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def signup_student(name, email, password, phone_no, student_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO student (name, email, password, phone_no, student_id) VALUES (%s, %s, %s, %s, %s)"
            curr.execute(sql, (name, email, password, phone_no, student_id))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def check_teach_key(key):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT name FROM teacher WHERE teacher_id = %s"
            curr.execute(sql, (key,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def check_stud_key(key):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT name FROM student WHERE student_id = %s"
            curr.execute(sql, (key,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def get_teacher_id(mail):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT teacher_id FROM teacher WHERE email = %s"
            curr.execute(sql, (mail,))
            output = curr.fetchall()
            return output[0][0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def get_student_id(mail):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT student_id FROM student WHERE email = %s"
            curr.execute(sql, (mail,))
            output = curr.fetchall()
            return output[0][0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def check_class_id(code):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_name FROM class_table WHERE class_id = %s"
            curr.execute(sql, (code,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def create_class(class_name, class_id, class_link, teacher_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO class_table (class_name, class_id, class_link, teacher_id) VALUES (%s, %s, %s, %s)"
            curr.execute(sql, (class_name, class_id, class_link, teacher_id))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def join_class(student_id, class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO stud_classroom (student_id, class_id) VALUES (%s, %s)"
            curr.execute(sql, (student_id, class_id))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def check_teach_mail(email):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT name FROM teacher WHERE email = %s"
            curr.execute(sql, (email,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def check_stud_mail(email):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT name FROM student WHERE email = %s"
            curr.execute(sql, (email,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def get_teach_classes(teacher_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_name, class_id, class_link FROM class_table WHERE teacher_id = %s ORDER BY creation_date DESC"
            curr.execute(sql, (teacher_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def joined_classes_info(class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = """SELECT C.class_name, C.class_link, C.class_id, T.name 
                     FROM class_table C 
                     JOIN teacher T ON C.teacher_id = T.teacher_id 
                     WHERE C.class_id = %s 
                     ORDER BY C.creation_date"""
            curr.execute(sql, (class_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def check_class_name(class_name, teacher_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_id FROM class_table WHERE class_name = %s AND teacher_id = %s"
            curr.execute(sql, (class_name, teacher_id))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def already_joined_class(student_id, class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT * FROM stud_classroom WHERE student_id = %s AND class_id = %s"
            curr.execute(sql, (student_id, class_id))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def get_joined_classes(student_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_id FROM stud_classroom WHERE student_id = %s"
            curr.execute(sql, (student_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def get_class_data(class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT content_heading, content_id, descript, upload_time FROM class_content WHERE class_id = %s ORDER BY upload_time DESC"
            curr.execute(sql, (class_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def get_teach_partiular_subject(class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_name, class_link FROM class_table WHERE class_id = %s"
            curr.execute(sql, (class_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def check_content_id(content_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_id FROM class_content WHERE content_id = %s"
            curr.execute(sql, (content_id,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def add_class_content(class_id, content_id, content_heading, descript, max_score, due_date):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            if max_score == "default" and due_date == "default":
                sql = "INSERT INTO class_content (class_id, content_id, content_heading, descript) VALUES (%s, %s, %s, %s)"
                curr.execute(sql, (class_id, content_id, content_heading, descript))
            elif max_score == "default":
                sql = "INSERT INTO class_content (class_id, content_id, content_heading, descript, due_date) VALUES (%s, %s, %s, %s, %s)"
                curr.execute(sql, (class_id, content_id, content_heading, descript, due_date))
            elif due_date == "default":
                sql = "INSERT INTO class_content (class_id, content_id, content_heading, descript, max_score) VALUES (%s, %s, %s, %s, %s)"
                curr.execute(sql, (class_id, content_id, content_heading, descript, max_score))
            else:
                sql = "INSERT INTO class_content (class_id, content_id, content_heading, descript, max_score, due_date) VALUES (%s, %s, %s, %s, %s, %s)"
                curr.execute(sql, (class_id, content_id, content_heading, descript, max_score, due_date))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def add_content_storage_link(content_id, links):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO content_storage_links (content_id, links) VALUES (%s, %s)"
            curr.execute(sql, (content_id, links))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def add_content_storage_files(content_id, content_links):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO content_storage (content_id, content_links) VALUES (%s, %s)"
            curr.execute(sql, (content_id, content_links))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def add_student_storage_files(submission_id, submission_link):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "INSERT INTO submission_storage (submission_id, submission_link) VALUES (%s, %s)"
            curr.execute(sql, (submission_id, submission_link))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def is_assignment_submitted(submission_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT submit_time FROM submission WHERE submission_id = %s"
            curr.execute(sql, (submission_id,))
            output = curr.fetchall()
            return len(output) > 0
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def get_assignment_details(content_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_id, content_heading, descript, upload_time, max_score, due_date FROM class_content WHERE content_id = %s"
            curr.execute(sql, (content_id,))
            output = curr.fetchall()
            return output if output else False
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def get_content_specific_data(content_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT class_id, content_heading, descript, due_date FROM class_content WHERE content_id = %s"
            curr.execute(sql, (content_id,))
            output = curr.fetchall()
            return output[0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def get_total_students(class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT COUNT(*) FROM stud_classroom WHERE class_id = %s"
            curr.execute(sql, (class_id,))
            output = curr.fetchall()
            return output[0][0] if output else 0
    except Exception as e:
        print(e)
        return 0
    finally:
        conn.close()

def get_smart_students(content_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT COUNT(*) FROM submission WHERE content_id = %s"
            curr.execute(sql, (content_id,))
            output = curr.fetchall()
            return output[0][0] if output else 0
    except Exception as e:
        print(e)
        return 0
    finally:
        conn.close()

def get_data_smart_students(content_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = """SELECT S.name, C.score, C.submit_time 
                     FROM student S 
                     JOIN submission C ON S.student_id = C.student_id 
                     WHERE content_id = %s"""
            curr.execute(sql, (content_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def get_Max_marks(content_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT max_score FROM class_content WHERE content_id = %s"
            curr.execute(sql, (content_id,))
            output = curr.fetchall()
            return output[0][0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def get_teacher_id_class_id(class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT teacher_id FROM class_table WHERE class_id = %s"
            curr.execute(sql, (class_id,))
            output = curr.fetchall()
            return output[0][0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def get_teacher_name(teacher_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT name FROM teacher WHERE teacher_id = %s"
            curr.execute(sql, (teacher_id,))
            output = curr.fetchall()
            return output[0][0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def get_students_id(class_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT student_id FROM stud_classroom WHERE class_id = %s"
            curr.execute(sql, (class_id,))
            output = curr.fetchall()
            return output
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

def get_student_name(student_id):
    conn = get_connection()
    try:
        with conn.cursor() as curr:
            sql = "SELECT name FROM student WHERE student_id = %s"
            curr.execute(sql, (student_id,))
            output = curr.fetchall()
            return output[0][0] if output else None
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()
