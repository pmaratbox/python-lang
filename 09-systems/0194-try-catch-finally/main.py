def main():
    try:
        raise ValueError("boom")
    except ValueError:
        print("caught")
    finally:
        print("cleanup")


if __name__ == "__main__":
    main()
