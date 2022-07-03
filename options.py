from argparse import ArgumentParser
from re import search

parser = ArgumentParser(description="Repetitive notification")
parser.add_argument("-t", "--timer", help="time in seconds for displaying notifications (default 600s [10 min])", type=int)
parser.add_argument("-nt", "--notificationtime", help="time in seconds for the duration of popup notification)", type=int)
parser.add_argument("-cp", "--custompath", help="print list from a custom filepath", type=str)
parser.add_argument("-fn", "--filename", help="file name saved in list directory")
args = parser.parse_args()

if args.custompath:
    file_name = search("(\w+).json$", args.custompath).group(1)
    args.filename = file_name
