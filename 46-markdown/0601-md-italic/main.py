import markdown

html = markdown.markdown("*italic*")
print(html.rstrip("\n"))
