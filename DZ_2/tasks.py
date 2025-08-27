import numpy as np
import matplotlib.pyplot as plt
'''
 Задачи на статистику

1. Для каждой из колонок посчитайте: mean, median, var, min, max .
2. Найдите max(quality) . Для всех записей (строчек таблицы) с этим quality вычислите средний pH
3. Проведите операцию "нормализации" для колонки quality :
Определите, чему равны min(quality) и max(quality) ;
Вычтите min(quality) из колонки quality ;
Поделите полученные значения на max(quality) - min(quality) . Таким образом, значения в колонке перейдут в диапазон [0; 1] .

Задачи на визуализацию

1. Постройте столбчатую диаграмму (plt.bar ) или круговую диаграмму (plt.pie ) для quality . Необходимо посчитать, сколько различных
уровней качества есть, после чего построить соответсвующую диаграмму распределения (функция np.unique с параметром return_counts в помощь).
 2. Постройте точечный график (plt.scatter ) для x = volatile acidity и y = alcohol .
Поделите исходный датасет на 2 таблицы (матрицы): с низким уровнем quality (т.е. min(quality) ) и высокими (т.е. max(quality) ).
Вызовите функцию plt.scatter 2 раза: с точками, у которых низкий уровень quality (окрасьте их зеленым цветом) и с точками, у которых он высокий (окрасьте их оранжевым цветом).
Есть ли какая-то зависимость между качеством вина и объемом спирта и летучей кислотой? Если есть, то какая?
'''

# alcohol,volatile acidity,sulphates,pH,quality
dataset = np.loadtxt(
             "wine_quality.csv",
                    delimiter=",",
                    skiprows=1, # пропускаем строчку с названиями колонок
             )


print('>>>Задачи на статистику<<< \n#1')
print(f'mean = {dataset.mean(axis=0)}\n'
      f'median = {np.median(dataset, axis=0)}\n'
      f'var = {dataset.var(ddof=1, axis=0)}\n'
      f'min = {dataset.min(axis=0)}\n'
      f'max = {dataset.max(axis=0)}\n')

print('#2')
#dataset[dataset[:,-1] == dataset[:,-1].max()][:,-2].mean()
max_q = dataset[:,-1].max()
records_with_max_q = dataset[dataset[:,-1] == max_q]
pH_mean = records_with_max_q[:,-2].mean()
print(pH_mean,'\n')

print('#3')
min_q = dataset[:,-1].min()
range_q = max_q - min_q
data = (dataset[:,-1] - min_q) / range_q
print(data)

#>>>Задачи на визуализацию<<<
#1
quality, count = np.unique(dataset[:,-1], return_counts=True)
plt.pie(x = count, autopct='%1.1f%%')
plt.title('Распределение уникальных уровней качества')
plt.show()

#2
q = dataset[:,-1]
low_q = dataset[q == min_q]
high_q = dataset[q == max_q]

plt.scatter(x = low_q[:,1], y = low_q[:, 0], color='tab:green', label="low quality")
plt.scatter(x = high_q[:,1], y = high_q[:, 0], color='tab:orange', label="high quality")
plt.legend()
plt.grid(True)
plt.xlabel('volatile acidity')
plt.ylabel('alcohol')
plt.title('Relationship between volatile acid and alcohol volume,\n depending on the quality')
plt.show()
