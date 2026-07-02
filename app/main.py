from fastapi import FastAPI

app = FastAPI(title="Uber Clone API")

@app.get("/health")
def health_check():
    return {"status": "ok"}