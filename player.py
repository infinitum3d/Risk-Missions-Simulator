"""
player.py

Represents a player or neutral faction in the Risk Missions Simulator.
"""

from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Player:
    """
    Represents one faction in the game.

    A Player may be either:
      - A human-controlled AI player
      - A neutral faction
    """

    id: int
    name: str
    is_neutral: bool = False

    # Game state
    score: int = 0
    eliminated: bool = False

    # Territory ownership
    territories: Set[str] = field(default_factory=set)

    # Missions
    hand: List[int] = field(default_factory=list)
    completed_missions: List[int] = field(default_factory=list)

    # Statistics
    armies_destroyed: int = 0
    armies_lost: int = 0
    territories_captured: int = 0
    turns_taken: int = 0

    def territory_count(self) -> int:
        """Return the number of territories currently owned."""
        return len(self.territories)

    def owns_territory(self, territory: str) -> bool:
        """Return True if this player owns the territory."""
        return territory in self.territories

    def add_territory(self, territory: str) -> None:
        """Add a territory to this player's control."""
        self.territories.add(territory)

    def remove_territory(self, territory: str) -> None:
        """Remove a territory from this player's control."""
        self.territories.discard(territory)

    def add_score(self, points: int = 1) -> None:
        """Increase the player's score."""
        self.score += points

    def complete_mission(self, mission_id: int) -> None:
        """
        Complete a mission.

        The mission is removed from the player's hand and placed
        into the completed mission pile.
        """
        if mission_id in self.hand:
            self.hand.remove(mission_id)

        if mission_id not in self.completed_missions:
            self.completed_missions.append(mission_id)

    def eliminate(self) -> None:
        """Mark this player as eliminated."""
        self.eliminated = True
        self.territories.clear()

    @property
    def active(self) -> bool:
        """True if this faction is still in the game."""
        return not self.eliminated

    def __str__(self) -> str:
        faction_type = "Neutral" if self.is_neutral else "Player"
        return (
            f"{faction_type} {self.id}: {self.name} | "
            f"Score={self.score} | "
            f"Territories={self.territory_count()} | "
            f"Active={self.active}"
        )
