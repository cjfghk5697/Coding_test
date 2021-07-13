from bisect import bisect_left, bisect_right 


def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index

n,m=list(map(int,input().split(' ')))
array=list(map(int,input().split()))

print(count_by_range(array,m,m))
