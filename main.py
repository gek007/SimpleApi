from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"msg":"Hello Kostya"}

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

