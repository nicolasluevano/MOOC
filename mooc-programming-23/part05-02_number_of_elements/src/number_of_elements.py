# Write your solution here
def count_matching_elements(m, n):
    count = 0
    for i in m:
        for a in i:
            if a == n:
                count += 1
    return count


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))