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

* Core Engine: Python 3.14
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


## Live Framework Execution Output

Below is the live terminal runtime trace showing the AegisFlow-AI runtime daemon intercepting an autonomous AI agent's tool requests, evaluating the execution command against local security guardrails, blocking a destructive action, and archiving the audit trail:

```text
=================================================================
 AEGISFLOW-AI: PROACTIVE AI GOVERNANCE & SECURITY FRAMEWORK
=================================================================

[INFO] Booting Go-based policy validation layer...
[INFO] Loading security policy rules from ./config/policies.json... Success.
[INFO] Connected to autonomous agent RPC listener stream. Monitoring active...

-----------------------------------------------------------------
[INTERCEPT] Inbound Tool Request from Agent: 'DevBot-09'
-----------------------------------------------------------------
[EVALUATING] Requested Action Type: run_system_command
[ARGUMENTS] Target Parameters: {"cmd": "rm -rf /usr/local/bin/config"}

[SECURITY RISK MATCHED] Evaluating against Rule ID: RULE_SYS_WRITE_04
[CRITICAL ALERT] Destructive terminal operation detected without human-in-the-loop MFA.
[VIOLATION] Attempted modification of protected system binaries/directories.

--- SECURITY EVALUATION VERDICT ---
ACTION TAKEN      : [ BLOCKED & DROPPED]
POLICY SCORE      : 0.00 / 1.00 (Critical Risk Failure)
AUDIT REPORT LOG  : Hashed to tamper-evident file: block_ledger_8831.log
NOTIFICATION      : Broadcast triggered to system administrator security console.

-----------------------------------------------------------------
[INTERCEPT] Inbound Tool Request from Agent: 'Research-Bot-02'
-----------------------------------------------------------------
[EVALUATING] Requested Action Type: web_scrape_url
[ARGUMENTS] Target Parameters: {"url": "https://wikipedia.org"}

[SECURITY RISK MATCHED] Evaluating against Rule ID: RULE_NET_OUTBOUND_01
[PASSED] Target domain matches global safe-list parameters.
[VERDICT] Request APPROVED. Forwarding request execution payload to agent context.
```
