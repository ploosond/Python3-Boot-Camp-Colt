def solution(A):
    # write your code in Python 3.6
    return (no for num in A if no < num and no not in  A)