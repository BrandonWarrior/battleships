class BattleshipGame:
    """
    A class to represent a Battleship game.
    """

    def __init__(self, size, num_ships, player_name, ship_type):
        """
        Initialize the game with grid size, number of ships, player name, and ship type.
        Also, create the grid and randomly place ships on it.
        """
        self.size = size
        self.num_ships = num_ships
        self.player_name = player_name
        self.ship_type = ship_type
        self.grid = self.create_grid()
        self.ships = self.place_ships()

    def create_grid(self):
        """
        Create an empty game grid of the specified size.
        """
        return [["O" for _ in range(self.size)] for _ in range(self.size)]

    def display_grid(self):
        """
        Display the current state of the game grid to the player.
        The grid will show hits ("H"), misses ("M"), and unexplored spots ("O").
        """
        for row in self.grid:
            print(*row)

    def place_ships(self):
        """
        Randomly place the specified number of ships on the grid.
        Ensures that no two ships occupy the same coordinates.
        """
        ships = []
        while len(ships) < self.num_ships:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in ships:
                ships.append((row, col))
                # Ships are hidden from the player in the grid.
        return ships

    def get_player_guess(self):
        """
        Prompt the player to enter coordinates for their guess.
        Ensures that the input is valid and within the bounds of the grid.
        """
        while True:
            try:
                row = int(input(f"Enter a row (0-{self.size - 1}): "))
                col = int(input(f"Enter a column (0-{self.size - 1}): "))
                if 0 <= row < self.size and 0 <= col < self.size:
                    return (row, col)
                else:
                    print("Invalid input! Please enter values within the grid range.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

    def check_guess(self, guess):
        """
        Check if the player's guess hits or misses a ship.
        Marks the grid accordingly with "H" for hits and "M" for misses.
        """
        row, col = guess
        if (row, col) in self.ships:
            print("Hit!")
            self.grid[row][col] = "H"
            self.ships.remove((row, col))
        else:
            print("Miss!")
            self.grid[row][col] = "M"

    def check_game_over(self):
        """
        Check if all ships have been sunk, indicating that the game is over.
        """
        if not self.ships:
            print("Congratulations! You've sunk all the ships!")
            return True
        return False

    def start_game(self):
        """
        Start the game, display the grid, and manage the game loop.
        The game continues until all ships are hit and the player wins.
        """
        print(f"Welcome, {self.player_name}! Let's play Battleships!\n")
        print(f"Grid Size: {self.size}x{self.size}, Ships: {self.num_ships}, Ship Type: {self.ship_type}")
        print("Here is your game board:\n")
        """
        Main game loop: Continues until all ships are sunk
        """
        while not self.check_game_over():
            self.display_grid()
            guess = self.get_player_guess()
            self.check_guess(guess)
        """
        Run the game if this script is executed
        """
if __name__ == "__main__":
    player_name = input("Enter your name to start the game: ")
    game = BattleshipGame(size=5, num_ships=4, player_name=player_name, ship_type="Battleship")
    game.start_game()