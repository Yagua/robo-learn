from threading import Timer
from pathlib import Path
from sys import exit
from os import system as exec

import input_file as inp
import options
import utils as utl

# default settings
TIMER = 6_000
POPUP_TIMER = 60
PATH = Path(__file__).resolve().parent / "lists"
ARGS = options.args

class Worker:
    def __init__(self, args, timer, popup_timer, path, counter=0):
        self.args = args
        self.timer = timer
        self.popup_timer = popup_timer
        self.path = path
        self.counter = counter

    def list_selector(self):
        args = self.args
        if args.custompath: return inp.read_json(None, args.custompath)
        elif args.filename: return inp.read_json(self.path, args.filename)
        else:
            print("You need a list to reproduce\nTip: see --help")
            exit(1)

    def start_process(self):
        selection = self.list_selector()
        if len(selection) == self.counter: self.counter = 0
        items = list(selection.items())
        title, body = items[self.counter]
        exec(f'notify-send "{title}" "{body}" -t {self.popup_timer} --icon=none')
        self.counter += 1
        Timer(self.timer, self.start_process).start()

    def show_configuration(self):
        utl.print_template(
            self.timer,
            utl.convert_time(self.popup_timer, "s"),
            self.args.filename
        )

if __name__ == "__main__":
    worker = Worker(
        ARGS,
        ARGS.timer or TIMER,
        utl.convert_time(ARGS.notificationtime or POPUP_TIMER, "m"),
        ARGS.custompath or PATH,
    )
    worker.start_process()
    worker.show_configuration()
