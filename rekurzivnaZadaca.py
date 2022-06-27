def rekurzija(a):
    if len(a) == 1:
        return a
    else:
        return rekurzija(a[1::]+a[0])
