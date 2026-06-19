import markdown

src = "> quote"
html = markdown.markdown(src)
print(html.rstrip("\n"))
