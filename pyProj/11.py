#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dict1 = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four'
    }
    dict2 = {}
    for x, y in dict1.items():
        dict2.setdefault(y, x)
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")