from pathlib import Path

import numpy as np
import pandas as pd


RANDOM_SEED = 42
NUMBER_OF_ROWS = 1000


def create_ecommerce_dataset(number_of_rows=NUMBER_OF_ROWS, seed=RANDOM_SEED):
    """Create a reproducible synthetic e-commerce order dataset."""
    rng = np.random.default_rng(seed)

    categories = np.array([
        "Electronics",
        "Home & Kitchen",
        "Clothing",
        "Books",
        "Sports",
        "Beauty",
    ])
    products = np.array([
        "Wireless Headphones",
        "Smart Watch",
        "Laptop Stand",
        "Coffee Maker",
        "Running Shoes",
        "Cotton T-Shirt",
        "Python Programming Book",
        "Yoga Mat",
        "Face Moisturizer",
        "Bluetooth Speaker",
    ])
    cities = np.array(["Lagos", "Abuja", "Ibadan", "Kano", "Port Harcourt"])
    payment_methods = np.array(["Card", "Bank Transfer", "Cash on Delivery", "Wallet"])
    statuses = np.array(["Delivered", "Shipped", "Processing", "Cancelled"])

    quantity = rng.integers(1, 6, size=number_of_rows)
    unit_price = rng.uniform(10, 500, size=number_of_rows).round(2)
    discount_percent = rng.choice([0, 5, 10, 15, 20], size=number_of_rows)
    total_amount = (quantity * unit_price * (1 - discount_percent / 100)).round(2)

    dataset = pd.DataFrame({
        "order_id": np.arange(1, number_of_rows + 1),
        "customer_id": rng.integers(1001, 1251, size=number_of_rows),
        "order_date": pd.Timestamp("2025-01-01") + pd.to_timedelta(
            rng.integers(0, 365, size=number_of_rows), unit="D"
        ),
        "product": rng.choice(products, size=number_of_rows),
        "category": rng.choice(categories, size=number_of_rows),
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_percent": discount_percent,
        "total_amount": total_amount,
        "city": rng.choice(cities, size=number_of_rows),
        "payment_method": rng.choice(payment_methods, size=number_of_rows),
        "order_status": rng.choice(statuses, size=number_of_rows, p=[0.65, 0.15, 0.15, 0.05]),
    })

    return dataset.sort_values("order_date").reset_index(drop=True)


def main():
    output_directory = Path(__file__).parent / "data"
    output_directory.mkdir(exist_ok=True)

    output_path = output_directory / "ecommerce_dataset.csv"
    dataset = create_ecommerce_dataset()
    dataset.to_csv(output_path, index=False)

    print(f"Created {len(dataset):,} rows at: {output_path}")
    print(dataset.head())


if __name__ == "__main__":
    main()
