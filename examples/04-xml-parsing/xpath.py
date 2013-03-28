from StringIO import StringIO
import lxml.etree as etree

data = """
<root>
	<person>
		<name>John</name>
		<address>
			<street>Hill Street</street>
		</address>
	</person>
	<person>
		<name>Jeff</name>
		<address>
			<street>Bay Street</street>
		</address>
	</person>
</root>
"""

root = etree.fromstring(data)
first_person = root[0]
print 'street of the first person in xml'
print first_person.xpath('address/street/text()')
