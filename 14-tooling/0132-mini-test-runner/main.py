def test_add():
    assert 1 + 1 == 2


def test_mul():
    assert 2 * 3 == 6


def test_concat():
    assert "ab" + "c" == "abc"


def main():
    tests = [test_add, test_mul, test_concat]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError:
            failed += 1
    print("{} passed, {} failed".format(passed, failed))


if __name__ == "__main__":
    main()
