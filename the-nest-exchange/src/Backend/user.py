from database_connect import connect_database

def create_user(id, username, role, email, first_name, last_name, phone):
   try:
        conn = connect_database()
        cursor = conn.cursor()
        query = "INSERT INTO Users (id, username, role, email, first_name, last_name, phone,) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (id, username, role, email, first_name, last_name, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return "User created successfully"
   except Exception as e:
       print(f"Error: {e}")


def delete_user(id):
    try:
        conn = connect_database()
        cursor = conn.cursor()
        query = "DELETE FROM Users WHERE id = %s"
        cursor.execute(query,(id))
        conn.commit()
        cursor.close()
        conn.close()
        return "User deleted successfully"
    except Exception as e:
        print(f"Eroror: {e}")
