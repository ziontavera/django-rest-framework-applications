# django-rest-framework-applications

# Project Name: Watchlist (IMDB Clone)

## Coverage:
1. Django Rest Framework intro
2. Views and Serializers
3. Postman
4. Permissions
5. Authentications (basic & Token Authentication)
6. Filtering, Searching, Ordering
7. Pagination

# Setup
1. Install pip: https://pip.pypa.io/en/latest/installation/
2. create a virtual environment: https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments
3. install django https://www.djangoproject.com/download/

# Usage (tested with postman):
## Admin Page:
http://127.0.0.1:8000/admin

## Accounts:
- login: `http://127.0.0.1:8000/accounts/login/`
- logout: `http://127.0.0.1:8000/accounts/logout/`
- register: `http://127.0.0.1:8000/accounts/register/`

## Movie List:
- all - `http://127.0.0.1:8000/movie/list/`
- paginated - `http://127.0.0.1:8000/movie/movie_list/`

## Movie Detail:
- `http://127.0.0.1:8000/movie/<int:movie_id>/`

## Streaming Platform List:
- `http://127.0.0.1:8000/movie/stream_list/`

## Streaming Platform detail:
- `http://127.0.0.1:8000/movie/stream_list/<int:streamplatform_id>`

## Movie Reviews:
- `http://127.0.0.1:8000/movie/<int:movie_id> /reviews`

## Review Details:
- `http://127.0.0.1:8000/movie/review/<int:review_id>/`

## Submit Reviews (must be logged in):
- `http://127.0.0.1:8000/movie/<int:movie_id>/submit_review`

## User Reviews:
- `http://127.0.0.1:8000/movie/reviews/?username=lebronjames`




