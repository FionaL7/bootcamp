import sqlite3
import os
from contextlib import contextmanager
import csv
import argparse

print(f"📁 Creating/connecting to: {os.path.abspath('store.db')}")

DB_NAME = "store.db"


class Product:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self._create_table()

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def _create_table(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            );
        """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    );""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                        id INTEGER PRIMARY KEY,
                        customer TEXT NOT NULL,
                        date DATETIME NOT NULL       
                               );""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS order_details (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);""")
                conn.commit()

        except Exception as e:
            print(f"❌ Error creating table: {e}")

    def add_product(self, name, price, category_id=None):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO products (name, price, category_id) VALUES (?, ?, ?);", (name, price, category_id))
                conn.commit()
                print(f"✅ Product added: {name} (${price}) {category_id}")
        except Exception as e:
            print(f"❌ Error adding product: {e}")

    def update_price(self, product_id, new_price):
        try:
            with self._connect as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE products SET price = ? WHERE id = ?;", (new_price, product_id))
                conn.commit()
                if cursor.rowcount == 0:
                    print(f"⚠️ No product found with ID {product_id}")
                else:
                    print(
                        f"✅ Updated product ID {product_id} to new price: ${new_price}")
        except Exception as e:
            print(f"❌ Error updating product: {e}")

    def delete_product(self, product_id):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM products WHERE id = ?;", (product_id,))
                conn.commit()
                if cursor.rowcount == 0:
                    print(f"⚠️ No product found with ID {product_id}")
                else:
                    print(f"🗑️ Product with ID {product_id} deleted.")
        except Exception as e:
            print(f"❌ Error deleting product: {e}")

    def list_products(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products;")
                products = cursor.fetchall()
                if products:
                    print("\n📋 Product List:")
                    for p in products:
                        print(
                            f"ID: {p[0]} | Name: {p[1]} | Price: ${p[2]:.2f} | Category ID: {p[3]}")
                else:
                    print("📭 No products found.")
        except Exception as e:
            print(f"❌ Error fetching products: {e}")

    def search(self, name_fragment):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM products WHERE name LIKE ?;", (f"%{name_fragment}%",))
                results = cursor.fetchall(
                )
                print(f"\n🔍 Search results for '{name_fragment}':")
                for r in results:
                    print(
                        f"ID: {r[0]} | Name: {r[1]} | Price: ${r[2]:.2f} | Category ID: {r[3]}")
        except Exception as e:
            print(f"❌ Error searching products: {e}")

    def list_with_categories(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""SELECT p.id, p.name, p.price, c.name
                               FROM products p
                               LEFT JOIN categories c ON p.category_id = c.id;""")
                results = cursor.fetchall()
                print("\n Products with Categories: ")
                for r in results:
                    cat = r[3] if r[3] else "Uncategorized"
                    print(
                        f"ID: {r[0]} | Name: {r[1]} | Price: ${r[2]:.2f} | Category: {cat}")
        except Exception as e:
            print(f"❌ Error fetching join data: {e}")

    def _validate_product(self, name, price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

    def add_category(self, name):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO categories (name) VALUES (?);", (name,))
                print(f"📁 Category added: {name}")
        except Exception as e:
            print(f"❌ Error adding category: {e}")

    def total(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT SUM(price) FROM products;")
                total = cursor.fetchone()[0]
                return total if total else 0.0
        except Exception as e:
            print(f"Error calculating total value: {e}")
            return 0.0

    def save_to_csv(self, filename="products_export.csv"):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products;")
                rows = cursor.fetchall()
                with open(filename, mode="w", newline="")as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Price", "Category  _ID"])
                    writer.writerows(rows)
            print(f"📁 Exported {len(rows)} rows to {filename}")
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

    def batch_insert(self, product_list):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.executemany("INSERT INTO products(name, price, category_id) VALUES (?, ?, ?);",
                                   product_list)
            print(f"✅ Inserted {len(product_list)} products in batch.")
        except Exception as e:
            print(f"❌ Error in batch insertion.Rolled back. Error: {e}")

    def update_order_and_details(self, order_id, new_customer, details_updates):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE orders SET customer = ? WHERE id = ?;",
                               (new_customer, order_id))
                for detail_id, new_qty in details_updates:
                    cursor.execute("UPDATE order_details SET quantity = ? WHERE id = ? ;",
                                   (new_qty, detail_id))
            print(f"Updated order {order_id} and details successfully.")
        except Exception as e:
            print(f"❌ Transaction failed, rolled back: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export products to CSV")
    parser.add_argument(
        "--csv",
        type=str,
        default="products_export.csv",
        help="Output CSV filename (e.g., myfile.csv)"
    )
    args = parser.parse_args()
    pm = Product()

    # pm.add_category("Electronics")

    # pm.add_product("Laptop", 1200, category_id=1)
    # pm.add_product("Mouse", 25, category_id=1)

    # pm.list_products()

    # pm.update_price(1, 329.99)

    # pm.delete_product(2)

    # pm.list_products()

    # pm.search("lap")

    # pm.list_with_categories()
    # pm.save_to_csv(args.csv)
    # batch = [
    #     ("Keyboard", 45.0, 1),
    #     ("Webcam", 85.5, 1),
    #     ("Chair", 150.0, 2),
    # ]
    # pm.batch_insert(batch)
    pm.update_order_and_details(
        order_id=1, new_customer="Alice", details_updates=[(1, 5), (2, 8)])
