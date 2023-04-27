## Group Members
# Jyothi Bhoomireddy
# Prathyusha Boinapally
# Bhanu Prakash Gadupudi
# Durga Chandra Vamsi Katiki
# Nikhil Veggalam

#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(word, 1)