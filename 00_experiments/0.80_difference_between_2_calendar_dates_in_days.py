from datetime import datetime

if __name__ == '__main__':
    # from1 = "2000-03-02"
    # to1 = "2000-03-06"
    # income1 = 10
    #
    # dt_from1 = datetime.strptime(from1, "%Y-%m-%d")
    # dt_to1 = datetime.strptime(to1, "%Y-%m-%d")
    #
    # from2 = "2000-03-05"
    # to2 = "2001-03-06"
    # income2 = 12
    # dt_from2 = datetime.strptime(from2, "%Y-%m-%d")
    # dt_to2 = datetime.strptime(to2, "%Y-%m-%d")

    from1 = "2000-03-02"
    to1 = "2099-03-02"
    dt_from1 = datetime.strptime(from1, "%Y-%m-%d")
    dt_to1 = datetime.strptime(to1, "%Y-%m-%d")

    delta = dt_to1 - dt_from1
    print(f'Difference is {delta.days} days')
