'''
Don't over create tags and context processors, use what you already have, if you need something more implement it
in your View which is where you have to put in place your business logic code, if it does
not fill your needs then as the last resort use custom tags.

There is a convention to name custom template tags with _tags suffice; Do not throw
an exception in your filter function, always return data so the filters can be chained together
You register filters with @template.Library().filter, if you want to expose a different name
than the function then do name=my_filter
usage
{% load custom_filter_tags %}
{{myvalue|to_hex}}
{{100|to_hex

The filters have a limitation, they take a required argument as input, and then they may
receive a second one, but no more than that. This is where tags come in to play.
Tags are implemented in a function-Node pair fashion, the function takes the input, performs the validation
then returns a Node.
function Tags always take as first argument the parser, and a token that contains everything inside {%%},
this means: the tag name as well as the arguments sent from the template. We call split_contents() to get
each component
'''

from django import template
from django.shortcuts import render
from django.template.defaultfilters import stringfilter
from django.template import loader
from django.template import Template
from datetime import datetime

register = template.Library()


### Filters ###
@register.filter
def to_hex(value):
    return '0x%.2x' % value


# stringfilter: optional, this makes sure the first argument is always converted to a string first,
# if you dont use it then you have to do the job manually str(text)
@register.filter
@stringfilter
def shrink(text, count):
    return text[:count]


# @register.filter(is_safe=True)
def nl2br(value):
    return value.replace('\\n', '<br />')


### Tags ###
@register.simple_tag
def join_them(delimiter,*args):
    return delimiter.join(args)

@register.tag
def make_pagination(parser, token):
    items = token.split_contents()[1:]
    return PageNode(items)


class PageNode(template.Node):
    def __init__(self, items):
        self.items = items

    def render(self, context):
        output = ""
        for item in self.items:
            template = Template('<li class="page-item"><a href="#" class="page-link">{{ item }}</a></li>')
            context.push({'item': item})
            output += template.render(context)

            # loader.render_to_string('partial/li.html', context)
        return output

def home(request):
    register.filter('nl2br', nl2br, is_safe=True)
    #register.tag('make_pagination', make_pagination)
    available_filters = ','.join([f for f in register.filters])
    return render(request, 'custom_filters_tags.html', {
        'demo_title': 'Custom Filters And Tags',
        'available_filters': available_filters,
        'long_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec diam est. Nunc quis magna non nisi imperdiet dictum. Maecenas et risus quis neque cursus fermentum in eget ex. Suspendisse potenti. Nulla orci sapien, tempus eget semper sed, interdum id urna. Proin lectus sem, feugiat vel urna nec, laoreet fringilla velit. Aenean congue aliquet tempor. Etiam tincidunt tempor ullamcorper. Cras mattis elit neque, eu pulvinar nibh facilisis quis. Aliquam lacinia dui leo, ac facilisis est scelerisque sit amet. Aenean mattis metus at euismod aliquam. Quisque fermentum mi non sapien malesuada euismod. Pellentesque sit amet eros pellentesque, ultrices quam id, tempor lorem. Nunc tristique malesuada efficitur. Donec rutrum eget neque condimentum bibendum.'})
