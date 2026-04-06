import httpx
from fastapi import HTTPException

from app.model import ANIMAL_CLASSES


async def fetch_taxon(client: httpx.AsyncClient, label: str) -> str:
    response = await client.get(
        "https://api.inaturalist.org/v1/taxa",
        params={"q": label, "rank": "species", "per_page": 1, "locale": "en"},
    )
    response.raise_for_status()
    results = response.json().get("results", [])

    if not results:
        raise HTTPException(status_code=422, detail=f"Species not found in iNaturalist: {label}")

    taxon = results[0]
    if taxon.get("iconic_taxon_name") not in ANIMAL_CLASSES:
        raise HTTPException(status_code=422, detail="Identified organism is not an animal")

    common_name: str | None = taxon.get("preferred_common_name")
    if not common_name:
        raise HTTPException(status_code=422, detail="No common name available for identified species")

    return common_name


async def fetch_photos(client: httpx.AsyncClient, common_name: str, unsplash_key: str) -> list[dict]:
    response = await client.get(
        "https://api.unsplash.com/search/photos",
        params={"query": common_name, "per_page": 4},
        headers={"Authorization": f"Client-ID {unsplash_key}"},
    )
    response.raise_for_status()
    photos = response.json().get("results", [])

    if not photos:
        raise HTTPException(status_code=422, detail="No photos found for identified species")

    return photos
