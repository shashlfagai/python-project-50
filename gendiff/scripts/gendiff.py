import argparse
from ..gendiff_func import generate_diff, stylish
# Устанавливаем форматер по умолчанию
generate_diff.default_formatter = stylish


def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )

    # Добавление позиционных аргументов
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    # Парсинг аргументов командной строки
    args = parser.parse_args()

    # Вызываем функцию generate_diff для получения различий между файлами
    diff = generate_diff(args.first_file, args.second_file)
    # Ваш код для обработки аргументов
    print(diff)


if __name__ == '__main__':
    main()
