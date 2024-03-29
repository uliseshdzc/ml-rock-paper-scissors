from enum import Enum


class Result(Enum):
    WIN = 1
    TIE = 0
    LOSE = -1

    def __str__(self):
        match self:
            case Result.WIN:
                return "You win!"
            case Result.TIE:
                return "It's a tie"
            case Result.LOSE:
                return "You lose"            