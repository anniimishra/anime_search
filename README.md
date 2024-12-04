**Anime Recommendation System**  

This is a backend project built with Django, Django Rest Framework (DRF), and PostgreSQL. The system integrates with the AniList GraphQL API to recommend anime based on user preferences such as genre, popularity, and previously watched anime. It also supports user registration, login (with JWT authentication), and allows users to manage their preferences.  


**Features**  

User Authentication: Register, login, and manage user sessions using JWT-based authentication.
Anime Search: Search for anime by name or genre using the AniList GraphQL API.
Anime Recommendations: Get anime recommendations based on the user's preferences.
User Preferences: Manage favorite genres and preferences for more accurate recommendations.  

**Technologies Used**  

Django: Backend framework.
Django Rest Framework (DRF): For creating RESTful APIs.
PostgreSQL: Database for storing user data and preferences.
AniList API: GraphQL API to fetch anime data.
JWT Authentication: For secure user login and registration.
Python: Programming language.  

**Requirements**  

Before running the project, make sure you have the following installed:

Python 3.8+
PostgreSQL
Pip (Python package installer)   

# API Endpoints

### 1. Register a New User (/auth/register)
- **Method**: `POST`
- **Body**:
```json
{
  "username": "user123",
  "password": "securepassword"
}
Response:
json
Copy code
{
  "message": "User created successfully!"
}
2. Login (/auth/login)
Method: POST
Body:
json
Copy code
{
  "username": "user123",
  "password": "securepassword"
}
Response:
json
Copy code
{
  "refresh": "refresh-token",
  "access": "access-token"
}
3. Search Anime (/anime/search)
Method: GET
Query Params:
name (optional) - The name of the anime.
genre (optional) - The genre of the anime.
Example Request:
http
Copy code
GET /anime/search?name=Naruto&genre=Action
Response:
json
Copy code
{
  "id": 1234,
  "title": { "romaji": "Naruto" },
  "genres": ["Action", "Adventure"],
  "popularity": 8000
}
4. Get User Preferences (/user/preferences)
Method: GET
Response:
json
Copy code
{
  "genres": ["Action", "Comedy"]
}
5. Update User Preferences (/user/preferences)
Method: POST
Body:
json
Copy code
{
  "genres": ["Action", "Comedy", "Romance"]
}
Response:
json
Copy code
{
  "message": "Preferences updated successfully!"
}






