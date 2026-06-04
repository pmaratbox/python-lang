def run(program):
    cell = 0
    for c in program:
        if c == "+":
            cell += 1
        elif c == "-":
            cell -= 1
    return cell


print(run("+++"))
