"""
Date: 11/04/2019
This file SCRUB's acord XML for security reason. This does not encrypt content. All that it does
is search for elemets and removes their children
say, 
    <NameInfo>
        <PersonName>
            <FirstName>sdjkf</FirstName>
            <LastName>sdkge</LastName>
        </PersonName>
    </NameInfo> 
    
    becomes
    <NameInfo>
        <PersonName/>
    </NameInfo>

For few other cases like 
    <PolicyNumber>CCC200 22 1234</PolicyNumber>
    is changed to
    <PolicyNumber />
To invoke this file do
    python3 scrub_acord_xml.py -i ./data/sample.xml
    python scrub_acord_xml.py -i ./data/sample.xml

Note: This works on both python3 & python2
"""

import sys, getopt
import xml.etree.ElementTree as ET

def load_xml_file(xml_file):
    try:
        tree = ET.parse(xml_file)
        return tree
    except Exception as e:
        print("ERROR: Failed to open XML file")
        print(e)


def find_and_print_element(tree, element):
    items = tree.findall(element)
    print("Found {} matches".format(len(items)))
    for item in items:
        print(item.text)


def find_and_clear_element(tree, elements):
    for element in elements:
        items = tree.findall(element)
        print("Found {} matches".format(len(items)))
        for item in items:
            # print(item)
            item.clear()
    

def encrypt_content(content):
    pass


def find_and_encrypt_data_in_element(tree, elements):
    pass


def save_tree_to_xml(tree, file_path):
    try:
        tree.write(file_path)
    except Exception as e:
        print('ERROR: Failed to save contents to file - {0}'.format(file_path))
        print(e)

def main(file_name):
    tree = load_xml_file(file_name)
    print('XML loaded successfully!')
    # find_and_print_element(tree, ".//PolicyNumber")
    find_and_clear_element(tree, [
        ".//PolicyNumber",
        ".//NameInfo/PersonName", ".//NameInfo/TaxIdentity",
        ".//Communications/PhoneInfo", ".//Communications/EmailInfo", 
        ".//BusinessInfo/SICCD", ".//BusinessInfo/NCCIIDNumber", 
        ".//Producer/ProducerInfo", 
        ".//DriverInfo/PersonInfo",".//DriverInfo/License",
        ".//WorkCompPolicyQuoteInqRq/Producer"
        ])
    save_tree_to_xml(tree, file_name)
    print('File changes done and saved to {0}'.format(file_name))


if __name__ == "__main__":
    inputfile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["xmlfile="])
    except getopt.GetoptError:
        print('main.py -i <xmlfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <xmlsfile>')
            sys.exit()
        elif opt in ("-i", "--xmlfile"):
            inputfile = arg
    main(inputfile)