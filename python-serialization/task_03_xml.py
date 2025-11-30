#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        elem = ET.SubElement(root, key)
        elem.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML back into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for elem in root:
        result[elem.tag] = elem.text  # STRING olaraq saxlanılır!

    return result

