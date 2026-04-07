import sqlite3
import os

db_path = 'c:/Users/harsh/OneDrive/Desktop/AE/TNPSC_Quiz/quiz_app.db'

def inspect_db():
    if not os.path.exists(db_path):
        print("DB does not exist.")
        return
        
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        print('Tables:', tables)
        
        for table in tables:
            t_name = table[0]
            print(f'\nSchema for {t_name}:')
            c.execute(f"PRAGMA table_info({t_name})")
            for col in c.fetchall():
                print(col)
            
        conn.close()
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    inspect_db()
