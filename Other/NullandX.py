class Field:
    EMPTY_CELL = ' '

    def __init__(self, size=3):
        self.size = size
        self.count = size * size
        self.cells = []
        for i in range(size):
            self.cells.append([Field.EMPTY_CELL] * size)
        # print(self.cells)

    def is_cell_empty(self, x, y):
        return self.cells[x][y] == Field.EMPTY_CELL

    def set_cell(self, x, y, value):
        self.cells[x][y] = value
        self.count -= 1

    def __str__(self):
        result = " " * 5
        for i in range(self.size):
            result += f"{i:^4}"
        line = "\n" + " " * 4 + "-" * (self.size * 4 + 1)
        result += line
        for i in range(self.size):
            row = f"{i:^4}" + "|"
            for j in range(self.size):
                row += f"{self.cells[i][j]:^3}" + "|"
            result += "\n" + row + line
        return result


class Player():
    def __init__(self, name, symbol, initial_score=0):
        self.name = name
        self.symbol = symbol
        self.score = initial_score

    def won_match(self):
        self.score += 100

    def lost_match(self):
        self.score -= 50

    def show_score(self):
        print('Игрок {}: {} очки'.format(self.name, self.score))


class Game():
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0

    def greet_user(self, currplayer):
        print("Очередь игрока " + currplayer.symbol)

    def play(self):
        flag = False

        while flag == False:

            currplayer = self.players[self.turn]

            self.board.print_board()

            self.greet_user(currplayer)

            move = Move(self.board, currplayer)
            player_move = move.ask_for_move()

            self.board.tiles[player_move] = currplayer.symbol

            winner = self.check_win(currplayer.symbol)

            if winner != False:
                self.game_over(winner)
                flag = True

            else:
                self.turn = 1 - self.turn

    def check_win(self, player_symbol):
        tiles = self.board.tiles

        for i in range(3):
            if tiles[i] == player_symbol and tiles[i + 3] == player_symbol and tiles[ i + 6] == player_symbol:
                 # check for vertical win
                return player_symbol
            elif tiles[(i * 3)] == player_symbol and tiles[(i * 3) + 1] == player_symbol and tiles[(i * 3) + 2] == player_symbol:
                # check for horizontal win
                return player_symbol

            if tiles[0] == player_symbol and tiles[4] == player_symbol and tiles[8] == player_symbol:
                return player_symbol
            elif tiles[2] == player_symbol and tiles[4] == player_symbol and tiles[6] == player_symbol:
                return player_symbol

        return False

    def game_over(self, player_symbol):
        print("Игра закончена! Игрок " + player_symbol + "выиграл")


class Checker:
    def __init__(self):
        self.field = None

    def check(self, field):
        self.field = field.cells
        for i in range(3):
            result = self.check_horizontal_line(i)
            if result:
                return result
        for i in range(3):
            result = self.check_vertical_line(i)
            if result:
                return result
        result = self.check_diagonal_line()
        if result:
            return result
        result = self.check_back_diagonal_line()
        if result:
            return result
        return None

    def check_horizontal_line(self, line_id):
        counts = {
            'x': 0,
            'o': 0,
            Field.EMPTY_CELL: 0
        }
        for j in range(3):
            key = self.field[line_id][j]
            counts[key] += 1
        if counts['x'] == 3:
            return 'x'
        if counts['o'] == 3:
            return 'o'
        return None

    def check_vertical_line(self, line_id):
        counts = {
            'x': 0,
            'o': 0,
            Field.EMPTY_CELL: 0
        }
        for j in range(3):
            key = self.field[j][line_id]
            counts[key] += 1
        if counts['x'] == 3:
            return 'x'
        if counts['o'] == 3:
            return 'o'
        return 0

    def check_diagonal_line(self):
        counts = {
            'x': 0,
            'o': 0,
            Field.EMPTY_CELL: 0
        }
        for i in range(3):
            key = self.field[i][i]
            counts[key] += 1
        if counts['x'] == 3:
            return 'x'
        if counts['o'] == 3:
            return 'o'
        return None

    def check_back_diagonal_line(self):
        counts = {
            'x': 0,
            'o': 0,
            Field.EMPTY_CELL: 0
        }
        for i in range(3):
            key = self.field[i][2 - i]
            counts[key] += 1
        if counts['x'] == 3:
            return 'x'
        if counts['o'] == 3:
            return 'o'
        return None


class Player():
        pass

        f = Field(3)
        print(f)
        p = Player()
        f.set_cell(1, 0, 'x')
        print(f)
        f.set_cell(0, 2, 'x')
        f.set_cell(1, 1, 'o')
        f.set_cell(2, 0, 'o')
        f.set_cell(1, 2, 'x')
        f.set_cell(2, 2, 'o')
        f.set_cell(0, 0, 'x')
        print(f)
        print(f.is_cell_empty(1, 0))
        print(f.is_cell_empty(1, 1))
        checker = Checker()
        print(checker.check(f))
