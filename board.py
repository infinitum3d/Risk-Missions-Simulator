"""
board.py

Core board data structures for the Risk Missions Simulator.

This first increment implements:

- Territory
- Board initialization
- Territory lookup
- Ownership
- Army placement/removal
- Basic validation

Adjacency, continent calculations, setup, combat helpers,
and path-finding will be added in later increments.
"""

from dataclasses import dataclass
from typing import Dict, Optional

from player import Player


@dataclass
class Territory:
    """
    Represents one territory on the game board.
    """

    name: str
    continent: str

    owner: Optional[Player] = None
    armies: int = 0

    def is_occupied(self) -> bool:
        return self.owner is not None


class Board:
    """
    Stores every territory and its current game state.
    """

    def __init__(self) -> None:
        self.territories: Dict[str, Territory] = {}

    # --------------------------------------------------
    # Territory management
    # --------------------------------------------------

    def add_territory(self, name: str, continent: str) -> None:
        if name in self.territories:
            raise ValueError(f"Duplicate territory: {name}")

        self.territories[name] = Territory(
            name=name,
            continent=continent,
        )

    def get(self, name: str) -> Territory:
        if name not in self.territories:
            raise KeyError(f"Unknown territory: {name}")

        return self.territories[name]

    def exists(self, name: str) -> bool:
        return name in self.territories

    # --------------------------------------------------
    # Ownership
    # --------------------------------------------------

    def owner(self, territory: str) -> Optional[Player]:
        return self.get(territory).owner

    def set_owner(self, territory: str, player: Player) -> None:
        t = self.get(territory)

        if t.owner is player:
            return

        if t.owner is not None:
            t.owner.remove_territory(territory)

        t.owner = player
        player.add_territory(territory)

    def clear_owner(self, territory: str) -> None:
        t = self.get(territory)

        if t.owner is not None:
            t.owner.remove_territory(territory)

        t.owner = None

    # --------------------------------------------------
    # Army management
    # --------------------------------------------------

    def armies(self, territory: str) -> int:
        return self.get(territory).armies

    def set_armies(self, territory: str, armies: int) -> None:
        if armies < 0:
            raise ValueError("Army count cannot be negative.")

        self.get(territory).armies = armies

    def add_armies(self, territory: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("Cannot add a negative number of armies.")

        self.get(territory).armies += amount

    def remove_armies(self, territory: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("Cannot remove a negative number of armies.")

        t = self.get(territory)

        if amount > t.armies:
            raise ValueError("Not enough armies in territory.")

        t.armies -= amount

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def territory_count(self) -> int:
        return len(self.territories)

    def occupied_count(self) -> int:
        return sum(
            1
            for territory in self.territories.values()
            if territory.owner is not None
        )

    def unoccupied_count(self) -> int:
        return self.territory_count() - self.occupied_count()
      
