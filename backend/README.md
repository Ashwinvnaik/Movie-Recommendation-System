# Movie Recommendation System - Backend

A Python-based backend for a movie recommendation system using Flask, featuring content-based filtering, collaborative filtering, and hybrid recommendation algorithms.

## Features

✨ **Recommendation Engines**
- **Content-Based Filtering**: Recommends movies similar to those liked by the user
- **Collaborative Filtering**: Suggests movies based on preferences of similar users
- **Hybrid Approach**: Combines both techniques for improved recommendations

📚 **Core Functionality**
- Movie database management (CRUD operations)
- User profile management
- Rating system for movies
- Search functionality for movies
- Pagination support for large datasets
- RESTful API endpoints

## Tech Stack

- **Framework**: Flask 2.3.2
- **Database**: SQLAlchemy ORM (SQLite for development)
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Additional**: Flask-CORS for cross-origin requests

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Ashwinvnaik/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

2. **Create a virtual environment**
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
cp .env.example .env
# Edit .env if needed (default settings work for development)
```

5. **Seed sample data** (optional)
```bash
python seed_data.py
```

## Running the Application

```bash
cd backend
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- `GET /api/health` - Check if API is running

### Movies
- `GET /api/movies` - Get all movies (with pagination)
- `GET /api/movies/<id>` - Get a specific movie
- `POST /api/movies` - Create a new movie
- `PUT /api/movies/<id>` - Update a movie
- `DELETE /api/movies/<id>` - Delete a movie
- `GET /api/movies/search?q=<query>` - Search movies by title or genre

### Users
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get a specific user
- `POST /api/users` - Create a new user

### Ratings
- `GET /api/ratings` - Get all ratings
- `GET /api/ratings/<id>` - Get a specific rating
- `POST /api/ratings` - Create/update a rating
- `DELETE /api/ratings/<id>` - Delete a rating

### Recommendations
- `GET /api/recommendations/content-based/<movie_id>?count=5` - Content-based recommendations
- `GET /api/recommendations/collaborative/<user_id>?count=5` - Collaborative recommendations
- `GET /api/recommendations/hybrid/<user_id>?count=5&movie_id=<optional>` - Hybrid recommendations
- `GET /api/recommendations/stats` - Get system statistics

## API Usage Examples

### Get All Movies
```bash
curl http://localhost:5000/api/movies
```

### Create a Movie
```bash
curl -X POST http://localhost:5000/api/movies \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Movie Name",
    "genre": "Action,Drama",
    "language": "English",
    "director": "Director Name",
    "cast": "Actor1,Actor2",
    "release_year": 2020,
    "rating": 8.5,
    "description": "Movie description"
  }'
```

### Create a User
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com"
  }'
```

### Rate a Movie
```bash
curl -X POST http://localhost:5000/api/ratings \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "movie_id": 1,
    "rating": 4.5
  }'
```

### Get Content-Based Recommendations
```bash
curl http://localhost:5000/api/recommendations/content-based/1?count=5
```

### Get Collaborative Recommendations
```bash
curl http://localhost:5000/api/recommendations/collaborative/1?count=5
```

### Get Hybrid Recommendations
```bash
curl http://localhost:5000/api/recommendations/hybrid/1?count=5
```

## Project Structure

```
backend/
├── app.py                      # Flask application factory
├── config.py                   # Configuration settings
├── models.py                   # Database models (Movie, User, Rating)
├── routes.py                   # API endpoints
├── recommendation_engine.py    # Recommendation algorithms
├── seed_data.py               # Database seeding script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
└── movies.db                 # SQLite database (created after first run)
```

## How Recommendation Algorithms Work

### Content-Based Filtering
1. Extracts features from movies (genre, cast, director, description)
2. Creates TF-IDF vectors from combined text features
3. Calculates cosine similarity between movies
4. Returns movies most similar to the input movie

### Collaborative Filtering
1. Creates user-item rating matrix
2. Applies Truncated SVD (Singular Value Decomposition)
3. Decomposes matrix into user factors and item factors
4. Predicts ratings for unrated movies
5. Returns top-rated predictions for the user

### Hybrid Approach
Combines both methods with configurable weights:
- Default: 50% content-based + 50% collaborative
- Returns recommendations ranked by combined score

## Database Models

### Movie
- id, title, genre, language, cast, director, release_year, rating, description, poster_url

### User
- id, username, email, password_hash, created_at

### Rating
- id, user_id, movie_id, rating (1-5 stars), created_at

## Configuration

Edit `backend/.env` to customize:
```
FLASK_ENV=development          # development or production
DATABASE_URL=sqlite:///movies.db
SECRET_KEY=your-secret-key
```

## Error Handling

The API returns consistent JSON responses:

**Success Response:**
```json
{
  "success": true,
  "data": {...},
  "message": "Operation successful"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message"
}
```

## Future Enhancements

- 🔐 User authentication and JWT tokens
- 📊 Advanced analytics and reporting
- 🎯 Matrix factorization techniques
- 🌐 Integration with external movie APIs
- 🚀 Caching for improved performance
- 📱 Mobile app support
- 🔄 Real-time recommendations
- 📈 A/B testing framework

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the GitHub repository.
