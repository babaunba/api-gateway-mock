from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Issue(BaseModel):
    title: str
    description: str


@app.post("/get-labels")
async def get_tags(_: Issue) -> List[str]:
    return [ "bug", "documentation" ]
