import markdown

html = markdown.markdown("`code`")
print(html.rstrip("\n"))
