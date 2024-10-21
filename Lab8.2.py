import numpy as np
import random
import math

M = int(input("Введіть перший розмір масиву:"))
N = int(input("Введіть другий розмір масиву:"))

masiv1=np.zeros((M,N))
for i in range(M):
    for j in range (N):
        masiv1[i][j]=random.randint(1,50)
print("Mасив1:\n", masiv1)

masiv2=np.zeros((M,N))
for i in range(M):
    for j in range (N):
        masiv2[i][j]=random.randint(1,50)
print("Mасив2:\n",masiv2)

dob = masiv1 * masiv2
print("Добуток масивів:\n",dob)

sum = masiv1 + masiv2
print("Сума масивів:\n",sum)

diff = masiv1 - masiv2
print("Різниця масивів:\n", diff)