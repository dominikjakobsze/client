import os

import httpx
from dotenv import load_dotenv
from fastapi import HTTPException

from app.clients import fetch_photos, fetch_taxon
from app.inference import run_inference
from app.model import load_model
from app.schemas import RecognitionResult

load_dotenv()


async def recognize_animal(image_bytes: bytes, client: httpx.AsyncClient) -> RecognitionResult:
    unsplash_key = os.getenv("UNSPLASH_KEY")
    if not unsplash_key:
        raise HTTPException(status_code=500, detail="UNSPLASH_KEY environment variable is not set")

    device, model, transforms, labels = await load_model()
    if labels is None:
        raise HTTPException(status_code=500, detail="Model labels not available")

    confidence, label = run_inference(image_bytes, device, model, transforms, labels)
    common_name = await fetch_taxon(client, label)
    photos = await fetch_photos(client, common_name, unsplash_key)

    return RecognitionResult(
        main=photos[0]["urls"]["full"],
        name=common_name,
        confidence=confidence,
        additional=[p["urls"]["full"] for p in photos[1:4]],
    )
