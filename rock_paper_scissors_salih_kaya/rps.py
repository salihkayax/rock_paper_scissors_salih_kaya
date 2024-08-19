import random
print("Rock, paper, scissors is a simple but fun game that can be played by two or more people. -or computer ;)-")
print("Rules: Rock crushes scissors. Scissors cuts paper. Paper covers rock.")
def rock_paper_scissors_salih_kaya():
    player_wins = 0
    computer_wins = 0
    game_count = 0


    while True:
        round_count = 0
        game_count += 1
        print(f"\nNew game started! (Game number: {game_count})")


        while True:  # This loop continues until one player reaches 2 points
            round_count += 1
            print(f"\nRound {round_count}:")

            player_choice = input("Choose rock, paper, or scissors (rock/paper/scissors): ").lower()
            while player_choice not in ['rock', 'paper', 'scissors']:
                player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

            computer_choice = random.choice(['rock', 'paper', 'scissors'])

            print(f"You: {player_choice}, Computer: {computer_choice}")

            if player_choice == computer_choice:
                print("Draw!")
            elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                 (player_choice == 'paper' and computer_choice == 'rock') or \
                 (player_choice == 'scissors' and computer_choice == 'paper'):
                print("You win!")
                player_wins += 1
                if player_wins == 2:
                    print("You won this round!")
                    break
            else:
                print("Computer wins!")
                computer_wins += 1
                if computer_wins == 2:
                    print("Computer won this round!")
                    break


        if player_wins == 2:
            print("You won the game!")
        elif computer_wins == player_wins:
            print("draw")
        else:
            print("Computer won the game!")

        player_wants_to_continue = input("Play again? (y/n): ").lower()
        computer_wants_to_continue = random.choice(['y', 'n'])
        if player_wants_to_continue != 'y' or computer_wants_to_continue != 'y':
            break

    print(f"\nTotal number of games: {game_count}")
    print(f"Your wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")

rock_paper_scissors_salih_kaya()