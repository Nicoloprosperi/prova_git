from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello from OpenShift"}

@app.get("/health")
def health():
    return {"ok": True}
