__author__ = 'g8y3e'

import xml.etree.ElementTree as etree

class XMLWrapper:
    @staticmethod
    def parse_xml(xml_str, parser=None):
        return etree.fromstring(xml_str, parser)

    @staticmethod
    def parse_xml_from_file(xml_path):
        utf8_parser = etree.XMLParser(encoding='utf-8')
        xml_str = open(xml_path).read()
        return etree.fromstring(xml_str, parser=utf8_parser)

    @staticmethod
    def get_root_node(node):
        return node.getroot()

    @staticmethod
    def get_child_node(parent_node, child_name, find_prefix=''):
        return parent_node.find(find_prefix + child_name)

    @staticmethod
    def get_all_child_node(parent_node, child_name, find_prefix=''):
        return parent_node.findall(find_prefix + child_name)

    @staticmethod
    def get_child_node_by_attr(parent_node, child_name, attr_name, attr_value, find_prefix=''):
        return parent_node.find(find_prefix + child_name + '[@' + attr_name + '=\'' + attr_value + '\']')

    @staticmethod
    def get_all_child_node_by_attr(parent_node, child_name, attr_name, attr_value):
        return parent_node.findall(child_name + '[@' + attr_name + '=\'' + attr_value + '\']')

    @staticmethod
    def get_node_name(node):
        return node.tag

    @staticmethod
    def get_node_text(node):
        return node.text

    @staticmethod
    def get_node_attr_list(node):
        return node.keys()

    @staticmethod
    def get_node_attr(node, attribute_name, find_prefix=''):
        return node.get(find_prefix + attribute_name)

    @staticmethod
    def get_node_prefix(node, prefix_name):
        prefix = ''
        for attrib_name, value in node.attrib.items():
            if attrib_name[0] == "{":
                prefix, ignore, tag = attrib_name[1:].partition("}")
                return "{" + prefix + "}"

        if len(prefix) == 0:
            node_tag = node.tag
            if node_tag[0] == "{":
                prefix, ignore, tag = node_tag[1:].partition("}")
                return "{" + prefix + "}"

        return prefix

    @staticmethod
    def get_string_from_xml(node):
        etree.register_namespace("", "http://schemas.qualisystems.com/ResourceManagement/DriverCommandResult.xsd")

        str_data = etree.tostring(node, 'utf-8')
        return str_data.replace('\n', '\r\n')

    @staticmethod
    def get_node_child_count(node):
        count = 0
        for child_node in node:
            count += 1

        return count

