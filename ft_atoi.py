#!/usr/bin/env python

def ft_atoi(str):
    length = 0
    i = 0
    sign = 1
    number = []
    while str[length:]:
        length += 1
    while str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\v' or str[i] == '\f':
        i += 1
    if str[i] == '-' or str[i] == '+':
        sign = -1 if str[i] == '-' else 1
        i += 1
    while str[i].isdigit():
        number.append(str[i])
        i += 1
    try:
        return int(''.join(number)) * sign
    except (TypeError, ValueError, AttributeError):
        return