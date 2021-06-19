from threading import Timer
import os
from lists import *
from options import *

#variables
timer = 6000
counter = 0

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

def main():
    global timer; global counter
    selection = list_selector()[0]
    if len(selection) == counter: counter = 0
    os.system("notify-send --icon=none \"%s\"" % (selection[counter]))
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
