from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import httpx

from models import StoreWithFilm

app = FastAPI()
db_service_url = "http://localhost:8002"

@app.get("/stores/films", response_model=List[StoreWithFilm])
async def search_stores(
    film_name: Optional[str] = Query(None, description="Search by film name"),
    genre: Optional[str] = Query(None, description="Search by genre"),
    actor: Optional[str] = Query(None, description="Search by actor name")
):
    search_params = {"film_name": film_name, "genre": genre, "actor": actor}
    search_params = {k: v for k, v in search_params.items() if v is not None}

    if len(search_params) != 1:
        raise HTTPException(status_code=400, detail="Specify exactly one search parameter: film_name, genre, or actor")

    search_type, search_value = next(iter(search_params.items()))

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{db_service_url}/stores/films", params={search_type: search_value})
            response.raise_for_status()
            stores = response.json()
        
        return [StoreWithFilm(**store) for store in stores]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve stores: {str(e)}")
