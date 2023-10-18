from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        description="Rota para criação de álbuns.",
        tags=["Criação de usuários"],
        parameters=[
            UserSerializer,
        ],
    )
    def post(self, request):
        return self.create(request)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        description="Rota para listagem de usuário por ID",
        tags=["Listagem, atualização e deleção de usuário"],
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Rota para atualização de usuário por ID",
        tags=["Listagem, atualização e deleção de usuário"],
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Rota para deleção de usuário por ID",
        tags=["Listagem, atualização e deleção de usuário"],
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
