# coding: utf-8
__author__ = 'yorick'

import random
import pickle


def generator():
    """
    this function generate random numbers for diceware password generator
    """
    one = random.randint(1, 6)
    two = random.randint(1, 6)
    three = random.randint(1, 6)
    four = random.randint(1, 6)
    five = random.randint(1, 6)
    x = str(one) + str(two) + str(three) + str(four) + str(five)
    return x


def loader():
    """
    this function load the dict of diceware words and keys
    """
    opf = 'files/dict.dll'
    f = open(opf, 'rb')
    d = pickle.load(f)
    return d


def voider(do):
    """
    this function generate password on method diceware
    """
    p = [generator() for x in range(0, do)]
    di = loader()
    en = ''
    for x in p:
        en += di[x] + ' '
    return en


def strenght_middle(s):
    """
    this function do password more strenght
    """
    p = str(s)
    del s
    p = p.replace('a', '@')
    p = p.replace('o', '(_)')
    p = p.replace('you', "'u'")
    p = p.replace(' ', '"')
    p = p[0:len(p)-1]
    return p


def strength_hard(s):
    """
    this function do password very big strength
    """
    p = strenght_middle(s)
    p = p.replace('t', 'Y')
    p = p.replace('i', 'T')
    p = p.replace('for', '4')
    p = p.replace('s', '$')
    p = p.replace('j', 'R')
    p = p.replace('s', 'Z')
    return p

