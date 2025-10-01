import time
import tracemalloc

def main():
    # Записываем массив чисел
    arr_input = input("Введите массив чисел через пробел: ")
    with open('input.txt', 'w') as f1:
        f1.write(arr_input)

    # Читаем массив из файла
    with open('input.txt', 'r') as f1:
        a = list(map(int, f1.readline().split()))

    # Записываем искомое значение
    v_input = input("Введите искомое значение: ")
    with open('input.txt', 'w') as f:
        f.write(v_input)

    # Читаем искомое значение из файла
    with open('input.txt', 'r') as f:
        v = int(f.readline())

    # Начинаем отслеживание памяти и времени
    tracemalloc.start()
    start_time = time.time()

    # Линейный поиск
    indices = []
    for i in range(len(a)):
        if a[i] == v:
            indices.append(i)

    # Завершаем отслеживание
    end_time = time.time()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Формирование и вывод результата
    if not indices:
        print(-1)
        with open("output.txt", "w") as f1:
            f1.write('-1')
    else:
        print(f"Найдено элементов: {len(indices)}")
        print(f"Индексы: {','.join(map(str, indices))}")
        with open("output.txt", "w") as f1:
            f1.write(" ".join(map(str, indices)))

    print(f'Время выполнения: {end_time - start_time:.6f} секунд')
    print(f'Пиковое использование памяти: {peak_memory / 1024:.2f} KB')


if __name__ == "__main__":
    main()