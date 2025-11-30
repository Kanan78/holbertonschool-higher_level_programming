#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML back into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for element in root:
        text = element.text

        # Simple type conversion attempts
        if text is None:
            result[element.tag] = None
        elif text.isdigit():
            result[element.tag] = int(text)
        else:
            # Try float conversion
            try:
                result[element.tag] = float(text)
            except ValueError:
                result[element.tag] = text

    return result


if __name__ == "__main__":
    sample = {"name": "Alice", "age": 23, "height": 5.4}

    serialize_to_xml(sample, "sample.xml")
    print("Serialized to sample.xml")

    data = deserialize_from_xml("sample.xml")
    print("Deserialized:", data)
