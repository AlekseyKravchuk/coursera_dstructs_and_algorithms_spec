
import sympy as sp

if __name__ == '__main__':
    x = sp.symbols('x', real=True)
    f = abs(x)

    df_dx = sp.diff(f, x)
    df_dx = sp.utilities.lambdify(x, df_dx)

    print(f'df_dx(-5) = {df_dx(-5)}')

