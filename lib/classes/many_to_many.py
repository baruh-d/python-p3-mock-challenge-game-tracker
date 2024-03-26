class Game:
    all = []

    def __init__(self, title=None):
        self._title = None
        self._game_started = False
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title is not None:
            if not isinstance(title, str) or len(title) < 1:
                raise ValueError("Title must be a non-empty string")
            if hasattr(self, '_game_started') and self._game_started:
                raise AttributeError("Title cannot be changed after the game has started")
        self._title = title

    def start_game(self):
        self._game_started = True

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        players_list = set([result.player for result in Result.all if result.game == self])
        return list(players_list)

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.game == self and result.player == player]
        if not scores:
            return 0
        return sum(scores) / len(scores)


class Player:
    all = []

    def __init__(self, username):
        self._username = None
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if len(username) < 2 or len(username) > 16:
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games_list = set([result.game for result in Result.all if result.player == self])
        return list(games_list)

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in Result.all if result.player == self and result.game == game)


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = None
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise TypeError("Score must be an integer")
        if score < 1 or score > 5000:
            raise ValueError("Score must be between 1 and 5000")
        self._score = score

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Player must be an instance of Player class")
        self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise TypeError("Game must be an instance of Game class")
        self._game = game
