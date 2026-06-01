class Resource:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, *args):
        print("close")


with Resource():
    print("use")
