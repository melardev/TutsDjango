from rest_framework import serializers, viewsets
from demos.models import ModelBookForRest

class SerializerBook(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelBookForRest
        fields = '__all__'

class ViewBookApi(viewsets.ModelViewSet):
    serializer_class = SerializerBook
    queryset = ModelBookForRest.objects.all()
