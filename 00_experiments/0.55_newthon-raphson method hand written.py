import pandas as pd


def f(x):
    return x ** 6 / 6 - 3 * x ** 4 - 2 * x ** 3 / 3 + 27 * x ** 2 / 2 + 18 * x - 30


def d_f(x):
    return x ** 5 - 12 * x ** 3 - 2 * x ** 2 + 27 * x + 18  # Complete this line with the derivative you have calculated.


if __name__ == '__main__':
    # x = -4.0
    # x = 1.99
    x = 3.1


    d = {"x": [x], "f(x)": [f(x)]}
    for i in range(0, 20):
        x = x - f(x) / d_f(x)
        d["x"].append(x)
        d["f(x)"].append(f(x))

    df = pd.DataFrame(d, columns=['x', 'f(x)'])
    # Convert the whole dataframe as a string and display
    # print(df.shape)
    print(df.to_markdown())
