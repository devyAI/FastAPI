# Learning  FastAPI
## 📘 What is an API?

An **API (Application Programming Interface)** allows two software components to communicate with each other. In the context of web development, APIs typically allow clients (like web or mobile apps) to send HTTP requests to a server and receive responses, such as data or actions performed.

Example:
- Client: "Here’s some text, what’s the sentiment?"
- API: "It's Positive, with 99.8% confidence."

---

## ⚡ About FastAPI

**FastAPI** is a modern, high-performance Python web framework for building APIs. It’s:
- Fast to run (based on **ASGI**, not WSGI)
- Fast to write (with **auto-validation**, **type hints**, and **interactive docs**)
- Ideal for modern use cases like **machine learning**, **microservices**, and **async I/O**

---

##  Why FastAPI is Fast

### Built on ASGI (Asynchronous Server Gateway Interface)
- Traditional frameworks use **WSGI** (synchronous).
- FastAPI uses **ASGI** via **Uvicorn**, enabling **non-blocking I/O**.
- Great for high concurrency (handling multiple requests efficiently).

###  Smart Code Generation
- Automatic docs via **Swagger (OpenAPI)** and **ReDoc**
- Based on function signatures and type hints → less boilerplate, more safety.

---

## Pydantic (Data Validation)

FastAPI uses **Pydantic** for:
- Defining **data models**
- Automatic **type validation**
- Error messages for incorrect input

Example:
```python
from pydantic import BaseModel

class InputText(BaseModel):
    text: str

 