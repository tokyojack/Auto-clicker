from random import uniform
from time import sleep

from keyboard import is_pressed
from mouse import click

while True:
    if is_pressed('esc'):
        print("Program cancelled")
        break

    if not is_pressed('a'):
        continue

    click(button='left');
    sleep(uniform(0.05, 0.1))
