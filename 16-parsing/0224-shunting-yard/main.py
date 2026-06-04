def to_postfix(expr):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    ops = []
    for tok in expr.split():
        if tok in prec:
            while ops and prec.get(ops[-1], 0) >= prec[tok]:
                output.append(ops.pop())
            ops.append(tok)
        else:
            output.append(tok)
    while ops:
        output.append(ops.pop())
    return output


print(" ".join(to_postfix("3 + 4 * 2")))
