from fastapi import FastAPI
from diplomkaback.routes.llm_route import router as llm_route

app = FastAPI()

app.include_router(llm_route)