def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return low

def sort_sequence(sequence):
    # Преобразование введенной последовательности в список
    numbers = sequence.split()
    numbers = [int(num) for num in numbers]

    # Сортировка списка по возрастанию элементов
    numbers.sort()

    return numbers

while True:
    # Ввод последовательности чисел
    sequence = input("Введите последовательность чисел через пробел: ")
    # Проверка соответствия условию ввода данных
    if not sequence.replace(" ", "").isdigit():
        print("Ошибка ввода. Введите только числа, разделенные пробелами.")
        continue

    # Ввод числа для сравнения
    target = int(input("Введите число для сравнения: "))

    # Получение отсортированной последовательности
    sorted_sequence = sort_sequence(sequence)

    # Проверка на соответствие введенного числа и последовательности
    if target > sorted_sequence[-1]:
        print("Введенное число больше всех чисел в последовательности. Повторите ввод.")
        continue

    # Поиск позиции элемента с использованием двоичного поиска
    position = binary_search(sorted_sequence, target)

    # Проверка на соответствие найденной позиции
    if position == len(sorted_sequence):
        print("Число больше всех элементов в последовательности.")
    elif position == 0 and sorted_sequence[position] > target:
        print("Число меньше всех элементов в последовательности.")
    else:
        print("Позиция числа в отсортированной последовательности:", position)

    # Проверка, желает ли пользователь повторить ввод
    choice = input("Желаете повторить ввод чисел? (Да/Нет): ")
    if choice.lower() != "да":
        break