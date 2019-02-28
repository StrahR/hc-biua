def similar(a: set, b: set) -> int:
    s0 = len(a.difference(b))
    s1 = len(b.difference(a))
    s2 = len(a.intersection(b))
    return min(s0, s1, s2)