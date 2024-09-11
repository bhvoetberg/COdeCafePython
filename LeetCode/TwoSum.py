def twosum1_brute_force(array_of_integers: list[int], target: int) -> list[int]:
    for i in range(len(array_of_integers)):
        for j in range(i + 1, len(array_of_integers)):
            if array_of_integers[i] + array_of_integers[j] == target:
                return [i ,j]
    return []


def twosum1_one_pass_hash(array_of_integers: list[int], target: int) -> list[int]:
    # Step 1: Again, create a dictionary to store numbers and their indices.
    numMap = {}
    # Step 2: During iteration over the numbers, the complement is calculated for each number.
    for i, num in enumerate(array_of_integers):
        complement = target - num
        # Step 3: It checks if the complement exists in the dictionary. If so, the indices are returned.
        if complement in numMap:
            return [numMap[complement], i]
        # Step 4: Otherwise, the current number and its index are added to the dictionary.
        numMap[num] = i
    # Step 5: If no pair sums up to the target, return an empty list.
    return []


def main():
    array_of_integers = [2, 7, 8, 9, 10, 11, 12, 13]
    target = 22
    print(twosum1_brute_force(array_of_integers, target))
    print(twosum1_one_pass_hash(array_of_integers, target))



if __name__ == '__main__':
    main()