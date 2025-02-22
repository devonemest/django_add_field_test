import psycopg2
from psycopg2 import sql
import time

db_config = {
    'dbname': 'test',
    'user': 'postgres',
    'password': 'toor',
    'host': 'localhost',
    'port': '5432'
}

batch_size = 1000

def update_rows():
    updated_rows_total = 0
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        while True:
            update_query = sql.SQL("""
                UPDATE dummies 
                SET new_field_test = '1' 
                WHERE id IN (SELECT id FROM dummies WHERE new_field_test IS NULL LIMIT %s FOR UPDATE SKIP LOCKED)
            """)
            cursor.execute(update_query, (batch_size,))
            updated_rows = cursor.rowcount

            conn.commit()
            updated_rows_total += updated_rows
            print(f"Обновлено строк: {updated_rows_total}")

            if updated_rows < batch_size:
                break

    except Exception as e:
        print(e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print('End')


if __name__ == '__main__':
    time_start = time.time()
    update_rows()
    time_end = time.time()
    print(time_end-time_start)
