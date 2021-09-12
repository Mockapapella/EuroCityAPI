# EuroCityAPI

This is just a basic POC for an API that accepts a european city name and returns the country it is located in. Previous requests are cached to improve performance.

# Setup

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# GET request

### case insensitive, handles English variants

```
curl http://localhost:8000/country/london/
curl http://localhost:8000/country/LoNdOn/
```

### cities outside of europe return 400 error

```
curl http://localhost:8000/country/beijing/
```

### any other queries return 404 error

```
curl http://localhost:8000/country/moon/
curl http://localhost:8000/country/❤️/
curl http://localhost:8000/country/Kyïv/
```
