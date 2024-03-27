import random

def play_guessing_game():
  """
  Runs a single round of the guessing game.

  Returns:
    None
  """

  # Generate a random number between 1 and 10
  hidden_number = random.randint(1, 10)

  # Initialize a variable to track if the user guessed correctly
  guessed_correctly = False

  # Loop for 3 chances
  for attempt in range(3):
      # Get user input with error handling
      while True:
          try:
              user_guess = int(input(f"Attempt {attempt + 1}: Guess the hidden number (between 1 and 10): "))
              if 1 <= user_guess <= 10:
                  break
              else:
                  print("Invalid guess. Please enter a number between 1 and 10.")
          except ValueError:
              print("Invalid guess. Please enter a number.")

      # Check if the guess is correct
      if user_guess == hidden_number:
          print("Congratulations! You guessed the correct number.")
          guessed_correctly = True
          break
      else:
          if user_guess < hidden_number:
              print("Hint: Higher")
          else:
              print("Hint: Lower")

  # Display success or failure message and offer play again option
  if guessed_correctly:
      print("You won!")
  else:
      print(f"Sorry, you ran out of chances. The hidden number was: {hidden_number}")

  while True:
      play_again = input("Do you want to play again? (yes/no/exit): ").lower()
      if play_again in ("yes", "no"):
          if play_again == "yes":
              # Restart the game by calling the function again
              play_guessing_game()
              break
          else:
              print("Thanks for playing!")
              break
      elif play_again == "exit":
          print("Exiting the game...")
          break
      else:
          print("Invalid choice. Please enter yes, no, or exit.")

if __name__ == "__main__":
  print("Welcome to the Guessing Game!")
  play_guessing_game()
