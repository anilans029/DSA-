
# the time complexity for finding power of a number using DAC is O(logn)
# T(n) = T(n/2) + c


def DAC_PowerOfNumber(a,n):
    if n <= 1:
        if n ==0:
            return 1
        elif n ==1:
            return a
    else:
        #divide
        m = n//2

        #concquer
        b = DAC_PowerOfNumber(a,m)

        #combine
        c = b*b
        if n % 2 == 0:
            return c
        else :
            return c*a

n = 100
a = 2
result = DAC_PowerOfNumber(a,n)
print(result)