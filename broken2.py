"""Small program to simulate rolling a d6 over and over again"""
import random
import time
import common

def random_die_sound():
    """Returns a random noise that a die might make"""

    return random.choice([
        "bump",
        "clack",
        "clatter",
        "rap"
    ])

def roll_d6():
    """Returns a random six sided die roll"""

    return random.randint(0, 6)

def main():
    """Main function of the program."""

    while common.get_response("Roll, or quit? (R/q) ").lower().strip() == "r":
        print("Rolling the die...")

        for _ in range(4):
            time.sleep(0.5)
            print(random_die_sound())

        time.sleep(0.5)

        print("And the result is...")
        print("%i!" % roll_d6())
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
