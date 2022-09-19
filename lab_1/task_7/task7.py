import re

def find_shortest(l):
    return min([len(x) for x in re.split('[^a-zA-Z]', l) if x], default=0)
