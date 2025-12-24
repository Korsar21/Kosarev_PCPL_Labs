import sys
import math


def get_coefficient():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            if a == 0:
                raise ValueError
            b = float(sys.argv[2])
            c = float(sys.argv[3])
            return a, b, c
        except ValueError:
            print("Ошибка в аргументах командной строки!")
    return


def input_coefficient():
    while True:
        try:
            a, b, c = map(float, input("Введите коэффициенты a, b, c через пробел: ").split())
            if a == 0:
                print('Коэффициент "a" не может быть равен нулю.')
                continue
            return a, b, c
        except ValueError:
            print("неверный ввод, ведите коэффициенты a, b, c через пробел")


def calculate_discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def find_real_roots(a, b, c, d):
    if d < 0:
        return set()

    sqrt_discriminant = math.sqrt(d)
    y1 = (-b + sqrt_discriminant) / (2 * a)
    y2 = (-b - sqrt_discriminant) / (2 * a)


    real_roots = set()

    if y1 >= 0:
        x_root = math.sqrt(y1)
        real_roots.add(x_root)
        real_roots.add(-x_root)

    if y2 >= 0:
        x_root = math.sqrt(y2)
        real_roots.add(x_root)
        real_roots.add(-x_root)

    return real_roots


def main():
    if (coefficients := get_coefficient()) is not None:
        a, b, c = coefficients
    else:
        a, b, c = input_coefficient()

    discriminant = calculate_discriminant(a, b, c)
    roots = find_real_roots(a, b, c, discriminant)

    print(f'дискриминант: {discriminant}')
    if len(roots) == 0:
        print('действительных корней нет')
        return

    print("Корни:", *roots)


if __name__ == "__main__":
    main()
