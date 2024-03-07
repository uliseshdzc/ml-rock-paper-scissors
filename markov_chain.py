import itertools
from random import randint


class MarkovChain:

    def __init__(self, labels: list[str], n_states: int = 1):
        # Initialize object by getting all posible labels of previous modes
        # and by initializing to 0 the occurrences matrix
        self.n_states = n_states
        self.labels = labels
        self.prev_moves_labels = list(
            map(''.join, itertools.product(labels, repeat=n_states)))
        self.transition_matrix = [[0] * len(labels)
            for _ in range(len(self.prev_moves_labels))]
        self.opponent_history = []

    def update(self, new_move):
        # Update Markov chain if there is enough data
        if len(self.opponent_history) >= self.n_states:
            prev_moves = self.opponent_history[-self.n_states:]
            
            # Increase by 1 the occurrence of the new move
            self.transition_matrix[self.prev_moves_labels.index(
                ''.join(prev_moves))][self.labels.index(new_move)] += 1

		# Insert new move into history
        self.opponent_history.append(new_move)
        
    def predict(self):
        # Return random move if there are not enough previous moves
        if len(self.opponent_history) < self.n_states:
            return self.labels[randint(0, len(self.labels) - 1)]

        prev_moves = self.opponent_history[-self.n_states:]

        # Get all indices with most occurrences
        occurrences_for_move = self.transition_matrix[self.prev_moves_labels.index(
            ''.join(prev_moves))]
        indexes = [i for i in range(0, len(occurrences_for_move)) 
            if occurrences_for_move[i] == max(occurrences_for_move)]

        # Get a winning move by predicting the opponent play
        # Return a random choice if there are two moves with the same probability
        opponent_move_prediction = self.labels[indexes[randint(0, len(indexes) - 1)]]
        return opponent_move_prediction