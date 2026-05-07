from flask import Flask, request, jsonify
import requests
from datetime import datetime
import os

app = Flask(__name__)

# TMDb API Configuration
TMDB_API_KEY = "e92ac64145126a30c6e764680e603bff"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

# ==================== Health Check ====================
@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if API is running"""
    return jsonify({
        "status": "healthy",
        "message": "API is running",
        "timestamp": datetime.now().isoformat()
    }), 200

# ==================== Genre Endpoints ====================
@app.route('/api/genres', methods=['GET'])
def get_genres():
    """Get all available genres from TMDb"""
    try:
        url = f"{TMDB_BASE_URL}/genre/movie/list"
        params = {"api_key": TMDB_API_KEY}
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "genres": data.get('genres', [])
            }), 200
        else:
            return jsonify({"error": "Failed to fetch genres"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Movie Filtering Endpoints ====================
@app.route('/api/movies/genre', methods=['GET'])
def filter_by_genre():
    """Filter movies by genre"""
    try:
        genre_id = request.args.get('genre_id')
        page = request.args.get('page', 1, type=int)
        
        if not genre_id:
            return jsonify({"error": "genre_id parameter is required"}), 400
        
        url = f"{TMDB_BASE_URL}/discover/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "with_genres": genre_id,
            "page": page,
            "sort_by": "popularity.desc"
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "movies": data.get('results', [])
            }), 200
        else:
            return jsonify({"error": "Failed to fetch movies"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/movies/year', methods=['GET'])
def filter_by_year():
    """Filter movies by release year"""
    try:
        year = request.args.get('year')
        page = request.args.get('page', 1, type=int)
        
        if not year:
            return jsonify({"error": "year parameter is required"}), 400
        
        url = f"{TMDB_BASE_URL}/discover/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "primary_release_year": year,
            "page": page,
            "sort_by": "popularity.desc"
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "movies": data.get('results', [])
            }), 200
        else:
            return jsonify({"error": "Failed to fetch movies"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/movies/filter', methods=['GET'])
def filter_movies():
    """Advanced filter: Genre + Year + Sorting"""
    try:
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        page = request.args.get('page', 1, type=int)
        sort_by = request.args.get('sort_by', 'popularity.desc')
        
        url = f"{TMDB_BASE_URL}/discover/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "page": page,
            "sort_by": sort_by
        }
        
        # Add optional filters
        if genre_id:
            params["with_genres"] = genre_id
        if year:
            params["primary_release_year"] = year
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "movies": data.get('results', []),
                "applied_filters": {
                    "genre_id": genre_id,
                    "year": year,
                    "sort_by": sort_by
                }
            }), 200
        else:
            return jsonify({"error": "Failed to fetch movies"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Movie Details ====================
@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    """Get detailed information about a specific movie"""
    try:
        url = f"{TMDB_BASE_URL}/movie/{movie_id}"
        params = {"api_key": TMDB_API_KEY}
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "movie": data
            }), 200
        else:
            return jsonify({"error": "Movie not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Search ====================
@app.route('/api/search', methods=['GET'])
def search_movies():
    """Search movies by title"""
    try:
        query = request.args.get('q')
        page = request.args.get('page', 1, type=int)
        
        if not query:
            return jsonify({"error": "q (search query) parameter is required"}), 400
        
        url = f"{TMDB_BASE_URL}/search/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "query": query,
            "page": page
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "search_query": query,
                "movies": data.get('results', [])
            }), 200
        else:
            return jsonify({"error": "Search failed"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Trending ====================
@app.route('/api/trending', methods=['GET'])
def get_trending():
    """Get trending movies (daily or weekly)"""
    try:
        time_window = request.args.get('time_window', 'week')  # day or week
        page = request.args.get('page', 1, type=int)
        
        if time_window not in ['day', 'week']:
            time_window = 'week'
        
        url = f"{TMDB_BASE_URL}/trending/movie/{time_window}"
        params = {
            "api_key": TMDB_API_KEY,
            "page": page
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "time_window": time_window,
                "movies": data.get('results', [])
            }), 200
        else:
            return jsonify({"error": "Failed to fetch trending movies"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Top Rated ====================
@app.route('/api/top-rated', methods=['GET'])
def get_top_rated():
    """Get top-rated movies"""
    try:
        page = request.args.get('page', 1, type=int)
        
        url = f"{TMDB_BASE_URL}/movie/top_rated"
        params = {
            "api_key": TMDB_API_KEY,
            "page": page
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "movies": data.get('results', [])
            }), 200
        else:
            return jsonify({"error": "Failed to fetch top-rated movies"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Recommendations ====================
@app.route('/api/recommendations/similar/<int:movie_id>', methods=['GET'])
def get_similar_movies(movie_id):
    """Get movies similar to the given movie"""
    try:
        page = request.args.get('page', 1, type=int)
        
        url = f"{TMDB_BASE_URL}/movie/{movie_id}/similar"
        params = {
            "api_key": TMDB_API_KEY,
            "page": page
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "success": True,
                "page": data.get('page'),
                "total_pages": data.get('total_pages'),
                "total_results": data.get('total_results'),
                "base_movie_id": movie_id,
                "similar_movies": data.get('results', [])
            }), 200
        else:
            return jsonify({"error": "Failed to fetch similar movies"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== Error Handlers ====================
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

# ==================== Main ====================
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
