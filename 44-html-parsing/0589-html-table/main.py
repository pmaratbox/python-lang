from bs4 import BeautifulSoup

DOC = "<table><tr><td>r1c1</td><td>r1c2</td></tr><tr><td>r2c1</td><td>r2c2</td></tr></table>"

soup = BeautifulSoup(DOC, "html.parser")

# Select every <td> cell with the CSS selector `td`, in document (row-major) order.
cells = soup.select("td")
print(",".join(td.get_text() for td in cells))
