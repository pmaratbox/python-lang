import xml.etree.ElementTree as ET

DOC = """<catalog>
  <book id="b1" lang="en"><title>Go</title><price>30</price></book>
  <book id="b2" lang="fr"><title>Rust</title><price>45</price></book>
</catalog>"""

root = ET.fromstring(DOC)
print(len(root.findall("book")))
