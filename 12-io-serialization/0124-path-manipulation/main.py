import posixpath

joined = posixpath.join("/tmp", "file.txt")
base = posixpath.basename(joined)
ext = posixpath.splitext(joined)[1]
print(joined, base, ext)
