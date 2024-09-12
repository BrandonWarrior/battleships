import random

class BattleshipGame:
    def __init__(self, size, num_ships, player_name, ship_type):
        self.size = size  # Set grid size (default 5x5)
        self.num_ships = num_ships  # Number of ships
        self.player_name = player_name  # Player name from input
        self.ship_type = ship_type  # Type of ships
        self.grid = self.create_grid()  # Create the game grid
        self.ships = self.place_ships()  # Place ships on the grid

    # Create a grid based on the size
    def create_grid(self):
        return [["O" for _ in range(self.size)] for _ in range(self.size)]

    # Display the grid to the user
    def display_grid(self):
        for row in self.grid:
            print(*row)

    # Place ships randomly on the grid
    def place_ships(self):
        ships = []
        while len(ships) < self.num_ships:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in ships:
                ships.append((row, col))
                self.grid[row][col] = "X"  # Mark ship locations with 'X' (for now)
        return ships

    # Start the game
    def start_game(self):
        print(f"Welcome, {self.player_name}! Let's play Battleships!\n")
        print(f"Grid Size: {self.size}x{self.size}, Ships: {self.num_ships}, Ship Type: {self.ship_type}")
        print("Here is your game board:\n")
        self.display_grid()

# Add logic to run the game
if __name__ == "__main__":
    # Ask for the player's name before starting
    player_name = input("Enter your name to start the game: ")
    
    # Initialize the game with grid size 5x5, 4 ships, player name, and ship type
    game = BattleshipGame(size=5, num_ships=4, player_name=player_name, ship_type="Battleship")
    game.start_game()
