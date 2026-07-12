# Multi-Vendor Marketplace Application

A robust, production-ready full-stack Multi-Vendor Marketplace application built with Django and MySQL. The system is architected as a clean monolith featuring isolated apps for granular feature handling, comprehensive user authentication, dynamic item listing, and a built-in messaging system for buyers and sellers.

## 🚀 Key Features
*   **Decoupled App Architecture:** Separated into `core`, `dashboard`, `item`, and `conversation` apps for modularity and scalability.
*   **Relational Database Backend:** Powered by a robust MySQL implementation managing complex relationships for listings and user chats.
*   **Security First:** Strict environment configuration using `.env` handling for sensitive data (`DEBUG`, `SECRET_KEY`, Database Credentials).
*   **Comprehensive Inbox System:** Native, internal messaging thread architecture allowing real-time context-based inquiries on marketplace items.

---

## 🛠️ Tech Stack
*   **Backend:** Python, Django (Monolithic Architecture)
*   **Database:** MySQL
*   **Environment Management:** Python `venv`, `python-dotenv`

---

## 💻 Getting Started Locally

### 1. Prerequisites
*   Python 3.10+
*   MySQL Server running locally

### 2. Installation & Setup
Clone the repository and navigate to the project directory:
```bash
git clone [https://github.com/manojkc1dev/marketplace-app.git](https://github.com/manojkc1dev/marketplace-app.git)
cd marketplace-app
