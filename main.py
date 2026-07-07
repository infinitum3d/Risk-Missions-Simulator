```python
"""
Risk Missions Simulator

Entry point for the application.
"""

from risk_missions.constants import (
    GAME_NAME,
    VERSION,
    TERRITORY_COUNT,
    PLAYER_COUNT,
    NEUTRAL_COUNT,
)


def main() -> None:
    print("=" * 40)
    print(GAME_NAME)
    print(f"Version {VERSION}")
    print("=" * 40)
    print()
    print(f"Territories : {TERRITORY_COUNT}")
    print(f"Players     : {PLAYER_COUNT}")
    print(f"Neutrals    : {NEUTRAL_COUNT}")
    print()
    print("Project initialized successfully.")
    print("Ready for Version 0.2.")


if __name__ == "__main__":
    main()
```
