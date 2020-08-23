from primos import es_primo, primo

def dcm(n1, n2, n3=None):
    if n3 != None:
        n1div = []
        n2div = []
        n3div = []
        for i in range(n1+1):
            try:
                if n1 % i == 0:
                    n1div.append(i)
                else:
                    continue
            except ZeroDivisionError:
                continue
        
        for i in range(n2+1):
            try:
                if n2 % i == 0:
                    n2div.append(i)
                else:
                   continue
            except ZeroDivisionError: #este codigo es un asco
                   continue
        for i in range(n3+1):
            try:
                if n3 % i == 0:
                    n3div.append(i)
                else:
                    continue
            except ZeroDivisionError:
                continue
        
        for i in reversed(n1div):
            if i in n2div and i in n3div:
                return i
                break
    else:
        
        n1div = []
        n2div = []
        for i in range(n1+1):
            try:
                if n1 % i == 0:
                    n1div.append(i)
                else:
                    continue
            except ZeroDivisionError:
                continue
        
        for i in range(n2+1):
            try:
                if n2 % i == 0:
                    n2div.append(i)
                else:
                        continue
            except ZeroDivisionError:
                        continue
        
        for i in reversed(n1div):
            if i in n2div:
                return i
                break

def mcm(n1, n2, n3=None):
    if n3 != None:
        n1div = []
        n2div = []
        n3div = []
        for i in range(1, 1000030):
            n1div.append(i * n1)
            n2div.append(i * n2)
            n3div.append(i * n3)
        for i in n1div:
            if i in n2div and i in n3div:
                return i
    else:
        n1div = []
        n2div = []
        for i in range(1, 100030):
            n1div.append(i * n1)
            n2div.append(i * n2)
        for i in n1div:
            if i in n2div:
                return i
            