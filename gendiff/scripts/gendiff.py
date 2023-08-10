import argparse
from ..gendiff_func import generate_diff
from ..formaters.stylish import stylishing
from ..formaters.plain import plain


def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )

    # Добавление позиционных аргументов
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        choices=['stylish', 'plain']
        )
    # Парсинг аргументов командной строки
    args = parser.parse_args()
    # Выбираем форматер в зависимости от указанного формата
    format_name = plain if args.format == 'plain' else stylishing
    # Вызываем функцию generate_diff для получения различий между файлами
    diff = generate_diff(args.first_file, args.second_file, format_name)
    # Ваш код для обработки аргументов
    print(diff)


if __name__ == '__main__':
    main()
