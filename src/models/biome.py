"""
Module biome.py
"""
from enum import Enum

class Biome(Enum):
    """
    Enumeration of possible biomes for the tiles.
    Each biome corresponds to a continuous area on the island.
    """
    WATER = "W"
    BEACH = "B"
    JUNGLE = "J"
    SAVANNA = "S"
    MOUNTAIN = "M"
    HILLS = "H"
    MARSH = "R"
    PLANTATION = "P"
    VILLAGE = "V"
    CITY = "C"
