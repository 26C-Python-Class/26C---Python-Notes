# Module: RESTful Architecture – Designing Scalable Web Systems

This guide introduces the principles of **REST (Representational State Transfer)**, the architectural style that powers the modern web. It provides a structured curriculum for understanding how servers and clients communicate efficiently.

---

## 1. Introduction: What is REST?
**REST** is not a piece of software or a specific programming language. It is an **Architectural Style** defined by Roy Fielding in 2000. 

The goal of REST is to make web systems **Scalable**, **Reliable**, and **Fast** by following a specific set of constraints.

### The Shift: From Verbs to Nouns
In older systems (like RPC), we focused on **Actions (Verbs)**. In REST, we focus on **Resources (Nouns)**.

| RPC Thinking (Actions) | REST Thinking (Resources) |
| :--- | :--- |
| `fetchVehicleData(id)` | `GET /vehicles/101` |
| `addNewEmployee()` | `POST /employees` |
| `removeAllLogs()` | `DELETE /logs` |



---

## 2. The 6 Guiding Constraints
To be truly "RESTful," an API must follow these six rules:

1.  **Client-Server Separation:** The interface (Mobile App/Browser) and the data storage (Server) are independent. You can change your database without breaking your app.
2.  **Statelessness (Crucial):** The server **never** remembers you between requests. Every single request must contain everything the server needs to know (like an Auth Token).
    * *Benefit:* If one server crashes, another can take over instantly because it doesn't need "session memory."
3.  **Cacheability:** Responses must state if they can be saved by the client to save data and speed up loading.
4.  **Layered System:** The client shouldn't know if it’s talking to the final server or a middleman (like a Load Balancer or Security Firewall).
5.  **Uniform Interface:** The system uses a standard language: **HTTP Methods** (GET, POST, etc.) and **URIs** (URLs).
6.  **Code on Demand (Optional):** Servers can send executable code (like JavaScript) to the client.

---

## 3. The Richardson Maturity Model
This is the "Report Card" for APIs. Most professional APIs aim for **Level 2**.

* **Level 0:** One URL for everything (The "Swamp").
* **Level 1:** Individual URLs for different things (e.g., `/products`, `/orders`).
* **Level 2:** Using the correct **HTTP Verbs** (GET for reading, DELETE for removing).
* **Level 3:** **HATEOAS** (The API provides links to "Next Steps," like a website menu).

---

## 4. HTTP Methods & Operations (CRUD)
REST maps your database actions to specific HTTP verbs.



| Verb | Action | SQL | Idempotent? | Real-World Example |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | Read | `SELECT` | **Yes** | View a product page. |
| **POST** | Create | `INSERT` | **No** | Submit a new order. |
| **PUT** | Replace | `UPDATE` | **Yes** | Replace an entire profile. |
| **PATCH** | Update | `UPDATE` | **No** | Change *only* the user's email. |
| **DELETE** | Delete | `DELETE` | **Yes** | Remove an old post. |

> **What is Idempotency?**
> If you click a "DELETE" button 10 times, the result is the same: the item is gone. That is **Idempotent**. If you click "POST" 10 times and get 10 different charges on your credit card, that is **NOT Idempotent**.

---

## 5. Professional Naming & Filtering
A professional API uses clean, logical paths.

### Proper Naming (Nouns)
* ✅ **Good:** `GET /flights/12`
* ❌ **Bad:** `GET /get_flight_details?id=12`

### Hierarchy (Sub-resources)
To show relationships, use slashes:
* `GET /authors/5/books` (Gets all books written by Author #5).

### Filtering & Sorting (Query Parameters)
Don't create new URLs for filters. Use the `?` symbol:
* **Filtering:** `GET /cars?color=red&brand=toyota`
* **Sorting:** `GET /cars?sort=price_asc`
* **Pagination:** `GET /cars?page=1&limit=20`

---

## 6. HTTP Status Codes: The Server's Voice
The server uses 3-digit codes to tell you what happened.

| Code | Meaning | Who's "fault" is it? |
| :--- | :--- | :--- |
| **200 OK** | Everything worked! | Success |
| **201 Created** | New resource made (POST). | Success |
| **400 Bad Request** | Your JSON/Data is wrong. | **Client Error** |
| **401 Unauthorized** | You forgot your password/token. | **Client Error** |
| **404 Not Found** | That URL doesn't exist. | **Client Error** |
| **500 Internal Error** | The Python code crashed. | **Server Error** |
| **503 Unavailable** | Server is down for maintenance. | **Server Error** |

---

### Classroom Challenge:
1.  **The Verb Test:** If you want to change just the "Price" of an item, should you use `PUT` or `PATCH`?
2.  **Naming Drill:** Correct this URL to be RESTful: `/api/v1/deleteUserAccount/99`.
3.  **Status Code Quiz:** A user tries to delete a post that belongs to someone else. Which `4xx` code should you return? (Hint: They are logged in, but don't have permission).
