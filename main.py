from threading import Timer
from pathlib import Path
import input_file as inp
import options
import utils

#variables
args = options.args
timer = 6000
popup_timer = 60
counter = 0
home = Path(__file__).parent / "lists"

#list selector
def list_selector():
    global args; global home
    if args.filepath: return inp.read_json(args.filepath, home)
    elif args.custompath: return inp.read_json(args.custompath, None)
    else: print("You need a list to reproduce\nTip: see --help"); utils.sys_exit()

#overrite timers and home or take the default values
timer = args.timer or timer
popup_timer = utils.convert_time(args.notificationtime or popup_timer, "m")
home = args.custompath or home

#main function
def main():
    global timer; global counter
    selection = list_selector()
    if len(selection) == counter: counter = 0
    utils.sys_command("notify-send -t %d --icon=none \"%s\""
            % (popup_timer, selection[counter]))
    counter += 1
    Timer(timer, main).start()

#start
main()
utils.print_template(
    utils.exc_message,
    timer,
    utils.convert_time(popup_timer, "d"),
    args.filepath
)
