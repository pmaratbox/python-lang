import markdown

html = markdown.markdown("**bold**")
print(html.rstrip("\n"))
