def move(inst, stack):
    _a = inst.replace("move ", "").split(" from")
    amount = int(_a[0].strip())
    start, end = _a[1].split(" to ")
    start = int(start.strip()) - 1
    end = int(end.strip()) - 1

    print(f"{ inst = }")
    print(f"{ amount = }")
    print(f"{ start = }")
    print(f"{ end = }")

    # print(f"Start: {stack}")
    # for i in range(1, amount + 1):
    #     # print(f"Move: {i}")
    #     blk = stack[start].pop(0)
    #     print(f"{ blk = }")
    #     stack[end].insert(0, blk)

    blks = stack[start][0:amount]
    del stack[start][0:amount]
    print(f"Blks: {blks}")
    blks.reverse()
    for b in blks:
        stack[end].insert(0, b)

    # print(f"Return: {stack}")
    return stack


if __name__ == "__main__":
    fn = "example.txt"
    fn = "live.txt"

    inst = []
    raw_stacks = []
    for line in open(fn, "rt").readlines():
        if (l := line).startswith("move"):
            inst.append(l.strip())
        elif line.strip():
            raw_stacks.append(l)

    raw_stacks.reverse()
    map = {}
    stacks = []
    for line in raw_stacks:
        for i, c in enumerate(line):
            try:
                n = int(c)
                stacks.append([])
                map[n] = i
            except ValueError:
                pass
            if c == "\n":
                break

    raw_stacks.reverse()
    for line in raw_stacks:
        if "1" in line:
            continue
        for k, v in map.items():
            if line[v].strip() != "":
                stacks[k - 1].append(line[v].strip())

    for i in inst:
        stacks = move(i, stacks)

    message = "".join([s[0] for s in stacks])
    print(stacks)
    print(message)
