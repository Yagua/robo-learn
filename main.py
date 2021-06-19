from threading import Timer
import os
from lists import *
from options import *

#variables
timer = 6000
popup_timer = 60
counter = 0

def seconds_to_miliseconds(value):
    if value == None: return
    result = 0
    result = value * 1000
    return result

#list selector
def list_selector():
    global args
    if args.days: return [DAYS, "Days"]
    elif args.months: return [MONTHS, "Months"]
    elif args.body: return [BODY, "Body"]
    elif args.vsentences: return [V_SENTENCES, "Verbs Sentences"]
    elif args.psentences: return [P_SENTENCES, "Phrasal verbs Sentences"]
    else: return [W_SENTENCES, "Words Sentences (default)"]

#overrite TIMER to --TIMER argument or take the default value
timer = args.timer or timer
popup_timer = seconds_to_miliseconds(args.notifitm) or popup_timer

def main():
    global timer; global counter
    selection = list_selector()[0]
    if len(selection) == counter: counter = 0
    os.system("notify-send -t %d --icon=none \"%s\""
            % (popup_timer, selection[counter]))
    counter += 1
    Timer(timer, main).start()

template = """%s
Current options:
  Timer: %ds
  List Selected: %s

Executing...
""" % (exc_message, timer, list_selector()[1])
print(template)

main()
