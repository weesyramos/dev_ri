from fastapi import FastAPI

app = FastAPI(title="Restaurant Platform")


@app.get("/health")
def healthcheck():
    return {"status": "ok"}