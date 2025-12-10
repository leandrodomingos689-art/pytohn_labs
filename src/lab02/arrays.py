def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Вернуть кортеж (минимум, максимум). Если список пуст — ValueError.
    """
    if len(nums) == 0:
        raise ValueError("Список не может быть пустым")

    min_val = nums[0]
    max_val = nums[0]

    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return (min_val, max_val)


###############################################################
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Вернуть отсортированный список уникальных значений (по возрастанию).
    """
    if len(nums) == 0:
        return []

    # Создаем список для уникальных значений
    unique_list = []

    # Проходим по всем числам и добавляем только те, которых еще нет в unique_list
    for num in nums:
        found = False
        for unique_num in unique_list:
            if num == unique_num:
                found = True
                break

        if not found:
            unique_list.append(num)

    n = len(unique_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique_list[j] > unique_list[j + 1]:
                # Меняем местами
                temp = unique_list[j]
                unique_list[j] = unique_list[j + 1]
                unique_list[j + 1] = temp

    return unique_list


###############################################################
def flatten(mat: list[list | tuple]) -> list:
    """
    «Расплющить» список списков/кортежей в один список по строкам (row-major).
    Если встретилась строка/элемент, который не является списком/кортежем — TypeError.
    """
    result = []

    for row in mat:
        # Проверяем, является ли элемент списком или кортежем
        if not isinstance(row, (list, tuple)):
            raise TypeError("Все элементы должны быть списками или кортежами")

        # Добавляем все элементы из текущего списка/кортежа в результат
        for item in row:
            result.append(item)

    return result


###############################################################
print(min_max([3, -1, 5, 5, 0]))
print(unique_sorted([3, 1, 2, 1, 3]))
# print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], "ab"]))
