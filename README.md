# 🚀 Learning FastAPI

## 📘 What is an API?

An **API (Application Programming Interface)** allows two software components to communicate with each other. In the context of web development, APIs typically allow clients (like web or mobile apps) to send HTTP requests to a server and receive responses, such as data or actions performed.

**Example:**
- Client: "Here’s some text, what’s the sentiment?"
- API: "It's Positive, with 99.8% confidence."

---

## ⚡ About FastAPI

**FastAPI** is a modern, high-performance Python web framework for building APIs. It’s:
- Fast to run (based on **ASGI**, not WSGI)
- Fast to write (with **auto-validation**, **type hints**, and **interactive docs**)
- Ideal for modern use cases like **machine learning**, **microservices**, and **async I/O**

---

## 🚀 Why FastAPI is Fast

### Built on ASGI (Asynchronous Server Gateway Interface)
- Traditional frameworks use **WSGI** (synchronous).
- FastAPI uses **ASGI** via **Uvicorn**, enabling **non-blocking I/O**.
- Great for high concurrency (handling multiple requests efficiently).

### Smart Code Generation
- Automatic docs via **Swagger (OpenAPI)** and **ReDoc**
- Based on function signatures and type hints → less boilerplate, more safety.

---

## 🪶 Starlette (Core of FastAPI)

FastAPI is powered by **[Starlette](https://www.starlette.io/)** under the hood — a lightweight ASGI toolkit.

### 🌟 Starlette Features:
- Async request handling
- Routing and middleware
- Background tasks
- WebSockets
- Dependency injection
- Sessions and cookies
- Built-in test client

FastAPI extends Starlette to provide easy-to-use syntax and advanced features like automatic validation and documentation.

---

## 🔎 Path Parameters

Path parameters are variables **embedded directly in the URL path**, used to uniquely identify a specific resource.

**Syntax:**
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

