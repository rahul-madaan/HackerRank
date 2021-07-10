def maximumToys(prices, k):
    prices = sorted(prices)
    print(prices)
    gifts = 0
    for price in prices:
        if k <=0:
            break;
        else:
            k = k- price
            gifts +=1
    print(gifts-1)


maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)