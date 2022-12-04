from dataclasses import dataclass


@dataclass
class Section:
    start: int
    end: int

    def range(self):
        return set(list(range(self.start, self.end + 1)))

    @classmethod
    def from_line(cls, line):
        r = line.split("-")
        return cls(start=int(r[0]), end=int(r[1]))


if __name__ == "__main__":
    print("woop")
    fn = "example.txt"
    fn = "live.txt"

    t = 0
    for line in open(fn, "rt").readlines():
        f, s = line.strip().split(",")
        first = Section.from_line(f)
        second = Section.from_line(s)
        print(f"{ first }")
        print(f"{ second }")
        print(f"{first.range() & second.range()}")

        if first.range() & second.range():
            t += 1
            print("Overlap")

        print(" ")
    print(f"Total: {t}")
