from fastapi import FastAPI

from recipies.router import router

app = FastAPI()

app.include_router(router=router)


@app.get('/')
def main_page():
    return {'message': 'Hello World!'}
