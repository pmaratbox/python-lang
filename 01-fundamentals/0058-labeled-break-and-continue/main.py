def scan():
    for i in range(1, 4):
        for j in range(1, 4):
            if j > i:
                break
            if i * j == 4:
                print(f"stop at {i},{j}")
                return
            print(f"{i},{j}")


scan()
