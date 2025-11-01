"""
Module special.py
"""
from enum import Enum

class Special(Enum):
    """
    List of special tiles.
    Placement subject to the rules defined in the generation.
    """
    AIRPORT = "AP"
    ILLEGAL_AIRSTRIP = "AI"
    PORT = "PT"
    SMALL_DOCK = "PQ"
    RUINS = "RU"
    HOTEL = "HT"
    SLUM = "BD"
    CASCADE = "CS"