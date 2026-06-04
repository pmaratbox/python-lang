class NullLogger:
    def log(self, message):
        pass


class RealLogger:
    def __init__(self):
        self.count = 0

    def log(self, message):
        self.count += 1


def main():
    null_logger = NullLogger()
    real_logger = RealLogger()
    null_logger.log("ignored")
    real_logger.log("recorded")
    print(real_logger.count)


if __name__ == "__main__":
    main()
