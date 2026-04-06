import asyncio
from collections.abc import Callable

import timm
import torch
import torch.nn as nn

ANIMAL_CLASSES = frozenset({
    "Mammalia", "Aves", "Reptilia", "Amphibia",
    "Actinopterygii", "Insecta", "Arachnida", "Mollusca", "Animalia",
})

_device: torch.device | None = None
_model: nn.Module | None = None
_transforms: Callable | None = None
_labels: list[str] | None = None


def _load_model() -> tuple[torch.device, nn.Module, Callable, list[str] | None]:
    global _device, _model, _transforms, _labels
    if _model is not None:
        return _device, _model, _transforms, _labels

    _device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
    _model = timm.create_model(
        "hf-hub:timm/vit_large_patch14_clip_336.laion2b_ft_augreg_inat21",
        pretrained=True,
        num_classes=10000,
    ).to(_device)
    _model.eval()

    data_config = timm.data.resolve_model_data_config(_model)
    _transforms = timm.data.create_transform(**data_config, is_training=False)
    _labels = _model.pretrained_cfg.get("label_names")

    return _device, _model, _transforms, _labels


async def load_model() -> tuple[torch.device, nn.Module, Callable, list[str] | None]:
    return await asyncio.to_thread(_load_model)
