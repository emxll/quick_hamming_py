from ctypes import *
import time

c_lib = CDLL('./hamming.so')

def r_16(f):
    for i in range(2 ** 20):
        f(i)
def r_8(f):
    for _ in range(int(2 ** 20 / 2 ** 8)):
        for i in range(2 ** 8):
            f(i)
def hi_r_16(f):
    for i in range(2 ** 32 - 2 ** 20, 2 ** 32):
        f(i)


def string_conv(v):
    return bin(v)[2:].count('1')

def shr(v):
    c = 0

    c += v & 0x1
    while v != 0:
        v = v >> 1
        c += v & 0x1
    return c

benchmarks = [
    {
        'func': r_16,
        'name': 'Generic range from 0 to 2^16',
        'count': 2 ** 20
    },
    {
        'func': r_8,
        'name': 'Generic range from 0 to 2^8',
        'count': 2 ** 20
    },
    {
        'func': hi_r_16,
        'name': 'Generic range from 2^32 - 2^16 to 2^32',
        'count' : 2 ** 20
    }
]

functions = [
    {
        'func': string_conv,
        'name': 'String conversion',
        'lang': 'Python'
    },
    {
        'func': shr,
        'name': 'Right-shift w/ counter',
        'lang': 'Python'
    },
    {
        'func': c_lib.shr,
        'name': 'Right-shift w/ counter',
        'lang': 'C'
    },
    {
        'func': c_lib.hakmem,
        'name': 'HAKMEM',
        'lang': 'C'
    },
]

def main():
    for b in benchmarks:
        print(f'Running "{b["name"]}"...')
        print()
        for f in functions:
            time_before = time.time()
            b['func'](f['func'])
            time_after = time.time()
            time_total = time_after - time_before
            print(f'"{f["name"]}" in {f["lang"]} finished:')
            print(f'Total time: {time_total}')
            print(f'Time per call: {time_total / b["count"]}')
            print()
        print('-' * 40)
        print()

if __name__ == '__main__':
    main()
