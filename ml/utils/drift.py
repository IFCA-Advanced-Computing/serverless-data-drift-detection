from pathlib import Path

import numpy as np
import torch
import torchvision
from PIL import Image
from torch.utils.data import Dataset

from ml.utils.dataset import CustomDataset


def make_transformed_dataset(
        subset: Dataset,
        transform: torch.nn.Module | torchvision.transforms.Compose | None = None,
) -> Dataset:
    return CustomDataset(
        subset=subset,
        transform=transform,
    )


def save_images(data_loader, target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    batch_size = data_loader.batch_size
    for i, batch in enumerate(data_loader):
        batch = (np.squeeze(batch[0].numpy(), axis=1) * 255).astype("uint8")
        for image, file_path in zip(batch, data_loader.dataset.samples[i*batch_size: i*batch_size + batch_size]):
            file_image_path = Path(target_dir, str(file_path[1]))
            file_image_path.mkdir(parents=True, exist_ok=True)
            Image.fromarray(image).save(Path(file_image_path, f"{Path(file_path[0]).name}"))


transformations = [
    (
        "GaussianBlur(kernel_size=(5, 9), sigma=0.25)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.GaussianBlur(
                    kernel_size=(5, 9),
                    sigma=0.25),
            ],
        ),
    ),
    (
        "GaussianBlur(kernel_size=(5, 9), sigma=0.5)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.GaussianBlur(
                    kernel_size=(5, 9),
                    sigma=0.5),
            ],
        ),
    ),
    (
        "GaussianBlur(kernel_size=(5, 9), sigma=1.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.GaussianBlur(
                    kernel_size=(5, 9),
                    sigma=1.0),
            ],
        ),
    ),
    (
        "GaussianBlur(kernel_size=(5, 9), sigma=2.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.GaussianBlur(
                    kernel_size=(5, 9),
                    sigma=2.0),
            ],
        ),
    ),
    (
        "GaussianBlur(kernel_size=(5, 9), sigma=4.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.GaussianBlur(
                    kernel_size=(5, 9),
                    sigma=4.0),
            ],
        ),
    ),
    (
        "ElasticTransform(alpha=12.5, sigma=5.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ElasticTransform(
                    alpha=12.5,
                    sigma=5.0,
                ),
            ],
        ),
    ),
    (
        "ElasticTransform(alpha=25.0, sigma=5.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ElasticTransform(
                    alpha=25.0,
                    sigma=5.0,
                ),
            ],
        ),
    ),
    (
        "ElasticTransform(alpha=50.0, sigma=5.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ElasticTransform(
                    alpha=50.0,
                    sigma=5.0,
                ),
            ],
        ),
    ),
    (
        "ElasticTransform(alpha=100.0, sigma=5.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ElasticTransform(
                    alpha=100.0,
                    sigma=5.0,
                ),
            ],
        ),
    ),
    (
        "ElasticTransform(alpha=200.0, sigma=5.0)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ElasticTransform(
                    alpha=200.0,
                    sigma=5.0,
                ),
            ],
        ),
    ),
    (
        "ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.025)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ColorJitter(
                    brightness=0.1,
                    contrast=0.1,
                    saturation=0.1,
                    hue=0.025,
                ),
            ],
        ),
    ),
    (
        "ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.05)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ColorJitter(
                    brightness=0.2,
                    contrast=0.2,
                    saturation=0.2,
                    hue=0.05,
                ),
            ],
        ),
    ),
    (
        "ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ColorJitter(
                    brightness=0.4,
                    contrast=0.4,
                    saturation=0.4,
                    hue=0.1,
                ),
            ],
        ),
    ),
    (
        "ColorJitter(brightness=0.8, contrast=0.8, saturation=0.8, hue=0.2)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ColorJitter(
                    brightness=0.8,
                    contrast=0.8,
                    saturation=0.8,
                    hue=0.2,
                ),
            ],
        ),
    ),
    (
        "ColorJitter(brightness=1.6, contrast=1.6, saturation=1.6, hue=0.4)",
        torchvision.transforms.Compose(
            [
                torchvision.transforms.ColorJitter(
                    brightness=1.6,
                    contrast=1.6,
                    saturation=1.6,
                    hue=0.4,
                ),
            ],
        ),
    ),
]
