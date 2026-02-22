# API Client

Consume a REST API (weather or GitHub).

## Features to Implement

- [ ] Make GET requests to a REST API
- [ ] Parse JSON responses
- [ ] Handle API errors and rate limiting
- [ ] Format and display results
- [ ] Cache responses (optional)
- [ ] Support multiple endpoints

## Usage

```bash
pip install -r requirements.txt
python3 main.py
```

## Suggested APIs (no auth required)

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — fake REST API for testing
- [Open-Meteo](https://open-meteo.com/) — free weather API
- [GitHub API](https://api.github.com/) — public endpoints (no auth for basic queries)

## Concepts Used

- HTTP requests (requests library)
- JSON parsing
- Error handling
- API patterns (REST, pagination, rate limiting)
- Data formatting
