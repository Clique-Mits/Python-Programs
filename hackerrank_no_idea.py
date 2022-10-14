def count_happiness(n_list, a_set, b_set):
    result = 0
    for item in n_list:
        if item in a_set:
            result += 1
        if item in b_set:
            result -= 1

    print(result)


if __name__ == "__main__":
    n, m = map(int, input().split())
    n_integers_list = list(map(int, input().split()))
    a_integers_set = set(map(int, input().split()))
    b_integers_set = set(map(int, input().split()))

    count_happiness(n_integers_list, a_integers_set, b_integers_set)