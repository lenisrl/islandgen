"""
Module tile.py
"""
from typing import List, Optional
from models.biome import Biome
from models.special import Special

class Tile:
    """
    Class representing a tile on the island.
    """
    def __init__(
        self,
        x: int,
        y: int,
        biome: Biome,
        special: Optional[Special] = None,
        description: Optional[str] = None,
        images: Optional[List[str]] = None
    ):
        self.x = x  # X coordinate
        self.y = y  # Y coordinate
        self.biome = biome
        self.special = special
        self.description = description
        self.images = images or []

    def add_image(self, image_path: str):
        """Adds an image path to the box."""
        self.images.append(image_path)