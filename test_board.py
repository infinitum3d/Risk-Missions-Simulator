from board import Board

board = Board()

print(f"Territories: {board.territory_count()}")
print(f"Continents: {board.continent_names()}")

print()

print("Neighbors of Alaska:")
print(sorted(board.neighbors("Alaska")))

print()

print("Neighbors of Brazil:")
print(sorted(board.neighbors("Brazil")))

print()

print("Neighbors of Siam:")
print(sorted(board.neighbors("Siam")))
