import os
from typing import List, Union
import random 

# Create a class named hangman 
class Hangman():
    """ This is Hangman Game, here you need to guess the correct word"""
    

    def __init__(self): 
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']

         # pick a word from the list 
        self.word_to_find = random.choice(self.possible_words)

        #Dashes for each letter in the word. Means length must be same
        self.correctly_guessed_letters = "_" * len(self.word_to_find)  
        self.well_guessed_letter = [] 
        self.wrongly_guessed_letters = []           # list of string whic are wrongly guessed by player
       
        self.lives = 5
        self.turn_count = 0                         #the number of turns played by the player
        self.error_count = 0                        #the number of errors made by the player



        
    def play(self):
        print("Welcome to Hangman game")
        print("Try to guess the word letter by letter")

        # This loop will run untill error_count = lives  
        while self.error_count < self.lives and self.correctly_guessed_letters != self.word_to_find: 
            print("The word is till guessed :", self.correctly_guessed_letters)
            
            guess = input("Enter your guessed letter :")

            self.turn_count += 1 

            # check the guess wheather it is correct or not
            if guess in self.word_to_find:
                print("Wells guessed letter")
                self.well_guessed_letter.append(guess)
       
                # to fill dashes with correct guessed letter at the place 
                new_current_guess = ""
                for letter in range(len(self.word_to_find)):
                    if guess == self.word_to_find[letter]:
                        new_current_guess += guess
                    else: 
                        new_current_guess += self.correctly_guessed_letters[letter]
        
                self.correctly_guessed_letters = new_current_guess

            else:
                print("bad guessed letters")
                self.wrongly_guessed_letters.append(guess)
                self.error_count += 1
            return self.start()

        return self.start()
    
    def game_over(self):
        """ The game will stop when error_count = lives means you have used your all lives"""

        if self.error_count == self.lives:
            print("game over")
            print("Correct word is:", self.word_to_find)
        
        else:
            return self.well_played()
    
    def well_played(self):

        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")


    def start(self):
        print("\n")
        print("Lives remaining are :", (self.lives - self.error_count))
        print("List of well guessed letters :", self.well_guessed_letter)
        print("List of wrongly guesses letters are :", self.wrongly_guessed_letters)
        print("Number errors made by the player :", self.error_count)
        print("Number of turns played by the player :", self.turn_count)
        print("\n")
        if self.error_count == self.lives and self.correctly_guessed_letters != self.word_to_find:
            return self.game_over()
        
        elif self.error_count < self.lives and self.correctly_guessed_letters != self.word_to_find:
            return self.play()
        else:
            return self.well_played()









    
 