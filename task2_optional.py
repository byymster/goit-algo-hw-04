def merge_k_lists(lists):
    if not lists:
        return []

    # Рекурсивно об'єднуємо всі списки
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists) - 1, 2):
            # Зливаємо по два списки
            merged_lists.append(merge(lists[i], lists[i + 1]))
        if len(lists) % 2 == 1:
            # Додаємо останній список, якщо кількість списків непарна
            merged_lists.append(lists[-1])
        lists = merged_lists

    return lists[0]

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Об'єднуємо менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки з лівої чи правої частини
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
