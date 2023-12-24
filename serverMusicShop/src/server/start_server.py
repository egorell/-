import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from instruments import router as instruments_router

app = FastAPI(
    title='Music_shop_server'
)

app.include_router(instruments_router, prefix='/instruments')

@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':

    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)