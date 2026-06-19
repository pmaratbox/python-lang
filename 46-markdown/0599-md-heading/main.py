import markdown

src = "# Hello"
html = markdown.markdown(src)
print(html.rstrip("\n"))
