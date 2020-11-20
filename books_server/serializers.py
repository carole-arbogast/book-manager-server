from rest_framework import serializers
from .models import Book, Bookshelf
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ('id', 'name', 'user')


class BookSerializer(serializers.ModelSerializer):
    queryset = Bookshelf.objects.all()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['request'].method == 'GET':
            self.fields['bookshelf'] = BookshelfSerializer()
        else:
            self.fields['bookshelf'] = serializers.PrimaryKeyRelatedField(queryset=Bookshelf.objects.all())

    class Meta:
        model = Book
        depth=1
        partial=True
        fields = ('id', 'title', 'author', 'cover', 'rating', 'date_added', 'reading_status', 'bookshelf')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')