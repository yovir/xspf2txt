import xml.etree.ElementTree as ET

tree = ET.parse("playlist.xspf")
root = tree.getroot()
NS = '{http://xspf.org/ns/0/}'

for list in root.iter(NS + 'track'):
	judul = ''
	artist = ''
	for judul in ['title']:
		field = list.find(NS + judul)
		if field is None:
			judul = None
		else:
			judul = field.text
	
	for artist in ['creator']:
		field = list.find(NS + artist)
		if field is None:
			artist = None
		else:
			artist = field.text
	
	print(artist,'-',judul)