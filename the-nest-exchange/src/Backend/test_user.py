from database_connect import connect_database
from user import create_user, delete_user

if __name__ == "__main__":
    try:
        conn = connect_database()
        create_user("1", "john1", "adlhfadhfoadshfdoush", "admin", "fakeemail", "john", "doe", "1111111111")
        delete_user("1")
        conn.close()
        print("Created and deleted user successfully")
    except: 
        conn.close()
        print("Errors")
