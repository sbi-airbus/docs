from docutils import nodes
from docutils.parsers.rst import Directive, directives
#from docutils.parsers.rst.roles import set_classes


class UP42ImageList(Directive):

    def run(self):

        fruits = ['Apples', 'Oranges', 'Bananas']
        lst = nodes.bullet_list()
        lst['class'] = 'foobar'
        for fruit in fruits:
            item = nodes.list_item()
            
            lst += item
            item += nodes.paragraph(text=fruit)

        return [lst]

def setup(app):
    app.add_directive("foolist", UP42ImageList)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
