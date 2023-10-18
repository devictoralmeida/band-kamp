from django.shortcuts import get_object_or_404
from albums.models import Album
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @extend_schema(
        description="Rota para listagem de músicas",
        tags=["Criação e listagem de músicas"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        description="Rota para criação de uma música",
        tags=["Criação e listagem de músicas"],
        parameters=[
            SongSerializer,
        ],
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        serializer.save(album=album)
