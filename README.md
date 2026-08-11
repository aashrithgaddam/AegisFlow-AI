# AegisFlow-AI
An asynchronous Zero-Trust AI Security Gateway and Reverse Proxy built with FastAPI and the Groq SDK to defend LLM endpoints against OWASP Top 10 prompt injections and automated rate-limiting attacks.
# AegisFlow-AI: Zero-Trust Guardrail Gateway

An enterprise-grade AI Security Reverse Proxy built to protect Large Language Model (LLM) networks. AegisFlow-AI acts as a sub-millisecond safety firewall, intercepting incoming API traffic to stop jailbreaks, clean raw payloads, and block infrastructure exploits before they process.

---

## Key Security Features

* OWASP Top 10 LLM Hardening: Scanning engine designed to stop dangerous string injections and adversarial jailbreaks.
* Sub-Millisecond Asynchronous Middleware: Built using Python asyncio to intercept heavy traffic streams with zero delay.
* In-Memory Rate Limiting: High-speed tracking array protecting backend infrastructure from automated spam attacks.
* Zero-404 Automatic Redirection: Instantly routes basic web address searches straight to your interactive documentation dashboard.
* Decoupled Key Management: Built with python-dotenv to keep your private API access keys hidden from public version control.

---

## Core Technology Stack

* Core Engine: Python 3.10+
* Framework: FastAPI (High-performance execution layer)
* Data Integrity: Pydantic v2 (Strict payload data validation)
* Upstream SDK: Official Groq Client Pipeline
* Server Interceptor: Uvicorn ASGI Server

---

## Quick Setup & Deployment

1. Install Dependencies:
pip install fastapi uvicorn pydantic python-dotenv groq

2. Set Up Your Secret Key:
Create a file named .env in your folder and add:
GROQ_API_KEY=your_actual_key_here

3. Run the App:
python run.py

4. Visual Control Dashboard:
Open Google Chrome and visit: http://localhost:8000/
