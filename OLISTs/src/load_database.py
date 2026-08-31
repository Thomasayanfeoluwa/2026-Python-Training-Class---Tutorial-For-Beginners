import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "raw"
DB_DIR = BASE_DIR / "database"

DB_PATH = DB_DIR / "olist.db"
SCHEMA_PATH = DB_DIR / "schema.sql"


def load_csv(connection, table_name, csv_file):
    csv_path = DATA_DIR / csv_file

    print(f"Loading {csv_file}...")

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        columns = reader.fieldnames

        if not columns:
            raise ValueError(f"No columns found in {csv_file}")

        column_names = ", ".join(f'"{column}"' for column in columns)
        placeholders = ", ".join("?" for _ in columns)

        sql = f"""
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders})
        """

        rows = []

        for row in reader:
            values = []

            for column in columns:
                value = row[column]

                if value == "":
                    values.append(None)
                else:
                    values.append(value)

            rows.append(values)

        connection.executemany(sql, rows)

    print(f"Loaded {len(rows):,} rows into {table_name}")


def main():

    DB_DIR.mkdir(exist_ok=True)

    if DB_PATH.exists():
        DB_PATH.unlink()

    connection = sqlite3.connect(DB_PATH)

    try:

        connection.execute("PRAGMA foreign_keys = ON;")

        with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
            schema = file.read()

        connection.executescript(schema)

        # ----------------------------------------------------
        # IMPORTANT:
        # Load parent tables before child tables because of
        # foreign-key constraints.
        # ----------------------------------------------------

        load_csv(
            connection,
            "customers",
            "olist_customers_dataset.csv"
        )

        load_csv(
            connection,
            "sellers",
            "olist_sellers_dataset.csv"
        )

        load_csv(
            connection,
            "products",
            "olist_products_dataset.csv"
        )

        load_csv(
            connection,
            "product_category_name_translation",
            "product_category_name_translation.csv"
        )

        load_csv(
            connection,
            "orders",
            "olist_orders_dataset.csv"
        )

        load_csv(
            connection,
            "order_items",
            "olist_order_items_dataset.csv"
        )

        load_csv(
            connection,
            "order_payments",
            "olist_order_payments_dataset.csv"
        )

        load_csv(
            connection,
            "order_reviews",
            "olist_order_reviews_dataset.csv"
        )

        load_csv(
            connection,
            "geolocation",
            "olist_geolocation_dataset.csv"
        )

        connection.commit()

        print()
        print("=" * 60)
        print("DATABASE CREATED SUCCESSFULLY")
        print("=" * 60)
        print(f"Database: {DB_PATH}")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    main()