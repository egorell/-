from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from groups import router as group_router

app = FastAPI()

app.include_router(group_router, prefix='/groups')

@app.get('/')
def root():
    return RedirectResponse('/docs')

if __name__ == '__main__':

    uvicorn.run(app='start_server:app', host='0.0.0.0', port=8000, reload=True)
