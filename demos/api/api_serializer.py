from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from demos.models import ModelBookForRest
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
from rest_framework.decorators import api_view

'''
Extending Serializer is low level stuff, and we have to implement create() and update(),
by doing so we will end-up rewriting boilerplate code over and over again, 
if we want we can take advatnage of OOP and extend from ModelSerializer which already
provides a default implementation for create and update to do what you most likely will, create the
object and updating the objuect based on input received from the user.
See my tutorial on ModelSerializer and HyperlinkSerializer
See my tutorial on how to manually serialize and deserialize using the shell
'''
class SerializerBook(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    isbn = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return ModelBookForRest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance

#@api_view(http_method_names=['GET','POST', 'PUT'])
@csrf_exempt
def view_api_serializer(request, pk=None):
    renderer = JSONRenderer()
    parser = JSONParser()
    if pk is None:
        if request.method == 'GET':
            books = ModelBookForRest.objects.all()
            serializer = SerializerBook(books, many=True)
            rendered = renderer.render(serializer.data)
            return HttpResponse(rendered, content_type='application/json')
        elif request.method == 'POST':
            data = parser.parse(request)
            unserializer = SerializerBook(data=data)
            if unserializer.is_valid():
                unserializer.save()
                return HttpResponse(renderer.render(unserializer.data), content_type='application/json')
            else:
                return HttpResponse(renderer.render(unserializer.errors), content_type='application/json',
                                    status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            book = ModelBookForRest.objects.get(pk=pk)
        except ModelBookForRest.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = SerializerBook(book)
            rendered = JSONRenderer().render(serializer.data)
            return HttpResponse(rendered, content_type='application/json')
        if request.method == 'PUT':
            parsed = parser.parse(request)
            unserializer = SerializerBook(book, data=parsed)
            if unserializer.is_valid():
                unserializer.save()
                rendered = renderer.render(unserializer.data)
                return HttpResponse(rendered, content_type='application/json')
            else:
                return HttpResponse(renderer.render(unserializer.errors), content_type='application/json',
                                    status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            unserializer = SerializerBook(book)
            json = unserializer.data
            rendered = renderer.render(json)
            book.delete()
            return HttpResponse(rendered, content_type='application/json')
