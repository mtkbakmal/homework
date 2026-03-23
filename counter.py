def counter():
    n = 0
    def incounter():
        nonlocal n
        n += 1
        print(n)
    return incounter
fn = counter()
fn()
fn()
fn()