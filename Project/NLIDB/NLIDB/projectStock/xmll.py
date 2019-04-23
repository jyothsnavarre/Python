from lxml import etree

# create XML
fio=open('ti.txt','r')
fi = open('text.xml', 'wb')
for i in fio:
    root = etree.Element('root')
    root.append(etree.Element('child'))
    # another child with text
    child = etree.Element('child')
    child.text = i
    root.append(child)
    # pretty string
    s = etree.tostring(root, pretty_print=True)
    fi.write(s)
    print(s)