from colors import Colors
import os
from methods import *

def main():
    try:
        num_p = float(input(f"{Colors.BOLD}Digite o número de pontos: {Colors.END_FORMAT}"))
        print("Para função: f(x) = e**(-x**2) * 1 / (x**2 + x + 1)")
        run_gauss_hermite(num_p, lambda x: 1/(x**2 + x + 1))
        print("Para função: f(x) = e**(-x) * 1 / x")
        run_gauss_laguerre(num_p, lambda x: 1 / x)
        print("Para função: f(x) = (1/(1 - x**2)**0.5) * x**2")
        run_gauss_chebyshev(num_p, lambda x: (1/(1 - x**2)**0.5) * x**2)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.RED}Entrada inválida!{Colors.END_FORMAT}")
        main()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()

