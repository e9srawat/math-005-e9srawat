"""Day005"""
def gcd(a, b):
    """GCD of a, b"""
    mx = max(a, b)
    mn = min(a, b)
    while mn:
        temp = mx
        mx = mn
        mn = temp%mn
    return mx
def solver(p, q):
    """lcm from range p-q"""
    if p > q:
        start = q
        end = p + 1
    else:
        start = p
        end = q + 1
    lcm = 1
    for i in range(start, end):
        lcm = lcm * i // gcd(lcm, i)
    return lcm
