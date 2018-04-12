from random import uniform
from time import sleep

from keyboard import is_pressed
from mouse import click

def startClicking():
    while True:
        if is_pressed('esc'):
            print("Program cancelled")
            break

        if not is_pressed('a'):
            continue

        click(button='left');
        sleep(uniform(0.05, 0.1))

if __name__ == '__main__':
    startClicking()
