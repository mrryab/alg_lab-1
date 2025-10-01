import time
import tracemalloc


def selection_sort(arr):
    """Сортировка выбором"""
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def main():
    try:
        # Получаем входные данные
        print("Введите количество элементов:")
        n_input = input()

        print("Введите элементы массива через пробел:")
        arr_input = input()

        # Записываем в файл (можно записать оба значения)
        with open('input.txt', 'w') as f:
            f.write(f"{n_input}\n{arr_input}")

        # Читаем из файла
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            n = int(lines[0].strip())
            arr = list(map(int, lines[1].split()))

        # Проверяем соответствие количества элементов
        if len(arr) != n:
            print(f"Предупреждение: Заявлено {n} элементов, но введено {len(arr)}")

        # Начинаем замеры производительности
        start_time = time.time()
        tracemalloc.start()

        # Выполняем сортировку
        sorted_arr = selection_sort(arr.copy())  # Используем copy чтобы не менять исходный массив

        # Завершаем замеры
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Выводим результаты
        print("Отсортированный массив:", sorted_arr)
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