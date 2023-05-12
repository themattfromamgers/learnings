import xml.etree.cElementTree as ET

mytree = ET.parse('iksemel.xml')
root = mytree.getroot()


for etiket in root.iter('ad'):
        print(etiket.text)




# with open('settings.xml','w') as xmldosya:
#     xmldosya.write("ıjıj")
# xmldosya.close()