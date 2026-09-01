# Data Engineering, Relational Database Systems & Analytics Lab

A centralized repository containing end-to-end data pipelines, relational database architectures, and analytical SQL engines built with Python, SQLite, and Pandas.

---

## 🏛️ Repository Architecture

```text
├── OLISTs/                                # Brazilian E-Commerce Analytics Engine
│   ├── data/raw/                          # Source datasets (CSVs)
│   ├── database/                          # Schema definitions (schema.sql) & SQLite instances
│   ├── src/                               # ETL pipelines & modular database connection interfaces
│   │   ├── load_database.py               # Robust CSV-to-SQLite automated ingestion pipeline
│   │   └── database.py                    # Connection handling & SQL runner utility
│   ├── notebooks/                         # Analytical query execution notebooks
│   └── exercises_solutions/               # Advanced relational challenge sets & solution keys
│
├── SQL Assignments and Solutions/         # Core SQL & Database Engineering Practice
│   ├── data/                              # Practice datasets & CSV generators
│   ├── ecommerce.sql                      # DDL/DML transactional schemas
│   ├── generate_dataset.py                # Synthetic dataset generation scripts
│   └── *.ipynb                            # Analytical exploration, joins & subqueries
│
└── Python Assignments and Solutions/      # Python Automation & Processing Modules
    └── *.py / *.ipynb                     # Core logic, algorithms, and automated workflows
```

---

## 🚀 Key Modules & Capabilities

### 1. Enterprise E-Commerce Relational Engine (`OLISTs/`)
- **Schema Design & Data Modeling**: Normalized multi-table relational schema covering customers, orders, order items, products, sellers, payments, reviews, geolocation, and translations.
- **Automated Ingestion Pipeline**: High-throughput Python ETL script enforcing foreign-key integrity, handling null-value standardization, and batch-inserting hundreds of thousands of records.
- **Advanced Query Engine**: Structured analytical SQL workflows covering multi-table `JOIN` operations, correlated/non-correlated subqueries, set operations (`UNION`, `INTERSECT`, `EXCEPT`), and windowed aggregations.

### 2. Relational Database Engineering (`SQL Assignments and Solutions/`)
- Relational schema modeling and constraints (`PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `UNIQUE`).
- Performance tuning, indexing strategies, and logical query processing analysis (`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`).
- Integrated analytics combining SQLite and Pandas for fast data retrieval and reporting.

### 3. Data Processing & Automation (`Python Assignments and Solutions/`)
- Modular Python utilities for file handling, data sanitization, and workflow automation.
- Data structures and computational problem-solving for data manipulation.

---

## 🛠️ Technology Stack

- **Database**: SQLite3 (Foreign Keys enabled, ACID compliant)
- **Programming & Scripting**: Python 3.11+
- **Data Manipulation & Analysis**: Pandas, NumPy
- **Environment**: Jupyter Notebooks, Visual Studio Code / IDE

---

## ⚡ Quickstart & Setup

### 1. Initialize Database & Run ETL Pipeline
To build and populate the `olist.db` relational database from raw CSV sources:

```bash
python OLISTs/src/load_database.py
```

### 2. Querying via Python / Jupyter
Interact with the database using the shared interface:

```python
import sys
sys.path.append("../src")

from database import run_sql

# Execute analytical query
df = run_sql("""
    SELECT 
        c.customer_state,
        COUNT(o.order_id) AS total_orders,
        ROUND(SUM(p.payment_value), 2) AS total_revenue
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_payments p ON o.order_id = p.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_state
    ORDER BY total_revenue DESC
    LIMIT 10;
""")

print(df)