from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello from Secure K8s Starter"}

@app.get("/health")
async def health():
    return {"status": "ok"}
