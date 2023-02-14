# -*- coding: utf-8 -*-
__version__ = '0.0.3' # Time-stamp: <2023-02-14T13:32:42Z>
## Language: Japanese/UTF-8

import random
import numpy as np

## 中平氏の枠組みでは、アリスがプレイヤー、ボブがモンティ(司会者)の役
## ということになる。

## アリスが 0番目を指定したときの行列を f0、ボブの行列を g0 とする。
f0 = np.array([[1, 1, 1],
               [0, 0, 0],
               [0, 0, 0]])
## ボブのランダムに選ぶときの確率を p_b とする。
p_b = random.random()
## 中平氏の主張と私が間違って思っていたもの。
g0 = np.array([[0, 1, 1],
               [p_b, 0, 0],
               [1-p_b, 0, 0]])
## 私が思うもの。
g0_1 = np.array([[0, 0, 0],
                 [p_b, 1, 0],
                 [1-p_b, 0, 1]])

## 整数乱数表現をベクトル表現に直す。
def int_vectorize(radix, i):
    r = np.array(np.zeros(radix))
    r[i] = 1
    return r

def calc_prob(mat, car):
    r = np.zeros(3)
    for i in range(3):
        r += np.dot(mat, int_vectorize(3, i)) * int_vectorize(3, i) \
            * car[i]
    return np.sum(r)

if __name__ == "__main__":
    ## アリスが選択を変えなかったときの確率
    #print((1/3) * np.sum(np.dot(f0, [1/3, 1/3, 1/3])))
    print(calc_prob(f0, [1/3, 1/3, 1/3]))
    ## ボブのものを選択したときの確率
    ## 確率計算は calc_prob を使わないとダメなようだ。
    #print((1/3) * np.sum(np.dot(g0, [1/3, 1/3, 1/3])))
    print(calc_prob(g0, [1/3, 1/3, 1/3]))
    #print((1/3) * np.sum(np.dot(g0_1, [1/3, 1/3, 1/3])))
    print(calc_prob(g0_1, [1/3, 1/3, 1/3]))

## 答えは次のように表示される。
##
## 0.3333333333333333
## 0.0
## 0.6666666666666666
