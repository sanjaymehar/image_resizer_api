from rest_framework import serializers
from .models import Imagee,Eimage,User
from rest_framework_simplejwt.tokens import RefreshToken
# create a serializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagee
        fields = "__all__"

class ISerializer(serializers.ModelSerializer):
    class Meta:
        model = Eimage
        fields = ['gray','thumbnail','medium','large']



class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password2 = serializers.CharField(min_length=4, write_only=True, required=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self,user):
        refresh = RefreshToken.for_user(user)
        refresh['user_email'] = user.email

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)
        
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}
