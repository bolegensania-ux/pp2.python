"""
with open("../sample.txt", "w") as f:
    f.write("hi! This is my sample file. \n")
    f.write("this is a text for the song by TS called: this is me trying. \n")
"""


with open("../sample.txt", "a") as f:
    f.write("I've been having a hard time adjusting,\n")
    f.write("I've had the shiniest wheels now they're rusting.\n")






with open("../sample.txt", "r") as f:
    print(f.read())