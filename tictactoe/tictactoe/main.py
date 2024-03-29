from .custom_errors import InvalidSlotError, OccupiedSlotError


class TicTacToe:
    def __init__(self, player_x=[], player_o=[]):
        self.player_x = player_x
        self.player_o = player_o

    def create_board(self):
        self.slots = [" "] * 9
        for i in self.player_x:
            self.slots[i - 1] = "x"
        for i in self.player_o:
            self.slots[i - 1] = "o"
    
    def get_avaliable_slots(self):
        return set([i + 1 for i in range(9)]) - set(self.player_x + self.player_o)

    def get_player(self, player_sign):
        if player_sign == "x":
            return self.player_x
        if player_sign == "o":
            return self.player_o
        raise ValueError("Invalid player, must be 'x' or 'o'.")
    
    def _check_valid_slot(self, slot):
        if slot < 1 or slot > 9:
            raise InvalidSlotError(slot)

    def _check_occupied_slot(self, slot):
        if slot in self.player_x + self.player_o:
            raise OccupiedSlotError(slot)

    def place(self, player_sign, slot):
        self._check_valid_slot(slot)
        self._check_occupied_slot(slot)
        player = self.get_player(player_sign)
        player.append(slot)
    
    def move(self, player_sign, slot):
        self._check_valid_slot(slot)
        player = self.get_player(player_sign)
        try:
            player.remove(slot)
        except ValueError:
            raise ValueError(f"{player_sign} has no brick in slot {slot}. Choose one of {player}")

    def check_win(self, player_sign):
        player = sorted(self.get_player(player_sign))
        if len(player) == 3:
            if player in (
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
                [1, 5, 9],
                [3, 5, 7]
            ):
                return True
        return False


def draw_board(game):
        game.create_board()
        for i in range(3):
            print("".join([f" {game.slots[i * 3 + j]} |" for j in range(3)])[:-1])
            if i != 2:
                print(11 * "-")


def command_line_game():
    game = TicTacToe()
    player_sign = ""
    while player_sign not in ("x", "o"):
        player_sign = input("Choose starting player, 'x' or 'y': ")
    player_sign = 'x' if player_sign == 'o' else 'o'
    while not game.check_win(player_sign):
        player_sign = 'x' if player_sign == 'o' else 'o'
        player = game.get_player(player_sign)
        if len(player) == 3:
            moved = False
            while not moved:
                try:
                    game.move(player_sign, int(input(f"{player_sign}'s turn. Choose which brick to move: ")))
                    moved = True
                except (ValueError, InvalidSlotError) as e:
                    print(e)
            
        placed = False
        while not placed:
            try:
                game.place(player_sign, int(input(f"{player_sign}'s turn. Choose where to place brick: ")))
                placed = True
            except InvalidSlotError as e:
                print(e)
            except OccupiedSlotError as e:
                print(f"{e} Available slots are {game.get_avaliable_slots()}")

        draw_board(game)

    print(f"Congratulations. {player_sign} won!")
