class TicTacToe:
    def __init__(self):
        self.player_x = []
        self.player_o = []
        self.create_board()

    def create_board(self):
        self.slots = [" "] * 9
        for i in self.player_x:
            self.slots[i - 1] = "x"
        for i in self.player_o:
            self.slots[i - 1] = "o"

    def draw_board(self):
        self.create_board()
        for i in range(3):
            print("".join([f" {self.slots[i * 3 + j]} |" for j in range(3)])[:-1])
            if i != 2:
                print(11 * "-")

    def get_player(self, player_sign):
        if player_sign == "x":
            return self.player_x
        if player_sign == "o":
            return self.player_o
        raise ValueError("Invalid player, must be 'x' or 'o'.")

    def place(self, player_sign, slot):
        player = self.get_player(player_sign)
        if slot not in (self.player_x + self.player_o):
            player.append(slot)
    
    def move(self, player_sign, slot):
        player = self.get_player(player_sign)
        player.remove(slot)   


if __name__ == "__main__":
    game = TicTacToe()
    game.place('x', 1)
    game.place('o', 3)
    game.draw_board()
    game.place('x', 4)
    game.place('o', 5)
    game.draw_board()
