import frontik.doc
import frontik.handler
from frontik import etree

class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.doc.put(frontik.doc.Doc(root_node_name='doc'))
        self.doc.put(frontik.doc.Doc(root_node_name='ok'))
