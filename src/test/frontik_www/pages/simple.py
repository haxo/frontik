import frontik.handler
from frontik import etree

class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.set_xsl('simple.xsl')

        self.doc.put(etree.Element('ok'))
