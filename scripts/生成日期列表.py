import datetime
from argparse import ArgumentParser

n = 10
d = datetime.datetime.now()
delta = datetime.timedelta(days = 1)

parser = ArgumentParser()
parser.add_argument('--days', help='generate number of days', type=int, default=10)
    
args = parser.parse_args()
i = 0
while i < args.days:
    print("\"%s\"" % (d.strftime("%Y-%m-%d")), end=",")
    d += delta
    i += 1
print()    