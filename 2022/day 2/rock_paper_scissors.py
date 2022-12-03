from enum import Enum


class Choice(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(Enum):
    Lost = 1
    Draw = 2
    Won = 3


elf_choices = {
    "A": Choice.Rock,
    "B": Choice.Paper,
    "C": Choice.Scissors,
}
player_choices = {
    "X": Choice.Rock,
    "Y": Choice.Paper,
    "Z": Choice.Scissors,
}

need_to = {
    "X": Outcome.Lost,
    "Y": Outcome.Draw,
    "Z": Outcome.Won,
}

round_score = {
    Choice.Rock: 1,
    Choice.Paper: 2,
    Choice.Scissors: 3,
}
outcome_score = {
    Outcome.Lost: 0,
    Outcome.Draw: 3,
    Outcome.Won: 6,
}
beats = {
    Choice.Rock: Choice.Scissors,
    Choice.Paper: Choice.Rock,
    Choice.Scissors: Choice.Paper,
}
beaten_by = {v: k for k, v in beats.items()}


def round(e, p):
    elf = elf_choices[e]
    action = need_to[p]
    # print(f"Elf will {elf} we need to {action}")

    match action:
        case Outcome.Lost:
            our_move = beats[elf]
            # print(f"Lose with {our_move}")
        case Outcome.Won:
            our_move = beaten_by[elf]
            # print(f"Win with {our_move}")
        case _:
            our_move = elf
            # print(f"Draw with {our_move}")

    return our_move


if __name__ == "__main__":
    print("woohoo")
    # fn = "example.txt"
    fn = "live.txt"

    score = 0
    for i, line in enumerate(open(fn, "rt").readlines()):
        e, p = line.strip().split(" ")
        sr = round_score[round(e, p)]
        so = outcome_score[need_to[p]]
        score += sr + so

        # print(f"Round ({i}) {sr} + {so} = {sr+so}, Total: {score}")
    print(score)
