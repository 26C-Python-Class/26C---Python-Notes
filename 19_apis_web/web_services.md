# Applying Web Services: From Concept to Code

## 1. The Developer’s Workflow
Professional API integration isn't "guess and check." It follows a specific four-step lifecycle to ensure reliability and security.

1.  **Discovery (Read the Docs):** Every reputable API has documentation (often using **OpenAPI/Swagger**). This tells you the URLs, required headers, and expected JSON structure.
2.  **Exploration (Test with Tools):** Before writing Python code, use a GUI like **Postman** or **Insomnia**. If the request fails in Postman, the problem is with the server or your credentials.
3.  **Implementation (Write the Script):** Use a library like `requests` to automate the interaction.
4.  **Resilience (Error Handling):** Use `try/except` blocks to handle "The Internet being The Internet" (Wi-Fi dropping, server timeouts, etc.).

---

## 2. Essential Tooling: Postman
Postman is a "Headless Browser." It lets you see exactly what the server is sending back, including hidden headers and cookies.



**Why use it first?** If your Python code throws an error, you don't know if the bug is in your **logic** or the **server's response**. Postman isolates the variable. If it works in Postman but fails in Python, the bug is in your code.

---

## 3. Consuming Services (The Client Side)
In Python, we use the `requests` library. It is much more "human-readable" than the built-in `urllib`.

### Example A: Fetching Data (GET)
*Scenario: Checking the current price of Bitcoin from a public API.*

```python
import requests

# 1. The Endpoint
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    # 2. Make the request
    response = requests.get(url, timeout=5)
    
    # 3. Check status (200 = Success)
    response.raise_for_status() # Automatically raises an error for 4xx/5xx codes
    
    # 4. Parse the JSON data
    data = response.json()
    usd_rate = data['bpi']['USD']['rate']
    print(f"Current Bitcoin Price: ${usd_rate}")

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except Exception as e:
    print(f"Connection Error: {e}")
```

### Example B: Sending Data (POST)
*Scenario: Submitting a new "Ticket" to a Customer Support system.*

```python
import requests

url = "https://api.supportsystem.com/v1/tickets"

# 1. The Payload (The Data)
ticket_data = {
    "title": "Cannot login",
    "priority": "High",
    "description": "User 'jdoe' receives a 401 error on login page."
}

# 2. Headers (Metadata)
# We tell the server: "I am sending JSON, and here is my key."
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_SECRET_TOKEN"
}

# 3. Execution
response = requests.post(url, json=ticket_data, headers=headers)

if response.status_code == 201:
    print("Success! Ticket Created.")
else:
    print(f"Failed: {response.status_code}")
```

---

## 4. Authentication & Security
Public APIs are rare. Most require you to prove who you are.

* **API Keys:** A unique string identifying your "app." Often passed as a query parameter (e.g., `?api_key=xyz`).
* **Bearer Tokens (OAuth 2.0):** The modern standard. It's like a "digital wristband." You send it in the header: `Authorization: Bearer <token>`.

> ### The Golden Rule of Security
> **NEVER** hardcode keys in your script. If you push that code to GitHub, hackers will find it in seconds.
> **The Solution:** Use environment variables.
> ```python
> import os
> api_key = os.getenv('MY_API_KEY') # Safer approach
> ```

---

## 5. Building a Service (The Server Side)
To understand how a client "consumes," you must see how a server "provides." We'll use **Flask**, a lightweight Python web framework.



```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# A "Resource" for books
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books_db)

@app.route('/api/books', methods=['POST'])
def add_book():
    new_data = request.get_json()
    books_db.append(new_data)
    return jsonify({"message": "Book added!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 6. Troubleshooting Common Errors

| Status Code | Name | Meaning | Fix |
| :--- | :--- | :--- | :--- |
| **200/201** | **Success** | Everything worked. | Keep going! |
| **400** | **Bad Request** | Syntax error in your JSON. | Validate your JSON format. |
| **401** | **Unauthorized** | Missing or wrong API Key. | Check your `Authorization` header. |
| **403** | **Forbidden** | Valid key, but no permission. | Check if your account is "Free" vs "Pro." |
| **404** | **Not Found** | URL is misspelled. | Check the endpoint path. |
| **429** | **Too Many Requests** | You are hitting the API too fast. | Add `time.sleep()` to your code. |
| **500** | **Server Error** | The server's code crashed. | Wait and try again later; it's not you. |
