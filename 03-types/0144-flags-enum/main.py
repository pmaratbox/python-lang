from enum import IntFlag


class Perm(IntFlag):
    READ = 1
    WRITE = 2


flags = Perm.READ | Perm.WRITE
print(f"{int(flags)} {'yes' if flags & Perm.WRITE else 'no'}")
