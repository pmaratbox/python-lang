from bs4 import BeautifulSoup

DOC = """<html><body>
<h1>Hello</h1>
<span id="status">active</span>
<ul class="items">
<li class="item">apple</li>
<li class="item">banana</li>
<li class="item">cherry</li>
</ul>
<a href="https://example.com">site</a>
<div class="content"><p>first</p><p>second</p></div>
</body></html>"""

soup = BeautifulSoup(DOC, "html.parser")

# Descendant selector ".content p": every <p> nested anywhere inside .content.
paragraphs = soup.select(".content p")
print(",".join(p.get_text() for p in paragraphs))
