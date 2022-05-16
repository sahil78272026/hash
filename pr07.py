if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple(integer_list)  # converting tuple to lis
    print(hash(t)) # hash of a tuple
