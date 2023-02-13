# -*- coding: utf-8 -*-
__version__ = '0.0.1' # Time-stamp: <2023-02-13T17:24:33Z>
## Language: Japanese/UTF-8

import random
import numpy as np

first_choice_matrix = None
monty_matrix = None


## パーセプトロンで使うステップ関数。
def step_function (x):
    return np.array(x > 0, dtype=int)

## 整数乱数表現をベクトル表現に直す。
def int_vectorize(radix, i):
    r = np.array(np.zeros(radix))
    r[i] = 1
    return r

## 乱数の組をベクトル表現に直す。
def monty_vector3 (car, first_choice, monty_choice):
    return np.hstack([int_vectorize(3, car),
                      int_vectorize(3, first_choice),
                      int_vectorize(2, monty_choice)])


## モンティ・ホール問題の実計算は次で行っている。
def check3(car, first_choice, monty_choice):
    if car == first_choice:
        true_monty_choice = car + 1 + monty_choice
        if true_monty_choice > 2:
            true_monty_choice -= 3
    else:
        true_monty_choice = car
    return (first_choice == car, true_monty_choice == car)


## モンティ・ホール問題のプレイヤーによる選択のままでいった場合の行列と、
## モンティ(司会者)が残したほうを選択した場合の行列を求める。
def make_monty_matrix():
    global first_choice_matrix, monty_matrix
    ftmp = []
    mtmp = []
    for car in range(3):
        for first_choice in range(3):
            for monty_choice in range(2):
                f, m = check3(car, first_choice, monty_choice)
                q = monty_vector3(car, first_choice, monty_choice)
                if f:
                    ftmp.append(q)
                if m:
                    mtmp.append(q)
    first_choice_matrix = np.array(ftmp)
    monty_matrix = np.array(mtmp)


## 次がメインルーチンになる。ここが行列的にした「プロセス」
## という私の理解。基本的に「パーセプトロン」である。
def calc_process_1(q):
    return np.sum(step_function(np.dot(first_choice_matrix, q) - 2.5)),\
        np.sum(step_function(np.dot(monty_matrix, q) - 2.5))

def calc_process(q):
    ftmp = 0
    mtmp = 0
    for car in range(3):
        for first_choice in range(3):
            for monty_choice in range(2):
                q1 = monty_vector3(car, first_choice, monty_choice)
                f, m = calc_process_1(q1)
                ## ただし、次のように論理積的な演算は使ってしまうので、
                ## 行列的というのにも疑問符がつく。
                ftmp += f * q[car]*q[3 + first_choice]*q[3 + 3 + monty_choice]
                mtmp += m * q[car]*q[3 + first_choice]*q[3 + 3 + monty_choice]
    return ftmp, mtmp


if __name__ == "__main__":
    make_monty_matrix()
    f, m = calc_process([1/3, 1/3, 1/3, 1/3, 1/3, 1/3, 1/2, 1/2])
    print(f, m)

## 答えは 0.33333333333333337 0.6666666666666669 と表示される。
