file = open("./FF_data.txt")  # 'file' object

# 1 ===

while True:  # bool, True
    year = input("please enter a 4-digit year: ")  # str, 1990
    if year.isdigit() and len(year) == 4:  # bool, True

        # 2 ===

        a = 0.0  # int, 0.0

        c = 0  # int, 0.0

        for list in file:  # str, "19260701    0.09   -0.22   -0.30   0.009\n"
            list = list.rstrip()  # str, "19260701    0.09   -0.22   -0.30   0.009"
            list = list.split()  # str, ["19260701",    "0.09",   "-0.22",   "-0.30",   "0.009"]
            data = list[0]  # str, "19260701"
            mktrf = float(list[1])  # float, 0.09
            j = data[0:4]  # str, "1926"
            sum_year = int(data[0])  # str, 1926

            if j == year:  # bool, True
                a = a + mktrf  # float, 0.0 + .....
                b = round(a, 2)  # float, -12.77
                c = c + sum_year  # int, 253

        # 3 ======

        mysum = float(b)  # float, 35.9
        mycount = (c)  # int, 7
        avr = mysum / mycount  # float, 5.128571428571428
        avr_round = round(avr, 2)

        # 4 ======

        print(f'count {c}, sum {b}, avg {avr_round}')
        break
    else:
        print("sorry, that was bad input")
