import os
import sys
import logging
import json
import joblib
import base64
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

from kindneyClassifier import logger  # Ensure logger is correctly set up

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as ConfigBox."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError(f"YAML file at {path_to_yaml} is empty or invalid.")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories from a list of paths."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data as a JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON data from a file and returns it as ConfigBox."""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file."""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in KB."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File at {path} does not exist.")
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring: str, fileName: str) -> None:
    """Decodes a Base64 image string and saves it to a file."""
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath: str) -> bytes:
    """Encodes an image into Base64 format."""
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
