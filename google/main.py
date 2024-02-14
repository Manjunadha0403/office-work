from fastapi import FastAPI
from routers import main_shopping, main_cus, main_pro
import uvicorn

app = FastAPI()

app.include_router(main_cus.router)
app.include_router(main_pro.router)
app.include_router(main_shopping.router)
app.get("/")
def main():
    return {"data":"hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)