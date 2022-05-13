import sympy as sp


if __name__ == '__main__':
    w0, w1 = sp.symbols('w0, w1')
    L = (-w1 + w0 -1)**2 + w0**2 + (w1 + w0 + 1)**2

    # calculate partial derivatives using SymPy package
    dL_dw0 = sp.diff(L, w0)
    dL_dw1 = sp.diff(L, w1)

    # translate partial derivatives (dL_dw0, dL_dw1) that ary merely SymPy expressions into Python functions (lambdify)
    dL_dw0_fobj = sp.utilities.lambdify((w0, w1), dL_dw0)
    dL_dw1_fobj = sp.utilities.lambdify((w0, w1), dL_dw1)

    h = 0.1


    print(dL_dw0)
    print(dL_dw1)



