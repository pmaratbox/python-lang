import markdown

src = "- a\n- b"
html = markdown.markdown(src)
print(html.rstrip("\n"))
