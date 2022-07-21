from math import sin, exp, pi
import os
from gauss_legendre import run_gauss_legendre
from colors import Colors


def main():
    try:
        a = float(
            input(f"{Colors.BOLD}Digite o início do intervalo: {Colors.END_FORMAT}")
        )
        b = pi
        num_p = float(
            input(f"{Colors.BOLD}Digite o número de pontos: {Colors.END_FORMAT}")
        )
        run_gauss_legendre(
            a, b, num_p, lambda x: 10 - 0.2 * sin(8 * x) * exp(-(x ** (2.5)))
        )
    except ValueError:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{Colors.RED}Entrada inválida!{Colors.END_FORMAT}")
        main()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
