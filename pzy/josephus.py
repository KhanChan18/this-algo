def josephus_A(n, k, m):
    people = list(range(1, n+1))
    i = k - 1

    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n

        if num < n - 1:
            print(", ", end="")
        else:
            print("")
    return

def josephus_L(n, k, m):
    people = list(range(1, n+1))

    i = k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(
            people.pop(i),
            end=(", " if num > 1 else "\n")
        )
    return

if __name__ == "__main__":
    josephus_A(1375, 1, 14367)
