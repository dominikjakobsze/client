import httpx
from fastapi import APIRouter, UploadFile

from app.schemas import RecognitionResult
from app.service import recognize_animal

router = APIRouter()


@router.post("/recognize", response_model=RecognitionResult)
async def recognize(file: UploadFile) -> RecognitionResult:
    contents = await file.read()
    async with httpx.AsyncClient(timeout=10.0) as client:
        return await recognize_animal(contents, client)
