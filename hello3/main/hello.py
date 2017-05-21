"""
Just say hello
"""


def hello_oxford():
    """
    Say hello
    """
    words = ["Hello", "University", "of", "Oxford"]
    counter = 0
    max_length = len(words) - 1
    while counter <= max_length:
        word = words[counter]
        #import pdb
        #pdb.set_trace()
        print(word + "!")
        counter = counter+1
    print("Bye!")

if __name__ == '__main__':
    hello_oxford()
