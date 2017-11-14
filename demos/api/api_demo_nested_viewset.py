from django.http import HttpResponse
from rest_framework import serializers, viewsets, status

from demos.models import ModelAuthorForRest, ModelBookForRestEx


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelAuthorForRest
        fields = ('first_name', 'last_name')


class SerializerPost(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    def create(self, validated_data):
        u = self.context['request'].user
        if not u.is_anonymous():
            model = ModelBookForRestEx()
            model.title = validated_data.get("title")
            model.author = u
            model.body = validated_data['body']
            model.save()
            return model

    class Meta:
        model = ModelBookForRestEx
        fields = '__all__'

from rest_framework import  generics
class ViewPostApi(generics.ListCreateAPIView):
    serializer_class = SerializerPost
    queryset = ModelBookForRestEx.objects.all()

class ViewPostExApi(viewsets.ModelViewSet):
    serializer_class = SerializerPost
    queryset = ModelBookForRestEx.objects.all()
