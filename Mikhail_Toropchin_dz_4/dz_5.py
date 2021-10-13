import utils
import sys


def main(argv):
    val = argv[1]
    result = utils.currency_rates(val)
    print(f'Курс {val}: {result[0]}\n'
          f'Время: {result[1]}')
    return 0


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
