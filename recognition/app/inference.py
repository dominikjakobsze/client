import io
from collections.abc import Callable

import torch
import torch.nn as nn
from PIL import Image


def run_inference(
    image_bytes: bytes,
    device: torch.device,
    model: nn.Module,
    transforms: Callable,
    labels: list[str],
) -> tuple[float, str]:
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    tensor = transforms(img).unsqueeze(0).to(device)

    with torch.no_grad():
        logits = model(tensor)
        probs = torch.softmax(logits, dim=-1)

    top = probs.topk(1)
    confidence: float = top.values[0].item()
    taxa_id: int = top.indices[0].item()
    return confidence, labels[taxa_id]
