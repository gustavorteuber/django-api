from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Contatos, Publicacao, Banner, saq
from core.serializers import UsuarioSerializer, UsuarioCreateSerializer, ContatosSerializer,DetailContatosSerializer, PublicacaoSerializer, DetailPublicacaoSerializer, DetailBannerSerializer, BannerSerializer,saqSerializer, DetailsaqSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['is_superuser'] = self.user.is_superuser
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return UsuarioCreateSerializer
        return UsuarioSerializer

class ContatosViewSet(ModelViewSet):
    queryset = Contatos.objects.all()
    serializer_class = ContatosSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailContatosSerializer
        return ContatosSerializer

class PublicacaoViewSet(ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailPublicacaoSerializer
        return PublicacaoSerializer

class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailBannerSerializer
        return BannerSerializer

class saqViewSet(ModelViewSet):
    queryset = saq.objects.all()
    serializer_class = saqSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailsaqSerializer
        return saqSerializer