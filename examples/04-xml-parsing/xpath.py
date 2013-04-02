# from StringIO import StringIO
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
print 'Print the street of the address of the first person in xml'
print first_person.xpath('address/street')[0].text


import lxml.etree as etree
import io
data = """
<root xmlns="http://my-xmlns.com/foo">
	<person>
		<name>John</name>
		<address>
			<home>
				<street>Hill Street</street>
			</home>
			<office>
				<street>Wall Street</street>
			</office>
		</address>
	</person>
	<person>
		<name>Jeff</name>
		<address>
			<home>
				<street>Bay Street</street>
			</home>
			<office>
				<street>Water Street</street>
			</office>
		</address>
	</person>
</root>
"""

xslt='''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" indent="no"/>

<xsl:template match="/|comment()|processing-instruction()">
    <xsl:copy>
      <xsl:apply-templates/>
    </xsl:copy>
</xsl:template>

<xsl:template match="*">
    <xsl:element name="{local-name()}">
      <xsl:apply-templates select="@*|node()"/>
    </xsl:element>
</xsl:template>

<xsl:template match="@*">
    <xsl:attribute name="{local-name()}">
      <xsl:value-of select="."/>
    </xsl:attribute>
</xsl:template>
</xsl:stylesheet>
'''

print 'Using xslt to get rid of namespaces'

xslt_doc=etree.parse(io.BytesIO(xslt))
transform=etree.XSLT(xslt_doc)
dom = etree.parse(io.BytesIO(data))
root = transform(dom)

# first_person = root[0]
print 'Print the street of the office address of the first person in xml'
print root.find('.//home/street').text


