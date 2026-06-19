import markdown

src = "1. a\n2. b"
html = markdown.markdown(src)
print(html.rstrip("\n"))
