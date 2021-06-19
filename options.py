import argparse

#options
parser = argparse.ArgumentParser(description="Repetitive notification")
parser.add_argument("-t", "--timer", help="time in seconds for displaying notifications (default 600s [10 min])", type=int)
parser.add_argument("-nt", "--notificationtime", help="time in seconds for the duration of popup notification)", type=int)
parser.add_argument("-cp", "--custompath", help="print list from a custom filepath", type=str)
parser.add_argument("-fp", "--filepath", help="file name saved in list directory")
args = parser.parse_args();
