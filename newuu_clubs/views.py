from .serializers import ClubsSerializer
from rest_framework import generics
from .models import Clubs


class GetClubs(generics.ListAPIView):
    serializer_class = ClubsSerializer
    queryset = Clubs.objects.all()
