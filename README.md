# Machine Learning: Rock-Paper-Scissors
This project is an implementation of [Markov chains](https://en.wikipedia.org/wiki/Markov_chain). I intend to prove the usefulness of Machine Learning in some tasks such as prediction. I try to show as well that it can be pretty easy to program this kind of algorithms.

The solution is composed by three main files:
1. `result.py`: `Enum` with the three possible results and their conversion to `string`.
2. `markov_chain.py`: This is the class that defines the whole algorithm. It includes the constructor that initializes the transition matrix, the opponent history array and an array with the possible previous moves. It also has the functions `update` (in order to amend the new moves of the player and allow the machine to learn) and `predict` (this method returns what the machine thinks the player is going to choose as the next move).
3. `main.py`: This file provides a CLI to be able to play against the machine.


# How to run this project?
1. [Install Python](https://www.python.org/downloads/) (I used Python 3.12.0 for this project).
2. Once it is installed, clone the project to your local repository.
3. You can then run it via the terminal or an IDE by using the command:
```bash
python main.py
```
The game should start. Type the key `R` (rock), `P` (paper) or `S` (scissors) and then press enter to confirm your choice (the game is not case sensitive).
```
ROUND 1
Enter your move: 
```
Have fun playing against the machine!
```
ROUND 1
Enter your move: R
The computer plays: R
It's a tie

ROUND 2
Enter your move: P
The computer plays: S
You lose

ROUND 3
Enter your move: S
The computer plays: S
It's a tie
```
Press `CTRL+C` to finish the game and retrieve your results.
```
Game ended. Score: 6 wins, 10 ties and 9 losses

Your win rate: 40.00%
Computer win rate: 60.00%
```