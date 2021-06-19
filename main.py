from threading import Timer
from pathlib import Path
import input_file as inp
import options
import utils

#variables
args = options.args
timer = 6000
popup_timer = utils.convert_time(60, "m")
counter = 0
home = Path(__file__).parent / "lists"

#list selector
def list_selector():
    global args; global home
    if args.filepath: return inp.read_json(args.filepath, home)
    else: print("you need pass a file name"); utils.sys_exit()

#overrite timers and -fp to -t and -nt options or take the default values
timer = args.timer or timer
popup_timer = utils.convert_time(args.notifitm, "m") or popup_timer
home = not args.filepath or home

def main():
    global timer; global counter
    selection = list_selector()
    if len(selection) == counter: counter = 0
    utils.sys_command("notify-send -t %d --icon=none \"%s\""
            % (popup_timer, selection[counter]))
    counter += 1
    Timer(timer, main).start()

main()
utils.print_template(utils.exc_message, timer, popup_timer, args.filepath)
