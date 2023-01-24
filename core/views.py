from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Contatos, Dolar, Indice, Banner, saq, acoes
from core.serializers import UsuarioSerializer, UsuarioCreateSerializer, ContatosSerializer,DetailContatosSerializer, DolarSerializer, DetailDolarSerializer, IndiceSerializer, DetailIndiceSerializer, DetailBannerSerializer, BannerSerializer,saqSerializer, DetailsaqSerializer, DetailacoesSerializer, acoesSerializer
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

class DolarViewSet(ModelViewSet):
    queryset = Dolar.objects.all()
    serializer_class = DolarSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailDolarSerializer
        return DolarSerializer

class IndiceViewSet(ModelViewSet):
    queryset = Indice.objects.all()
    serializer_class = IndiceSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailIndiceSerializer
        return IndiceSerializer


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailBannerSerializer
        return BannerSerializer

class acoesViewSet(ModelViewSet):
    queryset = acoes.objects.all()
    serializer_class = acoesSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailacoesSerializer
        return acoesSerializer

class saqViewSet(ModelViewSet):
    queryset = saq.objects.all()
    serializer_class = saqSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailsaqSerializer
        return saqSerializer