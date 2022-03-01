#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {'1a': '19', '3б': '15', '4в': '23', '5a': '18'}
    sum = 0

    for i in school:
        sum += int(school[i])

    print(f"Общее количество учащихся: {sum}")