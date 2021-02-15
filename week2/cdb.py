import xml.etree.ElementTree as ET
import argparse
import sys


def get_adjectives(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    sample_filtered = [
        child.attrib['form'] for child in root if child.attrib['pos'] == "ADJ"]

    sample_filtered_nodup = []
    for item in sample_filtered:
        if item not in sample_filtered_nodup:
            sample_filtered_nodup.append(item)
    return sample_filtered_nodup


def main(argv):
    print(get_adjectives(argv[1]))


if __name__ == "__main__":
    main(sys.argv)
