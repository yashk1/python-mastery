


def portfolio_cost(filename):
    total_sum = 0.0 

    with open(filename,'r') as file:

        for line in file:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_sum += nshares*price
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)

    print(total_sum)

portfolio_cost('../../Data/portfolio2.dat')#