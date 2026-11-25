from collections import deque

def normalize_data(articles):
    filtered = filter(lambda a: a.get('content'), articles)

    def clean_article(article):
        title = article['title'].strip()
        tags = set(map(str.lower, article['tags']))
        return {
            'clean_title': title,
            'unique_tags': sorted(tags)
        }

    cleaned = map(clean_article, filtered)

    return sorted(cleaned, key=lambda a: len(a['unique_tags']), reverse=True)


def task1():
    articles = [
        {'title': ' Functional Python 101 ', 'content': '...', 'tags': ['python', 'functional', 'PYTHON']},
        {'title': 'Async in Python', 'content': '...', 'tags': ['python', 'async']},
        {'title': 'Decorators Explained', 'content': '', 'tags': ['python', 'decorators']},
        {'title': '  Data Science Basics', 'content': '...', 'tags': ['data', 'pandas', 'numpy', 'data']},
    ]
    print("\nЗавдання 1: Конвеєр нормалізації даних")
    result = normalize_data(articles)
    for item in result:
        print(item)


def sliding_window(iterable, n):
    window = deque(maxlen=n)
    for item in iterable:
        window.append(item)
        if len(window) == n:
            yield tuple(window)


def task2():
    print("\nЗавдання 2: Генератор ковзного вікна")
    data = [1, 2, 3, 4, 5, 6]
    print("Дані:", data)
    try:
        n = int(input("Введіть розмір вікна n: "))
        if n <= 0:
            print("n має бути більше 0!")
            return
    except ValueError:
        print("Потрібно ввести ціле число!")
        return
    windows = sliding_window(data, n)
    print("Результат:", list(windows))

def main():
    while True:
        print("\nГОЛОВНЕ МЕНЮ")
        print("1 - Завдання 1 (нормалізація даних)")
        print("2 - Завдання 2 (ковзне вікно)")
        print("0 - Вихід")
        choice = input("Ваш вибір: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '0':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == '__main__':
    main()