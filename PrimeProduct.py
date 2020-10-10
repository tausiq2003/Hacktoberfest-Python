
def isPrime(a) :
    for i in range(2,a) :
        if a%i == 0 :
            return False
    return True

def primeProduct(b) :
    factorsl=[]
    primeFact=[]
    for i in range(1,b+1) :
        if b%i == 0 :
            factorsl=factorsl+[i]

    for j in factorsl :
        if isPrime(j) :
            primeFact=primeFact+[j]

    for k in range(1,len(primeFact)-1) :
        for l in range(k,len(primeFact)) :
            if primeFact[k]*primeFact[l] == b :
                return True
    return False


print(primeProduct(1147))
