class Node:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

def ask_question(node):
    # If we reach a leaf node (final answer)
    if not isinstance(node.yes, Node) and not isinstance(node.no, Node):
        # Display the question and get user response
        while True:
            response = input(node.question + " (yes/no): ").strip().lower()
            if response in ["yes", "y"]:
                print("Your answer is: " + node.yes + "!")
                return
            elif response in ["no", "n"]:
                print("Your answer is: " + node.no + "!")
                return
            else:
                print("Invalid response. Please answer with 'yes' or 'no'.")
    else:
        # For intermediate nodes in the decision tree
        while True:
            response = input(node.question + " (yes/no): ").strip().lower()
            if response in ["yes", "y"]:
                if isinstance(node.yes, Node):
                    ask_question(node.yes)
                else:
                    print("Your answer is: " + node.yes + "!")
                return
            elif response in ["no", "n"]:
                if isinstance(node.no, Node):
                    ask_question(node.no)
                else:
                    print("Your answer is: " + node.no + "!")
                return
            else:
                print("Invalid response. Please answer with 'yes' or 'no'.")

# Decision tree construction
tree = Node("Is it an animal?",
            Node("Can it fly?",
                 Node("Is it nocturnal?",
                      "Bat",
                      "Eagle"),
                 Node("Is it domestic?",
                      "Dog",
                      "Lion")),
            Node("Is it a technological object?",
                 Node("Is it a phone?",
                      "iPhone",
                      "Computer"),
                 Node("Is it used for transportation?",
                      "Car",
                      "Bicycle")))

# Start the game
print("Think of something and I'll try to guess what it is.")
print("Answer my questions with 'yes' or 'no'.")
ask_question(tree)

# Ask if they want to play again
while True:
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        print("\nThink of something new and I'll try to guess what it is.")
        ask_question(tree)
    elif play_again in ["no", "n"]:
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid response. Please answer with 'yes' or 'no'.")