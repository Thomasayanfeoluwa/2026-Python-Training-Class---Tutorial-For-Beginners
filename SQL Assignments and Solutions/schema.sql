PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS support_tickets;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS newsletter_subscribers;
DROP TABLE IF EXISTS vip_customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;


-- =========================================
-- CUSTOMERS
-- =========================================

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    city TEXT NOT NULL
);


INSERT INTO customers (id, name, email, city) VALUES
(1, 'Alice Johnson', 'alice@example.com', 'Lagos'),
(2, 'Bob Smith', 'bob@example.com', 'Abuja'),
(3, 'Carol Williams', 'carol@example.com', 'Lagos'),
(4, 'David Brown', 'david@example.com', 'Ibadan'),
(5, 'Eva Davis', 'eva@example.com', 'Abuja'),
(6, 'Frank Wilson', 'frank@example.com', 'Port Harcourt'),
(7, 'Grace Taylor', 'grace@example.com', 'Lagos'),
(8, 'Henry Moore', 'henry@example.com', 'Kano');


-- =========================================
-- PRODUCTS
-- =========================================

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
);


INSERT INTO products (id, name, category, price, stock) VALUES
(1, 'Laptop Pro', 'Electronics', 1200.00, 8),
(2, 'Wireless Mouse', 'Electronics', 25.00, 50),
(3, 'Mechanical Keyboard', 'Electronics', 90.00, 25),
(4, 'USB-C Hub', 'Electronics', 60.00, 30),
(5, 'Office Chair', 'Furniture', 250.00, 10),
(6, 'Standing Desk', 'Furniture', 450.00, 5),
(7, 'Notebook', 'Stationery', 8.00, 100),
(8, 'Desk Lamp', 'Furniture', 75.00, 20),
(9, 'Pen Set', 'Stationery', 12.00, 80),
(10, 'Monitor', 'Electronics', 300.00, 12);


-- =========================================
-- ORDERS
-- =========================================

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);


INSERT INTO orders (id, customer_id, order_date, status) VALUES
(101, 1, '2026-01-10', 'Delivered'),
(102, 1, '2026-02-15', 'Delivered'),
(103, 2, '2026-02-20', 'Shipped'),
(104, 3, '2026-03-01', 'Delivered'),
(105, 3, '2026-03-12', 'Pending'),
(106, 5, '2026-03-20', 'Delivered'),
(107, 7, '2026-04-02', 'Shipped');


-- =========================================
-- ORDER ITEMS
-- =========================================

CREATE TABLE order_items (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,

    PRIMARY KEY (order_id, product_id),

    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);


INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(101, 1, 1, 1200.00),
(101, 2, 2, 25.00),

(102, 3, 1, 90.00),
(102, 4, 1, 60.00),

(103, 5, 1, 250.00),
(103, 7, 3, 8.00),

(104, 2, 1, 25.00),
(104, 8, 1, 75.00),

(105, 10, 1, 300.00),

(106, 6, 1, 450.00),
(106, 9, 2, 12.00),

(107, 3, 1, 90.00),
(107, 7, 5, 8.00);


-- =========================================
-- REVIEWS
-- =========================================

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),

    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);


INSERT INTO reviews (id, customer_id, product_id, rating) VALUES
(1, 1, 1, 5),
(2, 1, 2, 4),
(3, 2, 5, 4),
(4, 3, 2, 5),
(5, 3, 8, 3),
(6, 5, 6, 5),
(7, 7, 3, 4),
(8, 7, 7, 5);


-- =========================================
-- NEWSLETTER SUBSCRIBERS
-- =========================================

CREATE TABLE newsletter_subscribers (
    customer_id INTEGER PRIMARY KEY,

    FOREIGN KEY (customer_id) REFERENCES customers(id)
);


INSERT INTO newsletter_subscribers (customer_id) VALUES
(1),
(2),
(3),
(4),
(6),
(8);


-- =========================================
-- VIP CUSTOMERS
-- =========================================

CREATE TABLE vip_customers (
    customer_id INTEGER PRIMARY KEY,

    FOREIGN KEY (customer_id) REFERENCES customers(id)
);


INSERT INTO vip_customers (customer_id) VALUES
(1),
(3),
(5),
(7);


-- =========================================
-- SUPPORT TICKETS
-- =========================================

CREATE TABLE support_tickets (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    subject TEXT NOT NULL,
    status TEXT NOT NULL,

    FOREIGN KEY (customer_id) REFERENCES customers(id)
);


INSERT INTO support_tickets (id, customer_id, subject, status) VALUES
(1001, 1, 'Cannot log in', 'Open'),
(1002, 2, 'Late delivery', 'Closed'),
(1003, 3, 'Refund request', 'Open'),
(1004, NULL, 'General product question', 'Open'),
(1005, 8, 'Payment issue', 'Open');