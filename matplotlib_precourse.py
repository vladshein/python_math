#Пакет Matplotlib широко використовується у мові Python для графічного відображення даних.
#В основному він використовується через інтерфейс pyplot для створення простих візуалізацій даних

#Лінійні графіки
#Основним елементом зображення є фігура (Figure)
#Для побудови графіка використовується функція plot
import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20])
plt.show()


#Текст на графіках
#Використовується функція xlabel для осі x та ylabel для y осі. 
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')

#Назву графіка можна задати методом title
plt.title('Денна погода у м. Полтава', fontsize=15)

#За допомогою параметра loc можна задати вирівнювання заголовка center, left, right
#Щоб помістити текст на полі графіка, необхідно викликати метод text з Text
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")

#І додати легенду можна, викликавши метод legend, не забувши додати параметр label у метод plot. 
#І остаточний результат буде наступним.
date = pd.date_range(start='2021-09-01', freq='D', periods=8)
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
plt.title('Температура в м. Полтава', fontsize=15)
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
plt.legend()
plt.show()


#Компонування графіків
#Якщо ми хочемо розмістити два графіки, хорошим способом буде використовувати метод subplots. 

#subplots повертає два об'єкти, перший - це Figure, підкладка, на якій будуть розміщені поля з графіками,
#другий - об'єкт (або масив об'єктів) Axes, через який можна отримати повний доступ до налаштування 
#зовнішнього вигляду елементів, що відображаються

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots()
axs.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs.plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
plt.title('Температура в м. Полтава', fontsize=15)
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
plt.legend()
plt.show()

#Розділити графіки на частини, то у функцію subplots ми повинні передати кількість рядків та стовпців
date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(2, 1)

axs[0].plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs[1].plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')

axs[0].set_title('Денна', fontsize=10)
axs[1].set_title('Нічна', fontsize=10)

fig.suptitle('Температура в м. Полтава', fontsize=15)
plt.show()


#Налаштування графіків
#Стиль лінії графіка задається через параметр linestyle, який може приймати значення з таблиці
#option - solid, dashed, dashdot, dotted, None

#Колір лінії графіка задається через параметр color
date = pd.date_range(start="2021-09-01", freq="D", periods=8)
plt.plot(
  date,
  [23, 17, 17, 16, 15, 14, 17, 20],
  label="day temperature",
  linestyle="--",
  color="#FF5733",
)
plt.plot(
  date,
  [19, 11, 16, 11, 10, 10, 11, 16],
  label="night temperature",
  linestyle=":",
  color="#061358",
)
plt.xlabel("Дата", fontsize="small", color="midnightblue")
plt.ylabel("Температура", fontsize="small", color="midnightblue")
plt.title("Температура в м. Полтава", fontsize=15)
plt.legend()
plt.show()

#Щоб встановити для межі осі інше значення, використовуються методи xlim та ylim.
#Також можна відобразити сітку за допомогою методу grid
#Товщина лінії визначається значенням аргументу lineweight (або просто lw) в пунктах (pt).

#final
date = pd.date_range(start="2021-09-01", freq="D", periods=8)
plt.plot(
  date,
  [23, 17, 17, 16, 15, 14, 17, 20],
  label="day temperature",
  linestyle="--",
  color="#FF5733",
  linewidth=2,
  marker="D",
)
plt.plot(
  date,
  [19, 11, 16, 11, 10, 10, 11, 16],
  label="night temperature",
  linestyle=":",
  color="#061358",
  linewidth=2,
  marker="^",
)
plt.ylim(0, 25)
plt.xlabel("Дата", fontsize="small", color="midnightblue")
plt.ylabel("Температура", fontsize="small", color="midnightblue")
plt.title("Температура в м. Полтава", fontsize=15)
plt.legend()
plt.grid()
plt.show()

#Стовпчикові діаграми
#Для створення стовпчикової діаграми використовується метод bar (barh) модуля pyplot
# bar — вертикальна стовпчаста діаграма;
# barh — горизонтальна стовпчаста діаграма.
plt.bar(
  ["США", "Китай", "Японія", "Велика Британія"],
  [39, 38, 27, 22],
  color=["b", "r", "y", "g"],
)

plt.xlabel("Країна", fontsize="small", color="midnightblue")
plt.ylabel("Кількість", fontsize="small", color="midnightblue")
plt.title("Золоті медалі: Літня олімпіада Токіо 2020", fontsize=15)
plt.show()

#Кругові діаграми
#Кругову або секторну діаграму можна побудувати за допомогою методу pie
#import matplotlib.pyplot as plt

labels = [
  "Junior Software Engineer",
  "Senior Software Engineer",
  "Software Engineer",
  "System Architect",
  "Technical Lead",
]

data = [63, 31, 100, 2, 11]
explode = [0.15, 0, 0, 0, 0]
plt.pie(
  data,
  labels=labels,
  shadow=True,
  explode=explode,
  autopct="%.2f%%",
  pctdistance=1.15,
  labeldistance=1.35,
)

plt.show()


#Діаграми в полярних координатах
import numpy as np
theta = np.linspace(0, 2.0 * np.pi, 1000)

r = np.sin(6 * theta)
plt.polar(theta, r)
plt.show()

#Тривимірні графіки
#Для створення тривимірного графіка необхідно імпортувати об'єкт Axes3D з модуля mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#Лінійний графік
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

theta_max = 8 * np.pi
n = 1000
theta = np.linspace(0, theta_max, n)
x = theta
z = np.sin(theta)
y = np.cos(theta)
ax.plot(x, y, z, "g")

plt.show()

#Діаграма розсіювання
#Для побудови тривимірної діаграми розсіювання використовується функція scatter з Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

x = [5, 10, 15, 20]
z = [10, 0, 5, 15]
y = [0, 10, 5, 25]
s = [150, 130, 30, 160]
ax.scatter(x, y, z, s=s)

plt.show()

#Каркасна поверхня
#Для побудови каркасної поверхні використовується функція plot_wireframe з Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

grid = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_wireframe(x, y, z)
plt.show()

#Поверхня
#Для побудови поверхні використовується функція plot_surface
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

grid = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_surface(x, y, z)
plt.show()

