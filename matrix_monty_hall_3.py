# -*- coding: utf-8 -*-
__version__ = '0.0.2' # Time-stamp: <2023-02-14T09:19:16Z>
## Language: Japanese/UTF-8

import random
import numpy as np


## アリスが0番目を指定という前提に立たない場合。

## アリスが 0番目を指定したときの行列を f0、ボブの行列を g0 とする。
f0 = np.array([[1, 1, 1],
               [0, 0, 0],
               [0, 0, 0]])
## ボブのランダムに選ぶときの確率を p_b とする。
p_b = random.random()
## 私が思うもの。
g0 = np.array([[0, 0, 0],
               [p_b, 1, 0],
               [1-p_b, 0, 1]])

## アリスが 1,2番目を指定したときの行列を f1,f2、ボブの行列を g1,g2 とする。
f1 = np.array([[0, 0, 0],
               [1, 1, 1],
               [0, 0, 0]])
g1 = np.array([[1, 1-p_b, 0],
               [0, 0, 0],
               [0, p_b, 1]])
f2 = np.array([[0, 0, 0],
               [0, 0, 0],
               [1, 1, 1]])
g2 = np.array([[1, 0, p_b],
               [0, 1, 1-p_b],
               [0, 0, 0]])

## アリスの選択を f、ボブの選択を g とする。
tmp0 = random.random()
tmp1 = random.random()
tmp2 = random.random()
tmp = tmp0 + tmp1 + tmp2
p0 = tmp0 / tmp
p1 = tmp1 / tmp
p2 = tmp2 / tmp
f = p0 * f0 + p1 * f1 + p2 * f2
g = np.hstack([g0, g1, g2])


## 整数乱数表現をベクトル表現に直す。
def int_vectorize(radix, i):
    r = np.array(np.zeros(radix))
    r[i] = 1
    return r

## ベクトルのテンソル積
def tensor_product(x, y):
    return np.hstack([x[i] * y for i in range(x.shape[0])])


## f についての確率の計算
def calc_prob(mat, car):
    r = np.zeros(3)
    for i in range(3):
        r += np.dot(mat, int_vectorize(3, i)) * np.array(int_vectorize(3, i)) \
            * car[i]
    return r


## g についての確率の計算
def calc_prob2(g, f, car):
    r = np.zeros(3)
    for i in range(3):
        a = np.dot(f, int_vectorize(3, i))
        for j in range(3):
            r += np.dot(g, tensor_product(int_vectorize(3, j),
                                          int_vectorize(3, i))) \
                * np.array(int_vectorize(3, i)) \
                * a[j] * car[i]
    return np.sum(r)


## calc_prob2 は次の形まで変形できそうだ。これが「図式」的なのだろうか？
##
# def calc_prob2(g, f, car):
#     r = np.zeros(3)
#     a = np.dot(f, car)
#     for i in range(3):
#         r += np.dot(g, tensor_product(a,
#                                       int_vectorize(3, i))) \
#             * np.array(int_vectorize(3, i)) \
#             * car[i]
#     return np.sum(r)


if __name__ == "__main__":
    ## アリスが選択を変えなかったときの確率
    print(np.sum(calc_prob(f, [1/3, 1/3, 1/3])))
    ## ボブのものを選択したときの確率
    print(calc_prob2(g, f, [1/3, 1/3, 1/3]))
    print(g)

## 答えは次のように表示される。
##
## 0.3333333333333333
## 0.6666666666666666
## [[0.         0.         0.         1.         0.72982054 0.
##   1.         0.         0.27017946]
##  [0.27017946 1.         0.         0.         0.         0.
##   0.         1.         0.72982054]
##  [0.72982054 0.         1.         0.         0.27017946 1.
##   0.         0.         0.        ]]
##
# #このように g を行列で表現できている！
