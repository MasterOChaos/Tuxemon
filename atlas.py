import sys
from tuxemon.atlas import npcatlas
import argparse

parser = argparse.ArgumentParser(description='Choose an option')
parser.add_argument('--mh', '--makehuman', dest='mkhuman', action='store_true',
                    help='Make the json files human readable')

args = parser.parse_args()

if(args.mkhuman == 1):
    npcatlas.humanread()
    sys.exit()
else:
    npcatlas.make()
    sys.exit()
