import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump

#-------------------------------------------------------------------------
class CommentedTreeBuilder(ET.TreeBuilder):
    def __init__(self, *args, **kwargs):
        super(CommentedTreeBuilder, self).__init__(*args, **kwargs)

    def comment(self, data):
            self.start(ET.Comment, {})
            self.data(data)
            self.end(ET.Comment)

def read_write():
    print ('---------------------------------------------------------')
    print ('Before: ElementTree ogirinal parser()')
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    dump (root)
    tree.write('original.xml', xml_declaration=True)

    print ('---------------------------------------------------------')
    print ('After:Commented parser dump')
    tree = ET.parse('sample.xml',parser=ET.XMLParser(target = CommentedTreeBuilder()))
    root = tree.getroot()
    dump (root)
    tree.write('commented_parser.xml',encoding='utf8',xml_declaration=True)


    print ('---------------------------------------------------------')
    print ('Commented root')
    try:
        tree = ET.parse('doubleroot.xml',parser=ET.XMLParser(target = CommentedTreeBuilder()))
    except:
        tree = ET.parse('doubleroot.xml')

    root = tree.getroot()
    dump (root)
    tree.write('commented_parser.xml',encoding='utf8',xml_declaration=True)

def read_element():
    tree = ET.parse('sample2.xml')
    root = tree.getroot()

    print ('ogrigianl----')
    dump(tree)
    for rank in root.iter('rank'):
        print (rank.get('updated'))
        new_rank = int(rank.text) + 1
        rank.text = str(new_rank)
        rank.set('updated New', 'yes')

    print ('after----')
    dump(tree)


if __name__ == "__main__":
    #read_write()
    read_element()