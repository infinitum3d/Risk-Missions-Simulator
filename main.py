```python
"""
Risk Missions Simulator

Application entry point.
"""

from constants import (
    GAME_NAME,
    VERSION,
    TERRITORY_COUNT,
    PLAYER_COUNT,
    NEUTRAL_COUNT,
)


def main():
    print("=" * 40)
    print(GAME_NAME)
    print(f"Version {VERSION}")
    print("=" * 40)
    print(f"Territories : {TERRITORY_COUNT}")
    print(f"Players     : {PLAYER_COUNT}")
    print(f"Neutrals    : {NEUTRAL_COUNT}")
    print()
    print("Initialization successful.")


if __name__ == "__main__":
    main()
```
