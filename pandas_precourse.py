#pre-course pandas

#Pandas (Panel data) - це широко поширена бібліотека мовою Python з відкритим
#вихідним кодом для обробки і аналізу даних.

#Головний об'єкт pandas DataFrame може містити неоднорідні типи даних
#Бібліотека pandas надає дві структури для роботи з даними: Series і DataFrame

#Series - це маркована одновимірна структура даних, її можна уявити, як таблицю з одним рядком (або стовпцем).
#DataFrame - це двовимірна маркована структура. Вона схожа на звичайну таблицю і 
#це виявляється у способі її створення та у роботі з її елементами.

import pandas as pd
mountain_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])
print(mountain_height)


#add name
mountains_height = pd.Series( 
data=[2061, 2035.8, 2028.5, 2022.5, 2016.4], 
index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"], name="Height, m", 
dtype=float,
)

print(mountains_height)

print(mountains_height[0]) # 2061.0
print(mountains_height["Goverla"]) # 2061.0

#use python type slice
mountains_height = pd.Series( 
data=[2061, 2035.8, 2028.5, 2022.5, 2016.4], 
index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"], 
name="Height, m", 
dtype=float,
)
print(mountains_height[1:3])
print(mountains_height["Brebenskyl":"Petros"])


#Операції порівняння та фільтрації об'єкта Series за допомогою логічних операцій створюють новий об'єкт Series
print(mountains_height > 2030)
print(mountains_height[mountains_height > 2030])

# Goverla True
# Brebenskyl True
# Pip_Ivan False
# Petros False
# Gutin_Tomnatik False
# Name: Height, m, dtype: bool
# Goverla 2061.0
# Brebenskyl 2035.8
# Name: Height, m, dtype: float64

#Операції перевірки на існування елемента в Series використовують індекс, а не значення:
print("Goverla" in mountains_height) # True

#Сортування виконується за індексом або за значеннями, дивлячись, що необхідно для конкретного випадку. 
#Використовуються методи Series.sort_index та Series.sort_values відповідно.
sort_index = mountains_height.sort_index()
print(sort_index)


#Елементи NaN (не число) в об'єкті Series можна замінити на задане значення, використовуючи метод fillna:
import pandas as pd

mountains_height = pd.Series( 
{"Goverla": 2061, "Brebenskyl": 2035.8, "Pip_Ivan": 2028.5}, 
index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"], name="Height, m", 
dtype=float,
)

print(mountains_height)
mountains_height.fillna(0, inplace=True)
print(mountains_height)

#DateFrame
#Як ми вже говорили об'єкт DataFrame - ця двовимірна таблиця даних.
contacts = pd.DataFrame(
  {
    "name": [
      "Allen Raymond",
      "Chaim Lewis",
      "Kennedy Lane",
      "Wylie Pope",
      "Cyrus Jackson",
    ],
    "email": [
      "nulla.ante@vestibul.co.uk",
      "dui.in@egetlacus.ca",
      "mattis.Cras@nonenimMauris.net",
      "est@utquamvel.net",
      "nibh@semsempererat.com",
    ],
    "phone": [
      "(992) 914-3792",
      "(294) 840-6685",
      "(542) 451-7038",
      "(692) 802-2949",
      "(501) 472-5218",
    ],
    "favorite": [False, False, True, False, True],
  },
  index=[1, 2, 3, 4, 5],
)

print(contacts)


#Вибір рядка за міткою:
print(contacts.loc[1])

#Вибір рядка за індексом:
print(contacts.iloc[1])

#Зріз за рядками:
print(contacts[0:2])

#Вибір рядків, які відповідають умові:
print(contacts[contacts["favorite"]])


#Читання та запис об'єктів Series та DataFrameS
#Робота з даними у форматі CSV

#Для читання текстових файлів з даними у форматі CSV в об'єкті DataFrame існує метод read_csv.
#Можливі аргументи

# filepath_or_buffer — шлях до зчитуваного файлу. Є обов'язковим параметром. Шлях може вказувати 
#   як локальний файл, так і URL для завантажування даних з мережі;
# sep — роздільник стовпців. За замовчуванням кома ,, але можна використовувати значення:
# /s+ для стовпців, розділених пробільними символами,
# \t для роздільників-табуляцій
# None, щоб бібліотека pandas сама спробувала логічно визначити символ-роздільник.
# delimiter — псевдонім для аргументу sep;
# header  — номери рядків (індекси), які використовуються для імен стовпців. 
#   За замовчуванням header=0, що говорить про використання першого рядка для імен стовпців. 
#   Іноді у файлі немає заголовка, тоді потрібно присвоїти значення header=None і визначити імена стовпців в аргументі names;
# names — послідовність неповторюваних імен стовпців, які використовуватимуться під час читання файлу;
# nrows — кількість рядків, які зчитуються з файлу. Буває необхідно під час читання декількох рядків 
#   з дуже великого файлу для тестування або дослідження даних, що містяться в ньому;
# comment — визначає символ, наприклад #, який при виявленні на початку рядка повідомляє про те, 
#   що весь рядок необхідно пропустити;
# skip_blank_lines — за замовчуванням встановлено значення True – пропуск порожніх рядків у вхідному файлі. 
#   При встановленні значення False порожні рядки інтерпретуються як рядки із значень NaN;
# delim_whitespace — можна встановити для цього аргумента значення True, замість визначення
#    аргумента sep='\s+', щоб встановити, що стовпці даних розділяються символами пробілів.

users = pd.read_csv("users.csv")
print(users)

#Щоб записати дані у файл CSV — необхідно використовувати метод об'єкта DataFrame to_csv
contacts.to_csv("data.csv", index=False)

#Робота з файлами Microsoft Excel
#Бібліотека pandas має можливість зчитувати вміст файлів Excel з розширеннями .xls та .xlsx
#в об'єкт DataFrame за допомогою методу pd.read_excel

persons = pd.read_excel("persons.xlsx")
print(persons)

#Щоб зберегти вміст об'єкта DataFrame у файл Excel на одному листі необхідно скористатися методом to_excel:
contacts = pd.DataFrame(
  {
    "name": [
      "Allen Raymond",
      "Chaim Lewis",
      "Kennedy Lane",
      "Wylie Pope",
      "Cyrus Jackson",
    ],
    "email": [
      "nulla.ante@vestibul.co.uk",
      "dui.in@egetlacus.ca",
      "mattis.Cras@nonenimMauris.net",
      "est@utquamvel.net",
      "nibh@semsempererat.com",
    ],
    "phone": [
      "(992) 914-3792",
      "(294) 840-6685",
      "(542) 451-7038",
      "(692) 802-2949",
      "(501) 472-5218",
    ],
    "favorite": [False, False, True, False, True],
  },
  index=[1, 2, 3, 4, 5],
)

contacts.to_excel('contacts.xlsx', sheet_name='Contacts')

#Робота з файлами JSON
#Для читання даних у форматі JSON використовується метод read_json
employees = pd.read_json("./json/split.json", orient="split")
print(employees)

# Але необхідно знати, що залежно від значення typ, ми можемо використовувати певні значення orient.
# Якщо typ='series', то orient може бути split, records або index.
# Якщо typ='frame', то orient розширює свої значення до списку: split, records, index, columns, values.

data = {
  "name": {"1": "Michael", "2": "John", "3": "Liza"},
  "country": {"1": "Canada", "2": "USA", "3": "Australia"}
}

employees = pd.DataFrame(data)
employees.to_json("employees.json", orient="split")

