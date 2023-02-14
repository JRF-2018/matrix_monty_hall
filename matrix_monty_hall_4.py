# -*- coding: utf-8 -*-
__version__ = '0.0.3' # Time-stamp: <2023-02-14T13:33:48Z>
## Language: Japanese/UTF-8

import random
import numpy as np

## 中平氏の枠組みでは、アリスがプレイヤー、ボブがモンティ(司会者)の役
## ということになる。

## 「正解」が0番目であるときの行列を f0、ボブの行列を g0 とする。
tmp0 = random.random()
tmp1 = random.random()
tmp2 = random.random()
tmp = tmp0 + tmp1 + tmp2
p0 = tmp0 / tmp
p1 = tmp1 / tmp
p2 = tmp2 / tmp
## 中平氏の主張(?)。
f0 = np.array([[p0, p0, p0],
               [p1, p1, p1],
               [p2, p2, p2]])
## 私の思うもの。
f0_1 = np.array([[1/3, 1/3, 1/3],
                 [1/3, 1/3, 1/3],
                 [1/3, 1/3, 1/3]])

## ボブのランダムに選ぶときの確率を p_b とする。
p_b = random.random()
## 中平氏の主張。
g0 = np.array([[0, 1, 1],
               [p_b, 0, 0],
               [1-p_b, 0, 0]])

## 整数乱数表現をベクトル表現に直す。
def int_vectorize(radix, i):
    r = np.array(np.zeros(radix))
    r[i] = 1
    return r


def calc_prob_a(mat, car0):
    r = np.dot(mat, int_vectorize(3, 0)) * int_vectorize(3, 0) \
        * car0
    return np.sum(r)


def calc_prob_b(g0, f0, car0):
    a = np.dot(f0, int_vectorize(3, 0))
    r = np.dot(g0, a) * int_vectorize(3, 0) \
        * car0
    return np.sum(r)

if __name__ == "__main__":
    ## アリスが選択を変えなかったときの確率
    print(calc_prob_a(f0, 1))
    ## ボブのものを選択したときの確率
    print(calc_prob_b(g0, f0, 1))
    ## アリスが選択を変えなかったときの確率
    print(calc_prob_a(f0_1, 1))
    ## ボブのものを選択したときの確率
    print(calc_prob_b(g0, f0_1, 1))

## 答えは次のように表示される。
##
## 0.41378870734983825
## 0.5862112926501617
## 0.3333333333333333
## 0.6666666666666666
