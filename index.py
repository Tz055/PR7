def main():
    # Ввод данных
    numbers = input("Введите числа через пробел: ").split()
    
    # Преобразование в int, удаление повторов и сортировка
    unique_sorted_numbers = sorted(set(map(int, numbers)))
    
    # Вывод результата
    print("Уникальные числа в порядке возрастания:")
    print(*unique_sorted_numbers)


if __name__ == "__main__":
    main()
