class Algorithm:
    def step(self):
        raise NotImplementedError

    def run(self):
        return " ".join(["start", self.step(), "end"])


class WorkAlgorithm(Algorithm):
    def step(self):
        return "work"


def main():
    print(WorkAlgorithm().run())


if __name__ == "__main__":
    main()
