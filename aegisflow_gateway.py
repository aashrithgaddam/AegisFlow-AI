import os
import time
import asyncio
import logging
from typing import List, Dict
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, RedirectResponse  # Added: RedirectResponse
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from groq import Groq 
import uvicorn  

# ==========================================
# 1. AUTOMATIC INTELLIGENT FILE LINKING
# ==========================================
current_directory = Path(".").resolve()
old_env_path = None

for parent in [current_directory, current_directory.parent, current_directory.parent.parent]:
    possible_paths = [
        parent / ".env",
        parent / "env",
        *parent.glob("*/.env")
    ]
    for path in possible_paths:
        if path.is_file() and path.name == ".env":
            old_env_path = path
            break
    if old_env_path:
        break

if old_env_path:
    print(f"\n[+] SUCCESS: Found and linked your previous key file at: {old_env_path}")
    load_dotenv(dotenv_path=old_env_path)
else:
    print("\n[-] Note: Scanning local directory space for configuration flags...")
    load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    logging.critical("CRITICAL ERROR: GROQ_API_KEY could not be found anywhere on your system paths!")
    raise ValueError("Missing GROQ_API_KEY in active pipeline workspace environment.")

client = Groq(api_key=api_key)

# ==========================================
# 2. INITIALIZATION & ENTERPRISE DOCS CONFIG
# ==========================================
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("AegisFlow-Gateway")

app = FastAPI(
    title="🛡️ AegisFlow-AI: Enterprise Guardrail Gateway",
    description="""
    ### Zero-Trust Asynchronous Firewall protecting LLM Endpoints.
    
    * 🔍 **OWASP Top 10 LLM Protection:** Real-time signature scanning for Prompt Injections.
    * ⏳ **Token-Bucket Rate Limiting:** High-speed in-memory state tracking to prevent DoS.
    * 🔐 **Data Sanitization:** Strict input schemas powered by Pydantic validation frameworks.
    """,
    version="1.0.0",
    docs_url="/docs",       
    redoc_url="/redoc"      
)

IP_RATE_TRACKER: Dict[str, List[float]] = {}
RATE_LIMIT_WINDOW = 60.0  
MAX_REQUESTS_PER_WINDOW = 5  

PROMPT_INJECTION_SIGNATURES = [
    "ignore all previous instructions",
    "system prompt",
    "disregard safety guidelines",
    "you are now a malicious",
    "output raw content",
    "dan mode",
    "jailbreak",
    "reveal your developers secrets"
]

class MessageSchema(BaseModel):
    role: str = Field(..., description="Role validation string constraint")
    content: str = Field(..., min_length=1, max_length=2000, description="Payload bounds checking")

class ChatCompletionRequest(BaseModel):
    model: str = Field(default="llama-3.3-70b-versatile", description="Target engine model deployment identifier")
    messages: List[MessageSchema] = Field(..., description="List structure containing conversations")
    temperature: float = Field(default=0.0, ge=0.0, le=1.0)

# ==========================================
# 3. AUTOMATIC HOME LINK WEBSITE RE-ROUTING
# ==========================================
@app.get("/")
async def redirect_to_website_dashboard():
    """Forces the basic link to instantly open the interactive UI, eliminating 404s."""
    return RedirectResponse(url="/docs")

# ==========================================
# 4. CYBERSECURITY FIREWALL RULES & ROUTING
# ==========================================
def scan_for_prompt_injection(text: str) -> bool:
    normalized_text = text.lower()
    for signature in PROMPT_INJECTION_SIGNATURES:
        if signature in normalized_text:
            logger.warning(f"INJECTION BLOCKED: Text pattern intercepted security flag: '{signature}'")
            return True
    return False

@app.middleware("http")
async def enforcement_rate_limiter(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown_ip"
    current_time = time.time()
    
    if client_ip not in IP_RATE_TRACKER:
        IP_RATE_TRACKER[client_ip] = []
        
    IP_RATE_TRACKER[client_ip] = [t for t in IP_RATE_TRACKER[client_ip] if current_time - t < RATE_LIMIT_WINDOW]
    
    if len(IP_RATE_TRACKER[client_ip]) >= MAX_REQUESTS_PER_WINDOW:
        logger.error(f"RATE BLOCKADE: Denied interaction path traffic processing on IP: {client_ip}")
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"error": "Rate limit exceeded. Dynamic protection activated. Max 5 req/min."}
        )
        
    IP_RATE_TRACKER[client_ip].append(current_time)
    return await call_next(request)

@app.post("/v1/chat/completions")
async def secure_chat_proxy(payload: ChatCompletionRequest):
    logger.info(f"Analyzing transaction frame target destination: {payload.model}")
    
    for message in payload.messages:
        if scan_for_prompt_injection(message.content):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Security Violation: Adversarial Prompt Injection Variant Detected."
            )
            
    try:
        messages_dict = [{"role": msg.role, "content": msg.content} for msg in payload.messages]
        
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model=payload.model,
                messages=messages_dict,
                temperature=payload.temperature
            )
        )
        
        return {
            "choices": [
                {
                    "message": {
                        "role": response.choices.message.role,
                        "content": response.choices.message.content
                    }
                }
            ],
            "model": payload.model
        }
        
    except Exception as exc:
        logger.critical(f"Handshake Execution Error: {str(exc)}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Upstream Cluster Transaction Interruption: {str(exc)}"
        )

if __name__ == "__main__":
    print("\n[*] Booting AegisFlow-AI Secure Proxy Interface Gateway...")
    uvicorn.run("aegisflow_gateway:app", host="127.0.0.1", port=8000)
