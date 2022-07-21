from math import sin, exp, pi
import os
from newton_cotes import (
    run_closed_newton_cotes_methods,
    run_opened_newton_cotes_methods,
)
from colors import Colors


def main():
    try:
        a = float(
            input(f"{Colors.BOLD}Digite o início do intervalo: {Colors.END_FORMAT}")
        )
        b = pi
        run_closed_newton_cotes_methods(
            a, b, lambda x: 10 - 0.2 * sin(8 * x) * exp(-(x ** (2.5)))
        )
        run_opened_newton_cotes_methods(
            a, b, lambda x: 10 - 0.2 * sin(8 * x) * exp(-(x ** (2.5)))
        )
    except ValueError:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{Colors.RED}Entrada inválida!{Colors.END_FORMAT}")
        main()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
