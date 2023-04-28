total_price = int(input())
price_list = [int(input()) for _ in range(9)]
print(total_price-sum(price_list))