import math
from colorama import Fore, init as colorama_init
colorama_init()

punctuations = '，。？！、 ,.?!'
char_count = {}
char_freq = {}

test_line = '早安你好'

with open('table.txt') as fp:
    s = 0
    for i in fp:
        char, count = i.split(',')
        count = int(count, 10)
        char_count[char] = count
        s += count

for char, count in char_count.items():
    char_freq[char] = count / s * 100

ranks = [
    (0.2, Fore.GREEN), # Top 100
    (0.1, Fore.WHITE), # Top 200
    (0.08, Fore.YELLOW), # Top 300
    (0.005, Fore.RED), # Top 500
    (0.0, Fore.MAGENTA), # Still in dict
    (-math.inf, Fore.BLUE), # Even not in dict
]

def get_color(freq):
    for f, c in ranks:
        if freq > f:
            return c

    raise ValueError(freq)

def print_line(s):
    for c in s:
        if c in punctuations or ord(c) in range(0x20, 0x7f):
            print(Fore.GREEN + c, end='')
        else:
            freq = char_freq.get(c, -1)
            print(get_color(freq) + c, end='')
    print(Fore.RESET)

print_line(test_line)

while s := input(' > ').strip():
    print_line(s)

