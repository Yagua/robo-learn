import argparse

#options
parser = argparse.ArgumentParser(description="Learn english robot")
parser.add_argument("-t", "--timer", help="time in seconds for displaying notifications (default 600s [10 min])", type=int)
parser.add_argument("-nt", "--notifitm", help="time in seconds for the duration of popup notification)", type=int)
parser.add_argument("-cp", "--custompath", help="print list from custom filepath")
parser.add_argument("-fp", "--filepath", help="file")
args = parser.parse_args();
