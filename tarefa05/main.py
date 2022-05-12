from math import sin
import os
from gauss_legendre import run_gauss_legendre
from colors import Colors


def main():
    try:
        a = float(
            input(f"{Colors.BOLD}Digite o início do intervalo: {Colors.END_FORMAT}"))
        b = float(
            input(f"{Colors.BOLD}Digite o fim do intervalo: {Colors.END_FORMAT}"))
        num_p = float(
            input(f"{Colors.BOLD}Digite o número de pontos: {Colors.END_FORMAT}"))
        run_gauss_legendre(a, b, num_p, lambda x: (sin(2 * x) + 4 * x ** 2 + 3 * x) ** 2)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.RED}Entrada inválida!{Colors.END_FORMAT}")
        main()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
