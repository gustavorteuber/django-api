from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Usuario, Dolar, Contatos, Banner, saq, Indice, acoes
from uploader.models import Image
from uploader.serializers import ImageSerializer

class UsuarioSerializer(ModelSerializer):
    
    password_confirmation = serializers.CharField(max_length=150, write_only=True)
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
        
    )
    foto = ImageSerializer(required=False, read_only=True, default=None)
    id = serializers.IntegerField(read_only=True, required=False)
    

    class Meta:
        model = Usuario
        read_only_fields = ('id', )
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password_confirmation', 'foto', 'foto_attachment_key', 'is_superuser')


    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        password = args.get('password')
        password_confirmation = args.get('password_confirmation')
        print(username)
        print(password)
        print(password_confirmation)
        if password != password_confirmation:
            raise serializers.ValidationError({'password': ('as senhas não são iguais')})
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('esse email já está cadastrado')})
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('esse nome de usuario já está em uso')})

        return super().validate(args)
  


class UsuarioCreateSerializer(ModelSerializer):
    
    password_confirmation = serializers.CharField(max_length=150, write_only=True)
    id = serializers.IntegerField(read_only=True, required=False)
    

    class Meta:
        model = Usuario
        read_only_fields = ('id', )
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password_confirmation')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        password = args.get('password')
        password_confirmation = args.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({'password': ('As senhas não são iguais')})
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('o email ja existe')})
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('esse nome de usuario ja está em uso')})

        return super().validate(args)
  

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        newUser = Usuario.objects.create_user(**validated_data)
        newUser.foto = None
        newUser.save()
        return newUser


class DolarSerializer(ModelSerializer):
    class Meta:
        model = Dolar
        fields = "__all__"


class DetailDolarSerializer(ModelSerializer):
    class Meta:
        model = Dolar
        fields = "__all__"
        depth = 1
      
class IndiceSerializer(ModelSerializer):
    class Meta:
        model = Indice
        fields = "__all__"


class DetailIndiceSerializer(ModelSerializer):
    class Meta:
        model = Indice
        fields = "__all__"
        depth = 1
      

class ContatosSerializer(ModelSerializer):
    class Meta:
        model = Contatos
        fields = "__all__"


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
        
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )

    foto = ImageSerializer(required=False, read_only=True)



class DetailBannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
        depth = 1

class saqSerializer(ModelSerializer):
    class Meta:
        model = saq
        fields = "__all__"
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

class DetailsaqSerializer(ModelSerializer):
    class Meta:
        model = saq
        fields = "__all__"
        depth = 1

class acoesSerializer(ModelSerializer):
    class Meta:
        model = acoes
        fields = "__all__"


class DetailacoesSerializer(ModelSerializer):
    class Meta:
        model = acoes
        fields = "__all__"
        depth = 1