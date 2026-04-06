from pydantic import BaseModel


class RecognitionResult(BaseModel):
    main: str
    name: str
    confidence: float
    additional: list[str]
