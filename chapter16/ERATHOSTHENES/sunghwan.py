class Sieve:
    def __init__(self, MAX_N, bits_per_i):
        if bits_per_i & (bits_per_i - 1) != 0:
            raise ValueError("Bits per i should be binary number")

        self._MAX_N = MAX_N
        self.__bits_per_i = bits_per_i
        self.__sieve = [(1 << (bits_per_i))-1] * (MAX_N // bits_per_i + 1)

        self.__set_composite(0)
        self.__set_composite(1)
        sqrt_n = int(MAX_N ** (1/2))

        for i in range(2, sqrt_n+1):
            if self.is_prime(i):
                for j in range(i*i, MAX_N+1, i):
                    self.__set_composite(j)

    def is_prime(self, n):
        if n > self._MAX_N:
            raise ValueError(f"N should be smaller or equals to {self._MAX_N}")

        ret = self.__sieve[n // self.__bits_per_i] \
                & (1 << (n & (self.__bits_per_i - 1)))

        return ret != 0

    def __set_composite(self, n):
        self.__sieve[n // self.__bits_per_i] &= ~(1 << (n & (self.__bits_per_i - 1)))


if __name__ == '__main__':
    s = Sieve(100, 16)
    for n in range(1, 100+1):
        print(n, s.is_prime(n))
