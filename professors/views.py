from professors.models import Professor
from professors.serializers import ProfessorSerializer
from rest_framework import mixins
from rest_framework import generics

class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
