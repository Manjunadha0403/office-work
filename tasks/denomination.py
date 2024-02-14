money = int(input("enter amount:"))
def denominations(money):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]#Denominations Value
    result = {}
    for denom in denominations:
        result[str(denom)] = money // denom
        money %= denom
    return result
# Example usage with your input
result_dict  = denominations(money)
print(result_dict)
# Print the result
for key, value in result_dict.items():#Key Words are use
    print(f'courency {key}/- = {value} = value {int(key) * value}/-')