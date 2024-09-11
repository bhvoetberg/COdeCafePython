# Sliding window

def best_day(stock_values) -> int:
    left: int = 0
    right: int = 1
    maximum: int = 0

    while right < len(stock_values):
        if stock_values[right] > stock_values[left]:
            maximum = max(maximum, stock_values[right] - stock_values[left])
        else:
            left = right
        right = right + 1
    return maximum


def main():
    stock_values = [7, 1, 5, 0, 3, 6, 4]

    print(best_day(stock_values))


if __name__ == '__main__':
    main()
