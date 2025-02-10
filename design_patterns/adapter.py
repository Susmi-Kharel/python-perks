"""
An adapter design pattern is a structural design pattern that allows different
and incompatible objects to work together

A good example of an adapter design pattern is using different parsers with
completely incompatible methods and calls.

The example below uses JsonAdapter and XmlAdapter to adapt the `parse` method.
"""

from typing import Any
from xml.etree import ElementTree
import json


class JsonParser:
    def load_json(self, data: str):
        return json.loads(data)


class XmlParser:
    def parse_xml(self, data: str):
        root = ElementTree.fromstring(data)
        # root = tree.getroot()
        return {child.tag: child.text for child in root}


# Adapter Interface
class ParserAdapter:
    parser: Any

    def parse(self, data: str):
        raise NotImplementedError


# Adapters for each parsers
class JSONAdapter(ParserAdapter):
    def __init__(self, json_parser):
        self.parser = json_parser

    def parse(self, data):
        return self.parser.load_json(data)


class XMLAdapter(ParserAdapter):
    def __init__(self, xml_parser):
        self.parser = xml_parser

    def parse(self, data):
        return self.parser.parse_xml(data)


if __name__ == "__main__":
    # defining an adapter  with different parser
    json_parser = JSONAdapter(JsonParser())
    xml_parser = XMLAdapter(XmlParser())

    json_parsed_dict = json_parser.parse('{"name": "John Doe", "age":20}')
    print(json_parsed_dict)  # {'name': 'John Doe', 'age': 20}

    xml_parsed_dict = xml_parser.parse("<xml><name>John Doe</name><age>20</age></xml>")
    print(xml_parsed_dict)  # {'name': 'John Doe', 'age': '20'}
