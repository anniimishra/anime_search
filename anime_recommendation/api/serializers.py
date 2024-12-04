from rest_framework import serializers
from .models import User, CachedAnime
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use the custom User model
        fields = ['username', 'password', 'preferences', 'watched_anime']

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])  # Hash the password
        user.preferences = validated_data.get('preferences', {})  # Set preferences
        user.watched_anime = validated_data.get('watched_anime', [])  # Set watched anime
        user.save()
        return user

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CachedAnime
        fields = '__all__'
