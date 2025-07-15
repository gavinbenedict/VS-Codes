import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='stock_db'
)


cursor = conn.cursor()


def create_item(name, quantity, price):
    sql = "INSERT INTO stock (item_name, quantity, price_per_unit) VALUES (%s, %s, %s)"
    values = (name, quantity, price)
    cursor.execute(sql, values)
    conn.commit()
    print("Item added successfully!")


def read_items():
    sql = "SELECT * FROM stock"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("Stock List:")
    for row in records:
        print(row)


def update_item(item_id, quantity, price):
    sql = "UPDATE stock SET quantity = %s, price_per_unit = %s WHERE id = %s"
    values = (quantity, price, item_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Item updated successfully!")


def delete_item(item_id):
    sql = "DELETE FROM stock WHERE id = %s"
    value = (item_id,)
    cursor.execute(sql, value)
    conn.commit()
    print("Item deleted successfully!")


create_item("Keyboard", 20, 750.00)
create_item("Mouse", 50, 300.00)
read_items()

update_item(1, 25, 780.00)
read_items()

delete_item(2)
read_items()


cursor.close()
conn.close()
