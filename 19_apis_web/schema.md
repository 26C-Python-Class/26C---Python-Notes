# Module: XML Schema (XSD) – The Digital Blueprint

This guide explains how to move from "flexible" XML to "reliable" XML using **XSD (XML Schema Definition)**. It provides a structured curriculum for teaching validation, data types, and Python implementation.

---

## 1. Introduction: Why do we need a Blueprint?
In the previous lesson, we learned that XML is incredibly flexible—you can name a tag anything you want (`<pizza>`, `<user>`, `<id>`). 

However, in professional environments like **Banking APIs** or **Healthcare Systems**, flexibility is a bug, not a feature.
* **The Problem:** If a customer sends `<age>Twenty</age>` (Text) but your database expects an **Integer**, your program will crash.
* **The Solution:** **XSD (XML Schema Definition)**. It acts as a legal contract. If the XML doesn't follow the XSD "blueprint," the system rejects it immediately.



---

## 2. Core Concepts & Terminology

### A. Simple Types vs. Complex Types
This is the most important distinction in XSD. Think of your XML as a tree:

| Type | Description | Analogy |
| :--- | :--- | :--- |
| **Simple Type** | Contains **only text**. No attributes, no child tags. | A **Leaf** on a tree. |
| **Complex Type** | Contains **child elements** or **attributes**. | A **Branch** on a tree. |

### B. Data Types (Enforcing Reality)
XSD turns XML from "just strings" into a typed database:
* `xs:string`: "Standard Text"
* `xs:integer`: Whole numbers only (1, 50, -10)
* `xs:decimal`: Numbers with points (19.99)
* `xs:date`: Specific format (`YYYY-MM-DD`)

### C. Indicators (Control Logic)
You can control the **Order** and **Quantity** of data:
* `<xs:sequence>`: Elements must appear in the **exact order** listed.
* `minOccurs="0"`: This field is **Optional**.
* `maxOccurs="unbounded"`: This field is a **List** (can repeat forever).

---

## 3. Power Feature: Facets (Restrictions)
XSD allows you to set "Rules" for your data. This is an industry standard for data cleaning. For example, if a `zipcode` must be exactly 5 digits, you define a **Restriction**:

```xml
<xs:element name="zipcode">
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9]{5}"/> 
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

---

## 4. Demonstration: The Structured Library
Here is how an XSD Blueprint and a valid XML file look side-by-side.

### The Blueprint (`inventory.xsd`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="inventory">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="book" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title" type="xs:string"/>
              <xs:element name="pages" type="xs:integer"/>
              <xs:element name="price">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="xs:decimal">
                      <xs:attribute name="currency" type="xs:string" use="required"/>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

---

## 5. Python Implementation: Validation
While Python's built-in `xml` library is great for reading, it doesn't support XSD validation. In the professional world, we use **`lxml`**.



### The Validation Script
```python
# Installation: pip install lxml
from lxml import etree

def check_validity(xml_file, xsd_file):
    try:
        # 1. Load the Blueprint (XSD)
        schema_root = etree.parse(xsd_file)
        schema = etree.XMLSchema(schema_root)

        # 2. Load the Data (XML)
        xml_doc = etree.parse(xml_file)

        # 3. Validate
        if schema.validate(xml_doc):
            print("✅ Success: XML matches the Blueprint.")
        else:
            print("❌ Error: Invalid XML Structure.")
            # Print specific line numbers where the error occurred
            for log in schema.error_log:
                print(f"   Line {log.line}: {log.message}")

    except Exception as e:
        print(f"System Error: {e}")

# Example Usage
# check_validity("my_data.xml", "blueprint.xsd")
```

---

## 6. Summary: Benefits of XSD
| Benefit | Why it matters |
| :--- | :--- |
| **Auto-Validation** | You don't have to write 50 `if/else` statements to check data types. |
| **Data Integrity** | Guarantees that "garbage" data never enters your database. |
| **Documentation** | The XSD tells other developers exactly what your API expects. |
| **Standardization** | It is used globally in Finance, Shipping, and Aviation. |
