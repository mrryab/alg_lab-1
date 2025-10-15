import time
import tracemalloc


def insertion_sort(arr):
    """Сортировка вставками"""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    try:
        # Читаем из файла
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            n = int(lines[0].strip())
            arr = list(map(int, lines[1].strip().split()))

        # Проверяем соответствие количества элементов
        if len(arr) != n:
            print(f"Предупреждение: Заявлено {n} элементов, но введено {len(arr)}")

        # Начинаем замеры производительности
        start_time = time.time()
        tracemalloc.start()

        # Выполняем сортировку
        sorted_arr = insertion_sort(arr.copy())  # Используем copy чтобы не менять исходный массив

        # Завершаем замеры
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Выводим результаты
        #print("Отсортированный массив:", " ".join(map(str, sorted_arr)))
        print(f'Время выполнения: {end_time - start_time:.6f} секунд')
        print(f'Пиковое использование памяти: {peak_memory / 1024:.2f} KB')

        # Записываем результат в файл
        with open("output.txt", "w") as f:
            f.write(" ".join(map(str, sorted_arr)))

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
