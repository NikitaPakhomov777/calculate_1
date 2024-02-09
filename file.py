def main(data):
    while True:
        if 'stop' in data:
            print('\nПрограмма завершена')
            break
        if len(data) != 3:
            raise Exception('throws Exception')

        num_1, symbol, num_2 = data[0], data[1], data[2]

        if '.' in num_1 or '.' in num_2 or symbol not in ['+', '-', '/', '*']:
            raise Exception('throws Exception')
        elif int(data[0]) not in range(1, 11) or int(data[2]) not in range(1, 11) or symbol not in ['+', '-', '/', '*']:
            raise Exception('throws Exception')

        new_dict = {'+': int(data[0]) + int(data[2]),
                    '-': int(data[0]) - int(data[2]),
                    '/': int(data[0]) // int(data[2]),
                    '*': int(data[0]) * int(data[2]), }

        print(f'Результат: {new_dict[symbol]}\n')

        data = input('Введите операцию: ').split()


new_str = input('Введите операцию: ').split()

main(new_str)