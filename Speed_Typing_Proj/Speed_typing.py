import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!\n")
    stdscr.addstr("Choose a difficulty level:\n")
    stdscr.addstr("1. Easy\n")
    stdscr.addstr("2. Medium\n")
    stdscr.addstr("3. Hard\n")
    stdscr.addstr("Press 1, 2, or 3 to choose.\n")
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        if key in ("1", "2", "3"):
            return int(key)

def display_text(stdscr, target, current, wpm=0, accuracy=100):
    stdscr.addstr(0, 0, target, curses.color_pair(3))
    stdscr.addstr(1, 0, f"WPM: {wpm}   Accuracy: {accuracy:.2f}%", curses.color_pair(3))

    for i, char in enumerate(current):
        correct_char = target[i] if i < len(target) else ""
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def countdown(stdscr):
    stdscr.clear()
    for i in range(3, 0, -1):
        stdscr.addstr(0, 0, f"Starting in {i}...", curses.A_BOLD)
        stdscr.refresh()
        time.sleep(1)
        stdscr.clear()

    stdscr.addstr(0, 0, "GO!", curses.A_BOLD)
    stdscr.refresh()
    time.sleep(1)
    stdscr.clear()

def load_text(level):
    filename = {1: "easy.txt", 2: "medium.txt", 3: "hard.txt"}[level]
    with open(filename, "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def calculate_accuracy(target, current):
    correct = sum(1 for i, char in enumerate(current) if i < len(target) and char == target[i])
    return (correct / len(current)) * 100 if current else 0

def wpm_test(stdscr, target_text):
    current_text = []
    countdown(stdscr)
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = time.time() - start_time
        wpm = round((len(current_text) / 5) / (time_elapsed / 60))
        accuracy = calculate_accuracy(target_text, current_text)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, accuracy)
        stdscr.refresh()

        if len(current_text) >= len(target_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    return wpm, accuracy

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # correct
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # incorrect
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # neutral

    while True:
        level = start_screen(stdscr)
        target = load_text(level)
        wpm, accuracy = wpm_test(stdscr, target)

        stdscr.clear()
        stdscr.addstr(f"\nFinished!\n")
        stdscr.addstr(f"Your WPM: {wpm}\n")
        stdscr.addstr(f"Accuracy: {accuracy:.2f}%\n")
        stdscr.addstr("Press 'r' to retry or ESC to quit.")
        stdscr.refresh()

        key = stdscr.getkey()
        if key.lower() != 'r':
            break

wrapper(main)
