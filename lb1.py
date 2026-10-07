
INITIAL_DATA = [10, 20, 30, 40, 50, 60, 70, 80]


def show(label, lst, expected_len=None):
    """Друкує стан списку; якщо задано expected_len — звіряє довжину."""
    line = f"{label}: {lst}  | len={len(lst)}"
    if expected_len is not None:
        status = "OK" if len(lst) == expected_len else "ПОМИЛКА"
        line += f" (очікувано {expected_len}) -> {status}"
    print(line)


def main():
    data = list(INITIAL_DATA)  
    expected = len(data)

    print("=== Крок 1. Початковий список ===")
    show("data", data, expected)
    print(f"id(data) = {id(data)}  (запам'ятовуємо ідентичність об'єкта)")
    original_id = id(data)

    print("\n=== Крок 2. Доступ за індексом ===")
    print(f"data[0]  (перший, додатний індекс)    = {data[0]}")
    print(f"data[3]  (додатний індекс)            = {data[3]}")
    print(f"data[-1] (останній, від'ємний індекс) = {data[-1]}")
    print(f"data[-3] (третій з кінця)             = {data[-3]}")

    print("\n=== Крок 3. Зрізи (кожен створює НОВИЙ список) ===")
    slices = [
        ("data[2:5]    — від 2 до 5 (не включно), крок 1", data[2:5]),
        ("data[:4]     — від початку до 4",                data[:4]),
        ("data[-3:]    — останні три елементи",            data[-3:]),
        ("data[::2]    — увесь список, крок 2",            data[::2]),
        ("data[1:-1:3] — від 1 до передостаннього, крок 3", data[1:-1:3]),
        ("data[::-1]   — у зворотному порядку (крок -1)",  data[::-1]),
    ]
    for label, result in slices:
        print(f"{label:<50} -> {result}")
    show("data після зрізів (не змінився)", data, expected)

    print("\n=== Крок 4. Зміни «на місці» (з діагностикою довжини) ===")

    data.append(90)
    expected += 1
    show("4.1 append(90)", data, expected)

    data.insert(2, 25)
    expected += 1
    show("4.2 insert(2, 25)", data, expected)

    data.remove(60)  
    expected -= 1
    show("4.3 remove(60)", data, expected)

    removed = data.pop(0)  
    expected -= 1
    print(f"    (pop(0) повернув {removed})")
    show("4.4 pop(0)", data, expected)

    data[1:3] = [111, 222, 333]  
    expected += 1
    show("4.5 data[1:3] = [111, 222, 333]", data, expected)

    del data[-2:]  
    expected -= 2
    show("4.6 del data[-2:]", data, expected)

    print("\n=== Крок 5. Нові об'єкти чи той самий? ===")
    print(f"id(data) після всіх мутацій = {id(data)}; "
          f"той самий об'єкт: {id(data) == original_id}")

    copy_by_slice = data[:]
    print(f"data[:] -> новий об'єкт: {id(copy_by_slice) != id(data)}")

    concat = data + [999]
    print(f"data + [999] -> новий об'єкт: {id(concat) != id(data)}; "
          f"data не змінився: {999 not in data}")

    data += [999]  #
    expected += 1
    print(f"data += [999] -> той самий об'єкт: {id(data) == original_id}")
    show("5.x після data += [999]", data, expected)

    print("\n=== Крок 6. Фінальний стан ===")
    show("data", data, expected)
    print(f"Початкова константа не змінилась: {INITIAL_DATA}")


if __name__ == "__main__":
    main()