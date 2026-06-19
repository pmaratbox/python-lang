import markdown

src = "[text](http://x.com)"
html = markdown.markdown(src)
print(html.rstrip("\n"))
