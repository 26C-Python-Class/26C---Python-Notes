# Module: Introduction to XML (eXtensible Markup Language)

This guide provides a structured breakdown of XML concepts, syntax rules, and programmatic handling using Python.

---

## 1. What is XML?
**XML** stands for **eXtensible Markup Language**. While it looks similar to HTML, they serve completely different purposes:
* **HTML** is for **displaying** data (focusing on how it looks: bold, headers, colors).
* **XML** is for **describing** data (focusing on what the data *is*: Price, ID, Name).

### Why use XML?
1.  **Platform Independent:** It is a plain-text format. A database on an old mainframe can send XML to a modern iPhone app, and both will understand the data.
2.  **Standardization:** It powers major formats like `.docx` (Word), `.xlsx` (Excel), and `SVG` (Vector Graphics).
3.  **Strict Structure:** Unlike HTML, which "guesses" if you forget a tag, XML crashes if the structure is wrong. This makes it highly reliable for banks and enterprise systems.

---

## 2. The Logical Structure: The "Tree"
XML documents are organized like a family tree. Every piece of data has a specific "address" within this hierarchy.



* **Root Element:** The single parent that contains all other elements.
* **Child Elements:** Nested inside the root or other children.
* **Attributes:** Metadata attached to a tag (e.g., `<product id="101">`).
* **Text (Leaves):** The actual information stored inside the tags.

---

## 3. Core Syntax Rules
For an XML file to be **"Well-Formed"** (valid), it must follow these rules strictly:

1.  **The Prolog:** The first line must define the XML version and encoding.
    `<?xml version="1.0" encoding="UTF-8"?>`
2.  **Case Sensitivity:** `<Data>` and `<data>` are viewed as two completely different tags.
3.  **Proper Nesting:** You must close the "inner" tag before the "outer" tag.
    * ✅ Correct: `<a><b>Text</b></a>`
    * ❌ Wrong: `<a><b>Text</a></b>`
4.  **Attribute Quotes:** All attribute values must be inside quotes.
    * ✅ Correct: `<user id="5">`
    * ❌ Wrong: `<user id=5>`

---

## 4. Special Characters and Entities
Because characters like `<` and `&` are used to define the XML structure, you cannot use them freely inside your text. You must use **Entity References**.

| Character | Entity Reference | Example |
| :--- | :--- | :--- |
| `<` | `&lt;` | `Age &lt; 21` |
| `>` | `&gt;` | `Score &gt; 90` |
| `&` | `&amp;` | `Salt &amp; Pepper` |
| `"` | `&quot;` | `&quot;Hello&quot;` |

---

## 5. Demonstration: Cataloging a Music Library
The following XML document demonstrates **Namespaces**, **Attributes**, and **Nested Elements**.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<music_library xmlns:rock="http://genres.com/rock">
    
    <album id="A99" genre="Classic Rock">
        <title>The Dark Side of the Moon</title>
        <artist>Pink Floyd</artist>
        <release_year>1973</release_year>
        
        <description>Masterpiece &amp; Progressive Rock Icon</description>
        
        <tracks>
            <track number="1">Speak to Me</track>
            <track number="2">Breathe</track>
        </tracks>
        
        <rock:subgenre>Progressive</rock:subgenre>
    </album>

</music_library>
```

---

## 6. Python Implementation: Navigating the Tree
Python uses the `xml.etree.ElementTree` library to "parse" (read) and interact with XML data.



```python
import xml.etree.ElementTree as ET

# Sample XML Data
raw_xml = """
<inventory>
    <item category="electronics">
        <name>Laptop</name>
        <price currency="USD">899.99</price>
        <specs>High Performance &amp; Lightweight</specs>
    </item>
    <item category="furniture">
        <name>Desk</name>
        <price currency="EUR">150.00</price>
        <specs>Oak wood</specs>
    </item>
</inventory>
"""

try:
    # 1. Parse the string into a tree object
    tree_root = ET.fromstring(raw_xml)
    print(f"Reading XML with Root: {tree_root.tag}\n")

    # 2. Iterate through 'item' elements
    for item in tree_root.findall('item'):
        # Get data from Attributes
        category = item.get('category')
        
        # Get data from Nested Child Tags
        name = item.find('name').text
        price_val = item.find('price').text
        currency = item.find('price').get('currency')
        specs = item.find('specs').text

        print(f"Product: {name} ({category.upper()})")
        print(f"Price:   {price_val} {currency}")
        print(f"Details: {specs}")
        print("-" * 30)

except ET.ParseError as error:
    print(f"Fatal Error: The XML is not well-formed! {error}")
```

### Explanation of Methods:
* **`ET.fromstring()`**: Turns a raw string into a Python object you can loop through.
* **`.findall('tag')`**: Searches for **all** direct children that match the tag name.
* **`.find('tag')`**: Grabs only the **first** match it finds (useful for unique items like 'name').
* **`.text`**: Extracts the actual value sitting between the `<tag>` and `</tag>`.
* **`.get('attr')`**: Reaches inside the tag to grab the value of an attribute.

