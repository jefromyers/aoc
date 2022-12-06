def find_unique(buf, window_size=4):
    current = 0
    while current + window_size < len(buf):
        window = buf[current : current + window_size]
        if len(set(window)) == len(window):
            return current + window_size
        current += 1

    return None


if __name__ == "__main__":
    fn = "example.txt"
    fn = "live.txt"

    stream = "".join([line for line in open(fn, "rt").readlines()])
    unique = find_unique(stream, window_size=14)
    print(f"{ unique = }")
