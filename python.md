from pathlib import Path

project = Path("/mnt/data/OLISTs")
exercises = project / "exercises"
solutions = project / "solutions"
exercises.mkdir(parents=True, exist_ok=True)
solutions.mkdir(parents=True, exist_ok=True)

questions = r"""# Olist SQL — Week 2 Progressive Examination

**Database:** `OLISTs/database/olist.db`  
**Dataset:** Brazilian Olist e-commerce dataset  
**Level:** CS50 SQL Week 2 → early intermediate  
**Rule:** Solve each question yourself before looking at the separate answer key.

## How to use this

Run each SQL query against the existing `olist.db`.

You are expected to write the SQL yourself. The questions deliberately progress from one concept to combinations of two or three concepts.

---

# Part I — JOIN Foundations

## 1. INNER JOIN — Orders and Customers

Return the following for the first 20 orders:

- `order_id`
- `customer_id`
- `customer_city`
- `customer_state`
- `order_status`

Join `orders` to `customers` using the appropriate key.

**Concept:** `INNER JOIN`

---

## 2. INNER JOIN — Products and Order Items

Return:

- `order_id`
- `product_id`
- `product_category_name`
- `price`

Join `order_items` to `products`.

Return 20 rows.

**Concept:** `INNER JOIN`

---

## 3. LEFT JOIN — Customers With and Without Orders

Return every customer and their order ID.

Show:

- `customer_id`
- `customer_city`
- `customer_state`
- `order_id`

Use a `LEFT JOIN` so that customers who never placed an order are still included.

**Concept:** `LEFT JOIN`

---

## 4. RIGHT JOIN — Understand the Direction

Rewrite Question 3 using a `RIGHT JOIN` instead of a `LEFT JOIN`.

The result should represent the same relationship.

**Concept:** `RIGHT JOIN` vs `LEFT JOIN`

**Hint:** Think carefully about which table must be on which side of the join.

---

# Part II — GROUP BY, HAVING, WHERE, ORDER BY

## 5. Count Orders by Status

Return each `order_status` and the number of orders with that status.

Sort from the most common status to the least common status.

**Concepts:** `GROUP BY`, aggregate function, `ORDER BY`

---

## 6. Customers With More Than One Order

Find customers who placed more than one order.

Return:

- `customer_id`
- number of orders

Only return customers with more than one order.

**Concepts:** `GROUP BY`, `HAVING`

---

## 7. WHERE vs HAVING

Find the number of delivered orders for each customer.

Only consider orders whose status is `delivered`.

Return customers with at least 2 delivered orders.

Return:

- `customer_id`
- delivered order count

**Concepts:** `WHERE` + `GROUP BY` + `HAVING`

---

## 8. Average Product Price by Category

Return each product category and its average product price.

Only include categories whose average product price is greater than 100.

Sort from highest average price to lowest.

**Concepts:** `GROUP BY`, `HAVING`, `ORDER BY`

---

# Part III — Basic Subqueries

## 9. Non-Correlated Subquery — Above-Average Product Price

Find products whose price is greater than the average price of **all products**.

Return:

- `product_id`
- `product_category_name`
- `price`

Sort from most expensive to least expensive.

**Concept:** non-correlated subquery

---

## 10. Subquery with IN

Find all customers who placed at least one order.

Use a subquery with `IN`.

Return:

- `customer_id`
- `customer_city`
- `customer_state`

**Concept:** `IN` + subquery

---

## 11. Subquery with EXISTS

Repeat Question 10, but this time use `EXISTS` instead of `IN`.

Return the same customer information.

**Concept:** `EXISTS` + subquery

---

## 12. Correlated Subquery

Find products whose price is greater than the average price of products in their **own category**.

Return:

- `product_id`
- `product_category_name`
- `price`

**Concept:** correlated subquery

**Hint:** The inner query must refer to the category of the current outer product.

---

# Part IV — Set Operations

## 13. UNION

Create one list containing:

1. customer cities
2. seller cities

Return one column called `city`.

Remove duplicates.

Sort alphabetically.

**Concept:** `UNION`

---

## 14. UNION ALL

Repeat Question 13 using `UNION ALL`.

Do not remove duplicates.

Observe the difference in the number of rows compared with Question 13.

**Concept:** `UNION ALL`

---

## 15. INTERSECT

Find cities that appear in both:

- the customer table
- the seller table

Return one column called `city`.

Sort alphabetically.

**Concept:** `INTERSECT`

---

## 16. EXCEPT

Find cities that appear among customers but do not appear among sellers.

Return one column called `city`.

Sort alphabetically.

**Concept:** `EXCEPT`

---

# Part V — Outer Joins and NULL

## 17. Customers Without Orders

Find customers who have never placed an order.

Use a `LEFT JOIN`.

Return:

- `customer_id`
- `customer_city`
- `customer_state`

**Do not use a subquery.**

**Concepts:** `LEFT JOIN`, `NULL`, filtering unmatched rows

---

## 18. Products That Have Never Been Ordered

Find products that do not appear in `order_items`.

Return:

- `product_id`
- `product_category_name`

Use a `LEFT JOIN`.

**Concepts:** `LEFT JOIN`, `NULL`

---

## 19. FULL OUTER JOIN — Understand Unmatched Rows

Create a simple comparison between customer cities and seller cities using a `FULL OUTER JOIN`.

Return:

- customer city
- seller city

You are not required to produce a meaningful business report. The purpose is to observe what happens when rows exist on one side but not the other.

**Concept:** `FULL OUTER JOIN`

---

# Part VI — NATURAL JOIN

## 20. NATURAL JOIN — Why It Can Be Dangerous

Use a `NATURAL JOIN` between two suitable Olist tables that share a column name.

Then write the equivalent explicit `JOIN ... ON ...` query.

Compare the results.

In your answer, explain:

1. Which columns SQLite used automatically.
2. Why explicitly naming the join condition is safer in production SQL.
3. What could happen if a new column with the same name were later added to both tables.

**Concept:** `NATURAL JOIN`, implicit join keys, maintainability risk

---

# Part VII — Logical Query Processing

## 21. Explain the Processing Order

Consider:

```sql
SELECT
    c.customer_state,
    COUNT(*) AS order_count
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
HAVING COUNT(*) >= 1000
ORDER BY order_count DESC
LIMIT 5;