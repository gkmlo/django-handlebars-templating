from django import template
from django.conf import settings
import pybars

register = template.Library()

class View(pystache.View):
    template_path = settings.STATICFILES_DIRS[0] + '/js/templates'

    def __init__(self, template_name, context):
        self.template_name = template_name
        return super(View, self).__init__(context=context)

class HandlebarsNode(template.Node):
    def __init__(self, template_path, attr=None):
        self.template = template_path
        self.attr = attr

    def render(self, context):
        mcontext = context[self.attr] if self.attr else {}
        compiler = Compiler()
        compiler.compile(self.template)
        return template(mcontext)

def do_handlebars(parser, token):
    """
    Loads a handlebars template and render it inline
    
    Example::
    
    {% handlebars "foo/bar" data %}
    
    """
    bits = token.split_contents()
    if len(bits) not in  [2,3]:
        raise template.TemplateSyntaxError("%r tag takes two arguments: the location of the template file, and the template context" % bits[0])
    path = bits[1]
    path = path[1:-1]
    attrs = bits[2:]
    return HandlebarsNode(path, *attrs)


register.tag("handlebars", do_handlebars)
