<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Documentation</title>
</head>
<body>

    <h1>API Endpoints</h1>

    <h2>1. Register a New User (/auth/register)</h2>
    <p><strong>Method:</strong> POST</p>
    <p><strong>Body:</strong></p>
    <pre>
    {
      "username": "user123",
      "password": "securepassword"
    }
    </pre>
    <p><strong>Response:</strong></p>
    <pre>
    {
      "message": "User created successfully!"
    }
    </pre>

    <hr>

    <h2>2. Login (/auth/login)</h2>
    <p><strong>Method:</strong> POST</p>
    <p><strong>Body:</strong></p>
    <pre>
    {
      "username": "user123",
      "password": "securepassword"
    }
    </pre>
    <p><strong>Response:</strong></p>
    <pre>
    {
      "refresh": "refresh-token",
      "access": "access-token"
    }
    </pre>

    <hr>

    <h2>3. Search Anime (/anime/search)</h2>
    <p><strong>Method:</strong> GET</p>
    <p><strong>Query Params:</strong></p>
    <ul>
        <li><strong>name</strong> (optional) - The name of the anime.</li>
        <li><strong>genre</strong> (optional) - The genre of the anime.</li>
    </ul>
    <p><strong>Example Request:</strong></p>
    <pre>
    GET /anime/search?name=Naruto&genre=Action
    </pre>
    <p><strong>Response:</strong></p>
    <pre>
    {
      "id": 1234,
      "title": { "romaji": "Naruto" },
      "genres": ["Action", "Adventure"],
      "popularity": 8000
    }
    </pre>

    <hr>

    <h2>4. Get User Preferences (/user/preferences)</h2>
    <p><strong>Method:</strong> GET</p>
    <p><strong>Response:</strong></p>
    <pre>
    {
      "genres": ["Action", "Comedy"]
    }
    </pre>

    <hr>

    <h2>5. Update User Preferences (/user/preferences)</h2>
    <p><strong>Method:</strong> PATCH</p>
    <p><strong>Body:</strong></p>
    <pre>
    {
      "genres": ["Action", "Comedy", "Romance"]
    }
    </pre>
    <p><strong>Response:</strong></p>
    <pre>
    {
      "message": "Preferences updated successfully!"
    }
    </pre>

</body>
</html>

