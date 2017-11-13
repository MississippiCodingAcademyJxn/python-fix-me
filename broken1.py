"""Prints a message after a delay"""
import time
import common

def wait_and_print(delay, message):
    """Waits for the given delay and then prints the message"""
    time.sleep(delay / 1000)
    print(message)

def main():
    """Program entry point"""
    print("Welcome Delayed Printing, where we fill all of your printing needs, eventually!")

    message = common.get_response("What would you like to say?")
    seconds = common.get_number_response("How many seconds would you like to wait?")

    print("Sounds great! See you in %i seconds!" % seconds)
    wait_and_print(seconds, message)

if __name__ == "__main__":
    main()
