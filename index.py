# Рефакторинг:
# Переменная numbers переименована в input_numbers
# Логика обработки ввода вынесена в функцию parse_input()

def parse_input():
    
    # Запрашивает ввод у пользователя и
    # преобразует его в список целых чисел.
    user_input = input("Введите числа через пробел: ")

    # Исправление: добавлена обработка пустого ввода,
    # чтобы избежать работы с пустым списком
    if not user_input.strip():
        print("Ввод пуст. Завершение программы.")
        return []

    try:
        return [int(value) for value in user_input.split()]
    except ValueError:
        print("Ошибка: введите только целые числа.")
        return []


def find_unique_numbers(input_numbers):
    
    # Возвращает отсортированный список уникальных чисел.
    unique_numbers = []

    for number in input_numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    unique_numbers.sort()
    return unique_numbers


def main():
    input_numbers = parse_input()
    if input_numbers:
        result = find_unique_numbers(input_numbers)
        print("Уникальные числа в порядке возрастания:")
        print(result)


if __name__ == "__main__":
    main()
