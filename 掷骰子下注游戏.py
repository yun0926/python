#!/usr/bin/env python
#coding:utf-8

import random

def roll_dice(numbers=3,points=None):
    print('<<<<< roll the dice! >>>>>')
    if points is None:
        points = []
    while numbers>0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <=10

    if isBig:
        return 'big'
    elif isSmall:
        return "small"


def start_game():
    your_money = 1000
    while your_money > 0:
        print('<<<<< game start! >>>>>')
        choices = ['big','small']
        your_choice = input('big or small:')

        if your_choice in choices:
            your_bet = int(input('How much you wanna bet? -'))
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if your_bet > your_money:
                print('You have only ',your_money)
            else:
                if youWin:
                    print('The points are' , points , "you win!")
                    print('You gained {}, you have {} now'.format(your_bet,your_money+your_bet))
                    your_money = your_money + your_bet
                else:
                    print('The points are' , points , "you lose!")
                    print('You lost {}, you have {} now'.format(your_bet,your_money-your_bet))
                    your_money = your_money - your_bet
        else:
            print("Invalid Words")
    else:
        print('game over!')

start_game()

