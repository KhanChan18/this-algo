def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

if __name__ == "__main__":
    data = [2,4,5,7,8,9,12,14,19,22,25,27,28,33,37]
    for i in range(len(data)):
        print(binary_search(data, 12, i, len(data)))
