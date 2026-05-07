# Movie Recommendation System - Simplified Backend

A lightweight Python Flask backend for movie recommendations using TMDb API with simple filtering by genre, year, and era. No database required!

## Features

✨ **Simple Filtering**
- Filter movies by **Genre** (Action, Comedy, Drama, etc.)
- Filter movies by **Year** (Release year)
- Filter movies by **Genre + Year** combination
- Search movies by title
- Get trending movies
- Get top-rated movies
- Get similar movies (content-based)

📚 **No Database Required**
- Uses TMDb API directly
- No authentication complexity (API key based)
- Lightning-fast responses
- Real-time movie data

## Tech Stack

- **Framework**: Flask 2.3.2
- **API**: The Movie Database (TMDb) API
- **HTTP Requests**: Requests library

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Quick Setup

1. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

2. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
```
GET /api/health
```

### Get All Genres
```
GET /api/genres
```
Returns list of all available movie genres with their IDs.

### Filter by Genre
```
GET /api/movies/genre?genre_id=28&page=1
```
**Parameters:**
- `genre_id` (required): Genre ID
- `page` (optional): Page number (default: 1)

**Example:** `/api/movies/genre?genre_id=28` → Action movies

### Filter by Year
```
GET /api/movies/year?year=2023&page=1
```
**Parameters:**
- `year` (required): Release year
- `page` (optional): Page number (default: 1)

### Advanced Filter (Genre + Year)
```
GET /api/movies/filter?genre_id=28&year=2023&page=1&sort_by=popularity.desc
```
**Parameters:**
- `genre_id` (optional): Genre ID
- `year` (optional): Release year
- `page` (optional): Page number
- `sort_by` (optional): Sorting option
  - `popularity.desc` (most popular)
  - `popularity.asc`
  - `release_date.desc` (newest)
  - `release_date.asc`
  - `vote_average.desc` (highest rated)
  - `vote_average.asc`

### Get Movie Details
```
GET /api/movies/{movie_id}
```
Returns complete details of a specific movie.

### Search Movies
```
GET /api/search?q=Inception&page=1
```
**Parameters:**
- `q` (required): Search query (movie title)
- `page` (optional): Page number

### Get Trending Movies
```
GET /api/trending?time_window=week&page=1
```
**Parameters:**
- `time_window` (optional): `day` or `week` (default: week)
- `page` (optional): Page number

### Get Top Rated Movies
```
GET /api/top-rated?page=1
```
**Parameters:**
- `page` (optional): Page number

### Get Similar Movies
```
GET /api/recommendations/similar/{movie_id}
```
Returns movies similar to the given movie (content-based recommendation).

## Popular Genre IDs

| Genre | ID |
|-------|-----|
| Action | 28 |
| Adventure | 12 |
| Animation | 16 |
| Comedy | 35 |
| Crime | 80 |
| Documentary | 99 |
| Drama | 18 |
| Family | 10751 |
| Fantasy | 14 |
| Horror | 27 |
| Romance | 10749 |
| Science Fiction | 878 |
| Thriller | 53 |

## Usage Examples

### 1. Get Action Movies from 2023
```bash
curl "http://localhost:5000/api/movies/filter?genre_id=28&year=2023"
```

### 2. Get Comedy Movies
```bash
curl "http://localhost:5000/api/movies/genre?genre_id=35"
```

### 3. Search for a Specific Movie
```bash
curl "http://localhost:5000/api/search?q=Inception"
```

### 4. Get Top Rated Movies
```bash
curl "http://localhost:5000/api/top-rated"
```

### 5. Get Similar Movies to Movie ID 550
```bash
curl "http://localhost:5000/api/recommendations/similar/550"
```

### 6. Get Trending Movies This Week
```bash
curl "http://localhost:5000/api/trending?time_window=week"
```

### 7. Get Drama Movies from 2020, Sorted by Rating
```bash
curl "http://localhost:5000/api/movies/filter?genre_id=18&year=2020&sort_by=vote_average.desc"
```

## API Response Format

**Success Response:**
```json
{
  "success": true,
  "page": 1,
  "total_pages": 100,
  "total_results": 2000,
  "movies": [
    {
      "id": 550,
      "title": "Fight Club",
      "overview": "An insomniac office worker...",
      "poster_path": "/path/to/poster.jpg",
      "release_date": "1999-10-15",
      "vote_average": 8.8,
      "genre_ids": [18, 53],
      "popularity": 85.5
    }
  ]
}
```

**Error Response:**
```json
{
  "error": "Error message"
}
```

## Project Structure

```
backend/
├── app.py              # Main Flask application (220 lines)
├── requirements.txt    # Python dependencies (3 packages)
└── README.md          # Documentation
```

## How It Works

1. **No Database** - All movie data fetches directly from TMDb API
2. **API Key Based** - Uses your TMDb API key for authentication
3. **Real-time Data** - Always returns the latest movie information
4. **Simple Filters** - Easy-to-use query parameters for filtering by genre, year, era

## Key Features

✅ **Genre Filtering** - Filter by 13+ movie genres  
✅ **Year Filtering** - Filter by release year  
✅ **Combined Filtering** - Genre + Year together  
✅ **Sorting Options** - Sort by popularity, rating, or release date  
✅ **Search** - Search movies by title  
✅ **Trending** - Get trending movies (daily/weekly)  
✅ **Top Rated** - Get highest-rated movies  
✅ **Recommendations** - Similar movies (content-based)  
✅ **No Database** - Lightweight and fast  
✅ **API Key Ready** - Pre-configured TMDb API  

## Running the Backend

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py

# Server runs at http://localhost:5000
```

## Example Use Cases

### Use Case 1: Movie Night Selection
Find all action movies from 2023:
```bash
curl "http://localhost:5000/api/movies/filter?genre_id=28&year=2023&sort_by=popularity.desc"
```

### Use Case 2: Classic Drama Films
Get top-rated drama movies from 2010s:
```bash
curl "http://localhost:5000/api/movies/filter?genre_id=18&year=2015&sort_by=vote_average.desc"
```

### Use Case 3: Latest Recommendations
Get movies similar to a favorite movie:
```bash
curl "http://localhost:5000/api/recommendations/similar/550"
```

### Use Case 4: Quick Movie Search
Search for a specific movie:
```bash
curl "http://localhost:5000/api/search?q=The%20Shawshank%20Redemption"
```

## Error Handling

The API handles various errors gracefully:
- Missing required parameters
- Invalid genre IDs or years
- TMDb API errors
- Connection issues

All errors return a JSON response with descriptive messages.

## Advantages

✨ **Lightweight** - Minimal dependencies (just 3 packages)  
⚡ **Fast** - No database overhead  
🔧 **Easy to Use** - Simple query parameters  
🎯 **Flexible** - Combine multiple filters  
📊 **Real-time** - Always updated data  
🚀 **Scalable** - Can handle large volumes  

## Future Enhancements

- 💾 Response caching for faster queries
- 📊 Advanced analytics endpoints
- 🔄 Batch recommendations
- 📱 Mobile optimization
- 🌐 Multi-language support

## Troubleshooting

**Issue: Port 5000 already in use**
- Change port in app.py: `app.run(debug=True, port=5001)`

**Issue: No movies returned**
- Verify genre_id is valid (1-37)
- Check that year is valid (1800-2100)

**Issue: API returns 401**
- Ensure API key is correct and active on TMDb

## Support

For issues or questions, please open an issue on the GitHub repository.
