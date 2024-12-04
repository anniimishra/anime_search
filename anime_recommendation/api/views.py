from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User, CachedAnime
from .serializers import UserSerializer, AnimeSerializer
import requests
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # Create the user with the validated data
            serializer.save()

            # Return a success response
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate the user using Django's built-in authenticate function
        user = authenticate(username=username, password=password)
        print(user)

        if user:
            # If authentication is successful, generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        else:
            # If authentication fails, return an error message
            return Response({"error": "Invalid credentials"}, status=400)
# Search Anime
class AnimeSearchView(APIView):
    def get(self, request):
        name = request.query_params.get("name")
        genre = request.query_params.get("genre")

        query = """
        query ($name: String, $genre: String) {
            Page {
                media(search: $name, genre: $genre, type: ANIME) {
                    id
                    title { romaji }
                    genres
                    popularity
                }
            }
        }
        """
        variables = {"name": name, "genre": genre}
        response = requests.post(
            "https://graphql.anilist.co",
            json={"query": query, "variables": variables}
        )
        return Response(response.json()["data"]["Page"]["media"])

# Recommendations
class RecommendationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        preferences = user.preferences.get("genres", [])
        recommended_anime = CachedAnime.objects.filter(
            genres__overlap=preferences
        ).order_by('-popularity')
        serializer = AnimeSerializer(recommended_anime, many=True)
        return Response(serializer.data)

# Manage Preferences
class PreferencesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(request.user.preferences)

    def post(self, request):
        request.user.preferences = request.data
        request.user.save()
        return Response({"message": "Preferences updated successfully!"})
