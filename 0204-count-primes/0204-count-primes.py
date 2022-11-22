'''
    NB ---> see: Sieve of Eratosthenes method
    link: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            prime = [True] * n
            prime[0] = prime[1] = False
            i = 2
            while i*i < n:
                if prime[i] == True:  
                    for j in range(i*i, n, i):
                        prime[j] = False
                i+=1
            
            return sum(prime)