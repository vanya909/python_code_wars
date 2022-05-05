# These don't work
#def palindrome(n, c): return (c*n)[:int(n/2+n%2)]+(c*n)[int(n/2)-1::-1]
#def palindrome(n,c):return c+c[0]*(n-len(c)*2)+c[::-1][n%2:]

# Working version
palindrome=lambda n,c:c+c[-1]*(n-len(c)*2+1)+c[-2::-1]
#-----------------------------------------------------|
# 55 characters