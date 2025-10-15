import time
import tracemalloc


def main():
    # Читаем данные из файла
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    # Если файл пустой или нет данных
    if not lines:
        with open("output.txt", "w") as f:
            f.write('-1')
        return

    # Первая строка - массив чисел
    a = list(map(int, lines[0].split()))

    # Вторая строка - искомое значение V
    v = int(lines[1])

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

    # Формирование и вывод результата согласно условию
    with open("output.txt", "w") as f:
        if not indices:
            # Если значение не найдено
            f.write('-1')
        else:
            # Если найдено - выводим количество и индексы через запятую
            result = f"{len(indices)}\n"
            result += ",".join(map(str, indices))
            f.write(result)

    # Вывод статистики
    print(f'Время выполнения: {end_time - start_time:.6f} секунд')
    print(f'Пиковое использование памяти: {peak_memory / 1024:.2f} KB')


if __name__ == "__main__":
    main()
