from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from . models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('body', 'updated', 'created')