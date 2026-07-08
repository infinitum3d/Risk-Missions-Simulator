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

    class Board:

    def __init__(self) -> None:
        self.territories: Dict[str, Territory] = {}
        self.adjacency = {}
        self._initialize_board()
        self._initialize_adjacency()

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
      
    # --------------------------------------------------
    # Board Initialization
    # --------------------------------------------------

    def _initialize_board(self) -> None:
        """Create all 42 standard Risk territories."""

            # --------------------------------------------------
    # Adjacency
    # --------------------------------------------------

    def _initialize_adjacency(self) -> None:
        """
        Create the complete standard Risk adjacency graph.
        """

        self.adjacency = {

            # ---------------- North America ----------------

            "Alaska": {
                "Northwest Territory",
                "Alberta",
                "Kamchatka",
            },

            "Northwest Territory": {
                "Alaska",
                "Alberta",
                "Ontario",
                "Greenland",
            },

            "Greenland": {
                "Northwest Territory",
                "Ontario",
                "Quebec",
                "Iceland",
            },

            "Alberta": {
                "Alaska",
                "Northwest Territory",
                "Ontario",
                "Western United States",
            },

            "Ontario": {
                "Northwest Territory",
                "Greenland",
                "Quebec",
                "Eastern United States",
                "Western United States",
                "Alberta",
            },

            "Quebec": {
                "Ontario",
                "Greenland",
                "Eastern United States",
            },

            "Western United States": {
                "Alberta",
                "Ontario",
                "Eastern United States",
                "Central America",
            },

            "Eastern United States": {
                "Ontario",
                "Quebec",
                "Western United States",
                "Central America",
            },

            "Central America": {
                "Western United States",
                "Eastern United States",
                "Venezuela",
            },

            # ---------------- South America ----------------

            "Venezuela": {
                "Central America",
                "Peru",
                "Brazil",
            },

            "Peru": {
                "Venezuela",
                "Brazil",
                "Argentina",
            },

            "Brazil": {
                "Venezuela",
                "Peru",
                "Argentina",
                "North Africa",
            },

            "Argentina": {
                "Peru",
                "Brazil",
            },

            # ---------------- Europe ----------------

            "Iceland": {
                "Greenland",
                "Great Britain",
                "Scandinavia",
            },

            "Scandinavia": {
                "Iceland",
                "Ukraine",
                "Northern Europe",
                "Great Britain",
            },

            "Ukraine": {
                "Scandinavia",
                "Northern Europe",
                "Southern Europe",
                "Ural",
                "Afghanistan",
                "Middle East",
            },

            "Great Britain": {
                "Iceland",
                "Scandinavia",
                "Northern Europe",
                "Western Europe",
            },

            "Northern Europe": {
                "Great Britain",
                "Scandinavia",
                "Ukraine",
                "Western Europe",
                "Southern Europe",
            },

            "Western Europe": {
                "Great Britain",
                "Northern Europe",
                "Southern Europe",
                "North Africa",
            },

            "Southern Europe": {
                "Western Europe",
                "Northern Europe",
                "Ukraine",
                "Middle East",
                "Egypt",
                "North Africa",
            },

            # ---------------- Africa ----------------

            "North Africa": {
                "Brazil",
                "Western Europe",
                "Southern Europe",
                "Egypt",
                "East Africa",
                "Congo",
            },

            "Egypt": {
                "North Africa",
                "Southern Europe",
                "Middle East",
                "East Africa",
            },

            "East Africa": {
                "Egypt",
                "North Africa",
                "Middle East",
                "Congo",
                "South Africa",
                "Madagascar",
            },

            "Congo": {
                "North Africa",
                "East Africa",
                "South Africa",
            },

            "South Africa": {
                "Congo",
                "East Africa",
                "Madagascar",
            },

            "Madagascar": {
                "East Africa",
                "South Africa",
            },

            # ---------------- Asia ----------------

            "Ural": {
                "Ukraine",
                "Siberia",
                "China",
                "Afghanistan",
            },

            "Siberia": {
                "Ural",
                "Yakutsk",
                "Irkutsk",
                "Mongolia",
                "China",
            },

            "Yakutsk": {
                "Siberia",
                "Kamchatka",
                "Irkutsk",
            },

            "Kamchatka": {
                "Yakutsk",
                "Irkutsk",
                "Mongolia",
                "Japan",
                "Alaska",
            },

            "Irkutsk": {
                "Siberia",
                "Yakutsk",
                "Kamchatka",
                "Mongolia",
            },

            "Mongolia": {
                "Irkutsk",
                "Kamchatka",
                "Japan",
                "China",
                "Siberia",
            },

            "Japan": {
                "Kamchatka",
                "Mongolia",
            },

            "Afghanistan": {
                "Ukraine",
                "Ural",
                "China",
                "India",
                "Middle East",
            },

            "Middle East": {
                "Ukraine",
                "Afghanistan",
                "India",
                "Southern Europe",
                "Egypt",
                "East Africa",
            },

            "India": {
                "Middle East",
                "Afghanistan",
                "China",
                "Siam",
            },

            "Siam": {
                "India",
                "China",
                "Indonesia",
            },

            "China": {
                "Ural",
                "Siberia",
                "Mongolia",
                "Siam",
                "India",
                "Afghanistan",
            },

            # ---------------- Australia ----------------

            "Indonesia": {
                "Siam",
                "New Guinea",
                "Western Australia",
            },

            "New Guinea": {
                "Indonesia",
                "Western Australia",
                "Eastern Australia",
            },

            "Western Australia": {
                "Indonesia",
                "New Guinea",
                "Eastern Australia",
            },

            "Eastern Australia": {
                "Western Australia",
                "New Guinea",
            },
        }


        for continent, territories in continents.items():
            for territory in territories:
                self.add_territory(territory, continent)

    # --------------------------------------------------
    # Queries
    # --------------------------------------------------

    def territories_in_continent(self, continent: str):
        return [
            territory
            for territory in self.territories.values()
            if territory.continent == continent
        ]

    def all_territories(self):
        return list(self.territories.values())

    def territory_names(self):
        return sorted(self.territories.keys())

    def continent_names(self):
        return sorted(
            {
                territory.continent
                for territory in self.territories.values()
            }
        )
    # --------------------------------------------------
    # Neighbor Queries
    # --------------------------------------------------

    def neighbors(self, territory: str) -> set[str]:
        return self.adjacency[territory]

    def are_adjacent(self, first: str, second: str) -> bool:
        return second in self.adjacency[first]

    def can_attack(self, attacker: str, defender: str) -> bool:
        if not self.are_adjacent(attacker, defender):
            return False

        if self.owner(attacker) is None:
            return False

        if self.owner(defender) is None:
            return False

        if self.owner(attacker) == self.owner(defender):
            return False

        return self.armies(attacker) > 1
