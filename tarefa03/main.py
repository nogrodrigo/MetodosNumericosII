from math import sin
import os
from newton_cotes import run_closed_newton_cotes_methods, run_opened_newton_cotes_methods
from colors import Colors


def main():
    try:
        a = float(
            input(f"{Colors.BOLD}Digite o início do intervalo: {Colors.END_FORMAT}"))
        b = float(
            input(f"{Colors.BOLD}Digite o fim do intervalo: {Colors.END_FORMAT}"))
        run_closed_newton_cotes_methods(a, b, lambda x: (sin(2 * x) + 4 * x ** 2 + 3 * x) ** 2)
        run_opened_newton_cotes_methods(a, b, lambda x: (sin(2 * x) + 4 * x ** 2 + 3 * x) ** 2)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.RED}Entrada inválida!{Colors.END_FORMAT}")
        main()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
