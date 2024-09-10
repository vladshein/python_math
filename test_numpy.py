import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=int)
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(b)

#Розмір
print(f"{a.shape} {b.shape}")

#Щоб створити вектор або матрицю, які складаються з одиниць, використовують метод ones
a = np.ones((5,), dtype=float)
print(a)

m = np.ones((2, 3), dtype=int)
print(m)

#Щоб створити вектор або матрицю, які складаються з нулів, використовують метод zeros
a = np.zeros(5, dtype=float)
print(a)

m = np.zeros((2, 3), dtype=int)
print(m)

#Для створення одиничної матриці використовують метод identity
m = np.identity(4, dtype=int)
print(m)

#Для створення масиву, що містить послідовність чисел, існують два методи: np.arange та np.linspace
#Метод np.arange аналогічний методу Python range
a = np.arange(5)
b = np.arange(1, 3, 0.5)
print(a)
print(b)

#Щоб включити останній елемент визначеної послідовності, можна використовувати метод np.linspace
a = np.linspace(1, 5, num=5)
b = np.linspace(1, 3, num=3)
print(a)
print(b)

#Є можливість створювати масиви та матриці наповнені випадковими значеннями
a = np.random.random(3)
b = np.random.random((3, 3))
print(a)
print(b)

#index
a = np.array([1, 2, 3, 4, 5])
print(a[0])
print(a[1:])
print(a[:2])


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1, 1])
print(a[1:, 1])
print(a[0, :2])

#arithmetic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Для арифметичних операцій необхідно, щоб матриці були одного й того самого розміру. 
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(a + b)
print(a - b)
print(a * b)
print(a / b)



a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 2, 3])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# min — мінімальне значення
# max — максимальне значення
# sum — сума всіх елементів
# mean — середнє арифметичне
# prod — перемножити всі елементи
a = np.array([1, 2, 3, 4, 5])
print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(a.prod())

#Матриця
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(a.prod())

#У Numpy є ще один спосіб створення матриць - це побудова об'єкта типу matrix за допомогою однойменного методу.
a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

#Щоб побудувати із матриці a діагональну матрицю b можна використати метод diag.
a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag = np.diag(a)
print(diag)

b = np.diag(diag)
print(b)

#Для створення одиничної матриці ми вже використали метод identity, але є альтернативний варіант, метод eye
#який при цьому дозволяє задати зміщення діагоналі з одиничними значеннями. Зміщення задаємо через ключ значення k
a = np.eye(4, k=-1, dtype=float)
print(a)


