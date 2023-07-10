import argparse


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    # Добавление позиционных аргументов
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Парсинг аргументов командной строки
    args = parser.parse_args()

    # Ваш код для обработки аргументов
    
    # Ваш код для обработки аргументов
    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")

if __name__ == '__main__':
    main()
