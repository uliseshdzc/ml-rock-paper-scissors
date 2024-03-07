import re
from markov_chain import MarkovChain
from result import Result

WINNNING_MOVE = {'R': 'P', 'P': 'S', 'S': 'R'}
LABELS = ['R', 'P', 'S']
markov_chain = MarkovChain(LABELS, n_states=3)

def play(player_move: str, computer_move: str, score: dict) -> Result:
    result = None

    if player_move == computer_move:
        result = Result.TIE    
    elif WINNNING_MOVE[computer_move] == player_move:
        result = Result.WIN
    else:
        result = Result.LOSE
    
    score[result] += 1
    return result
    
def main():
    n_round = 1
    score = {r:0 for r in Result}

    try:
        while True:
            print('ROUND {round}'.format(round = n_round))
            player_move = input('Enter your move: ')
            player_move = player_move.upper()

            if not re.match('^[rps]$', player_move, re.IGNORECASE):
                print('Incorrect input, please enter one of these three values: {labels}.\n'
                      .format(labels = LABELS)) 
                continue
            
            computer_move = WINNNING_MOVE[markov_chain.predict()]
            print('The computer plays: {move}'.format(move = computer_move))

            result = play(player_move, computer_move, score)
            print('{result}\n'.format(result = result))

            n_round += 1
            markov_chain.update(player_move)

    except KeyboardInterrupt:
        rounds_without_ties = score[Result.WIN] + score[Result.LOSE]
        p_win_rate = 0 if rounds_without_ties == 0 else score[Result.WIN] / rounds_without_ties * 100
        c_win_rate = 0 if rounds_without_ties == 0 else 100 - p_win_rate

        print('\n\nGame ended. Score: {wins} wins, {ties} ties and {loses} loses'
              .format(wins = score[Result.WIN], ties = score[Result.TIE], loses = score[Result.LOSE]))
        print('\nYour win rate: {p_win_rate:.2f}%\nComputer win rate: {c_win_rate:.2f}%'
              .format(p_win_rate = p_win_rate, c_win_rate = c_win_rate))

if __name__ == "__main__":
    main()