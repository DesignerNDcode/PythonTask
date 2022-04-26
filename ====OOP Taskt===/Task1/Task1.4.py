class coputation:
    def __init__(self):
        nos = []
        self.nos = nos
        while True:
            ask = input("Want to add no? yes/no")

            if ask == "yes":
                num = int(input("enter number"))
                nos.append(num)
                print(nos, "\n")
            else:
                print("number Choosed", nos,
                      "\n", "==========First number will be taken ", "\n", " where 1 value will be needed=========",
                      "\n")
                break

    def sum(self):
        print("sum of", self.nos, "is", sum(self.nos), '\n')

    def factorial(self):
        factorial = 1
        if self.nos[0] < 0:
            print(" ! ! ! ! ! Factorial value cannot be intended for negative integers ! ! ! ! ! ")
        # The default factorial value for zero is one and this is printed here
        elif self.nos[0] == 0:
            print(" ! ! ! ! 1 is the factorial value 0 ! ! ! ! ")
        else:
            # For loop to handle the factorial calculation
            for i in range(1, self.nos[0] + 1):
                factorial = factorial * i
            print("The factorial value for the ", self.nos[0], "is", factorial, '\n')

    def testprime(self):
        for n in range(2, int(self.nos[0] ** 0.5) + 1):
            if self.nos[0] % n == 0:
                print(self.nos[0], "is not prime Number")

            else:
                print(self.nos[0], "is prime number", n)

    def testprimes(self):
        for h in range(len(self.nos)):
            for n in range(2, int(self.nos[h] ** 0.5) + 1):
                if self.nos[h] % n == 0:
                    print(self.nos[h], "is not prime Number")

                else:
                    print(self.nos[h], "is prime number", n, "\n")

    def tableMult(self):
        for i in range(1, 11):
            res = self.nos[0], 'x', i, '=', self.nos[0] * i
            print(res)
        print("============= First value")

    def alltableMult(self):
        for h in range(len(self.nos)):
            for i in range(1, 11):
                res = self.nos[h], 'x', i, '=', self.nos[h] * i
                print(res)
            print("============= all")

    def divisors(self):
        ldiv = []
        self.div = ldiv
        for i in range(1, self.nos[0] // 2 + 1):
            if self.nos[0] % i == 0:
                ldiv.append(i)

        print(self.nos[0], "Divisors =", ldiv, "\n",
              "==================")

    def listDivPrim(self):
        for h in range(len(self.div)):
            for n in range(2, int(self.div[h] ** 0.5) + 1):
                if self.div[h] % n == 0:
                    print(self.div[h], "is not prime Number")

                else:
                    print(self.div[h], "is prime number", n)


math = coputation

math.__init__(math)
math.sum(math)

math.factorial(math)

math.testprime(math)

math.testprimes(math)

math.divisors(math)

math.tableMult(math)

math.alltableMult(math)

math.listDivPrim(math)

