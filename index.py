def find_unique_numbers(input_numbers):
    """
    Функция принимает список целых чисел
    и возвращает отсортированный список уникальных чисел.
    """
    unique_numbers = []

    for number in input_numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    # Сортировка списка уникальных чисел
    unique_numbers.sort()
    return unique_numbers

try:
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    result = find_unique_numbers(numbers)
    print("Уникальные числа в порядке возрастания:")
    print(result)
except ValueError:
    print("Ошибка: введите только целые числа.")
