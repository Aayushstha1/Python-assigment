import sys
from time import sleep

def print_lyrics():
    lines = [
        ("she gives me love", 0.07),
        ("she gives me love", 0.07),
        ("she gives me love", 0.07),
        ("she gives me love", 0.07),
        ("she gives me love", 0.07),
    ]
    delays = [0.06, 0.3, 0.3,0.3,0.3]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        print('')  # Move to a new line after each line of lyrics
        sleep(delays[i])  # Delay between each line

print_lyrics()
