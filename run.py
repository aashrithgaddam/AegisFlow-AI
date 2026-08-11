import sys
import subprocess

print("[*] Diagnostic: Actively tracing your system's Python paths...")
print(f"[*] Executive path tracking: {sys.executable}")

# Force python to run the installer directly through its active execution core
print("[*] Synchronizing dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn", "pydantic", "python-dotenv", "groq"])

# Instantly hand off execution via Uvicorn module runner path to process strings correctly
print("\n[*] Handshake complete. Booting Gateway...")
subprocess.run([sys.executable, "-m", "uvicorn", "aegisflow_gateway:app", "--host", "127.0.0.1", "--port", "8000"])
