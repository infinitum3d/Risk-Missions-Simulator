```python
"""
constants.py

Global constants used throughout the Risk Missions Simulator.
"""

from enum import Enum

# --------------------------------------------------
# Project Information
# --------------------------------------------------

GAME_NAME = "Risk Missions Simulator"
VERSION = "0.1.0"

# --------------------------------------------------
# Game Setup
# --------------------------------------------------

PLAYER_COUNT = 3
NEUTRAL_COUNT = 3
FACTION_COUNT = PLAYER_COUNT + NEUTRAL_COUNT

TERRITORY_COUNT = 42
CONTINENT_COUNT = 6

STARTING_TERRITORIES = 7
STARTING_ARMIES = 21

PUBLIC_MISSIONS = 3
PRIVATE_MISSIONS = 3
TOTAL_MISSIONS = 12

WINNING_POINTS = 4

# --------------------------------------------------
# Dice
# --------------------------------------------------

MAX_ATTACK_DICE = 3
MAX_DEFEND_DICE = 2

# --------------------------------------------------
# Continents
# --------------------------------------------------

class Continent(Enum):
    NORTH_AMERICA = "North America"
    SOUTH_AMERICA = "South America"
    EUROPE = "Europe"
    AFRICA = "Africa"
    ASIA = "Asia"
    AUSTRALIA = "Australia"

# Standard Risk continent bonuses
CONTINENT_BONUSES = {
    Continent.NORTH_AMERICA: 5,
    Continent.SOUTH_AMERICA: 2,
    Continent.EUROPE: 5,
    Continent.AFRICA: 3,
    Continent.ASIA: 7,
    Continent.AUSTRALIA: 2,
}
```
