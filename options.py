import argparse

#options
parser = argparse.ArgumentParser(description="Learn english robot")
parser.add_argument("-d", "--days", help="print the days of the week", action="count")
parser.add_argument("-ws", "--wsentences", help="print sentences with words (default)", action="count")
parser.add_argument("-vs", "--vsentences", help="print sentences with verbs", action="count")
parser.add_argument("-ps", "--psentences", help="print sentences phrasal verbs", action="count")
parser.add_argument("-m", "--months", help="print the months of the year", action="count")
parser.add_argument("-b", "--body", help="print body parts", action="count")
parser.add_argument("-t", "--timer", help="time in seconds for displaying notifications (default 600s [10 min])", type=int)
parser.add_argument("-nt", "--notifitm", help="time in seconds for the duration of popup notification)", type=int)
args = parser.parse_args();

