import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'godmode'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0
    max_rounds = 5

    print("\n🎮 Rock Paper Scissors - Best of 5 Mode!")
    print("Type 'godmode' to always win 😈")
    print("Type 'exit' anytime to quit.\n")

    while rounds < max_rounds:
        user = input("👉 Your choice (rock/paper/scissors): ").lower()
        if user == 'exit':
            print("🚪 Game exited.")
            break
        if user not in ['rock', 'paper', 'scissors', 'godmode']:
            print("⚠️ Invalid choice. Try again!\n")
            continue

        computer = get_computer_choice()
        print(f"🤖 Computer chose: {computer}")

        result = decide_winner(user, computer)
        if result == 'tie':
            print("⚖️ It's a tie!")
        elif result == 'user':
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        rounds += 1
        print(f"📊 Score: You {user_score} - {computer_score} Computer\n")

    print("🏁 Final Result:")
    if user_score > computer_score:
        print("🎉 YOU WIN THE GAME!")
    elif computer_score > user_score:
        print("💀 COMPUTER WINS THE GAME!")
    else:
        print("😬 IT'S A DRAW!")

if __name__ == "__main__":
    play_game()
