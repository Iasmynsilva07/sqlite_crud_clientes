from database import connect, TABLE_NAME

def insert_customer(name, weight):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)',
            (name, weight)
        )
        conn.commit()

def list_customers():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        return cursor.fetchall()

def get_customer_by_id(customer_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = ?', (customer_id,))
        return cursor.fetchone()

def delete_customer(customer_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = ?', (customer_id,))
        conn.commit()