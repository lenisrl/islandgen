"""
Module island.py
"""
from typing import List
from models.tile import Tile
from models.biome import Biome
from datetime import datetime

class Island:
    """
    Class representing an entire island.
    Contains metadata and the grid of boxes.
    """
    def __init__(
        self,
        name: str,
        width: int = 80,
        height: int = 80,
        population: int = 10000,
        wealth: str = "medium",
        crime: str = "low",
        climate: str = "tropical",
        biomes: List[Biome] = None,
        seed: int = None
    ):
        self.name = name
        self.width = width
        self.height = height
        self.population = population
        self.wealth = wealth
        self.crime = crime
        self.climate = climate
        self.biomes = biomes or []
        self.seed = seed
        self.created_at = datetime.now()

        # Island grid: list of Tile lists
        self.tiles: List[List[Tile]] = [
            [None for _ in range(width)] for _ in range(height)
        ]

    def set_tile(self, x: int, y: int, tile: Tile):
        """Place a tile in the grid."""
        self.tiles[y][x] = tile

    def get_tile(self, x: int, y: int) -> Tile:
        """Returns the tile to the given position."""
        return self.tiles[y][x]

    def all_tiles(self) -> List[Tile]:
        """Returns a flat list of all tiles on the island."""
        return [tile for row in self.tiles for tile in row if tile is not None]
    