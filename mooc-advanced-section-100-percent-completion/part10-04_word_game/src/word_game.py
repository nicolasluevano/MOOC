# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        player1_word_len = len(player1_word)
        player2_word_len = len(player2_word)

        if player1_word_len == player2_word_len:
            pass
        elif player1_word_len > player2_word_len:
            return 1
        else:
            return 2


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ['a', 'e', 'i', 'o', 'u']
        player1_vowels = []
        player2_vowels = []

        for letter in player1_word:
            if letter in vowels:
                player1_vowels.append(letter)

        for letter in player2_word:
            if letter in vowels:
                player2_vowels.append(letter)

        if len(player1_vowels) == len(player2_vowels):
            pass
        elif len(player1_vowels) > len(player2_vowels):
            return 1
        else:
            return 2



class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)


    def round_winner(self, player1_word: str, player2_word: str):
        valid_words = ['rock', 'paper', 'scissors']
        if player1_word in valid_words and player2_word in valid_words:
            if player1_word == player2_word:
                pass
            elif player1_word == 'rock' and player2_word == 'scissors':
                return 1
            elif player1_word == 'paper' and player2_word == 'rock':
                return 1
            elif player1_word == 'scissors' and player2_word == 'paper':
                return 1
            else:
                return 2
        elif player1_word not in valid_words and player2_word not in valid_words:
            pass
        elif player1_word in valid_words and player2_word not in valid_words:
            return 1
        else:
            return 2

