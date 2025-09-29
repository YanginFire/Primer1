# from sympy import *

# 1 способ
# k, T, C, L = symbols('k C T L') # Что это означает? (данная строка означает, что переменные k, T, C, L являются символами) оценка 5

C_ost = 100000
# Am_lst = [ ] 
# C_ost_lst = [ ] # Сосед увеличил интевал между скобками (выполнено форматирование кода) у переменных Am и C_ost_lst

# for i in range(5):
#   Am = (C - L) / T
#   C_ost -= Am.subs({C: 100000, 
#                     T: 5, 
#                     L: 0
#                    }) # Сосед разбил переменные по строкам внутри фигурных скобок
#   Am_lst.append(round(Am.subs({C: 100000, 
#                                T: 5, 
#                                L: 0}), 
#                                2)) # Сосед разбил переменные по строкам внутри фигурных скобок 2.0
#   C_ost_lst.append(round(C_ost, 2))

# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# 2 Способ
# Aj = 0
C_ost = 100000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(5):
#   Am = k * 1 / T * (C - Aj)
#   C_ost -= Am.subs({C: 100000, k: 2, T: 5})
#   Am_lst_2.append(round(Am.subs({C: 100000, k: 2, T: 5}), 2))
#   Aj += Am # Что это означает? (данная строка означает, что переменная Aj увеличивается на значение переменной Am) оценка 5
#   C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# Контейнер табличного вывода
# import pandas as pd

# Y = range(1,6)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

# print(tfame) #Что это означает? (данная строка означает вывод данных в виде таблицы))
# print(tfame2)

# Контейнер визуализации

# from matplotlib import pyplot as plt

# Line chart
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt .plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
# plt.show()

# Pie chart # Что это означает? - данная строка означает комментарий к коду ниже, визуализирующий результат вывода данных в виде круговой диаграммы оценка 5
# vals = Am_lst_2
# labels = list(range(1,6))
# explode = [0.1, 0.1, 0.1, 0.1, 0.1]
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, rotatelabels=True, wedgeprops={'edgecolor': 'k', 'lw':1, 'ls':'--'})
# ax.axis('equal')
# plt.show()

# Bar chart
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])

# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.show()

# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.show()









# Вариант 1 

# from sympy import *
# # 1 способ
# k, T, C, L = symbols('k C T L')

# C_ost = 1000000
# Am_lst = []
# C_ost_lst = []

# for i in range(16):
#   Am = (C - L) / T
#   C_ost -= Am.subs({C: 1000000, T: 15, L: 0})
#   Am_lst.append(round(Am.subs({C: 1000000, T: 15, L: 0}), 2))
#   C_ost_lst.append(round(C_ost, 2))

# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# # 2 Способ
# Aj = 0
# C_ost = 1000000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(16):
#   Am = k * 1 / T * (C - Aj)
#   C_ost -= Am.subs({C: 1000000, k: 2, T: 15})
#   Am_lst_2.append(round(Am.subs({C: 1000000, k: 2, T: 15}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# # Контейнер табличного вывода
# import pandas as pd

# Y = range(1,16)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

# print(tfame)
# print(tfame2)

# # Контейнер визуализации

# from matplotlib import pyplot as plt

# # Line chart
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt .plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
# # plt.show()

# # Pie chart
# vals = Am_lst_2
# labels = list(range(1,17))
# explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, rotatelabels=True, wedgeprops={'edgecolor': 'k', 'lw':1, 'ls':'--'})
# ax.axis('equal')
# # plt.show()

# # Bar chart
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])

# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.show()

# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.show()

# import os
# print(os.getenv('My_secret'))


# print(os.getenv('MONGO_API'))
# print(os.getenv('FIREBASE_API'))
# print(os.getenv('REACT_API'))