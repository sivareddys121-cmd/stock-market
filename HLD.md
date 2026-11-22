# High-Level Design (HLD): Stock Market Dashboard

## 1. System Overview

The Stock Market Dashboard follows a two-tier architecture:

```text
Browser (index.html)
  |  HTTP/JSON
  v
FastAPI Backend (app.py)
  |  Python API
  v
Stock Data Layer (data.py)
  |  yfinance
  v
Yahoo Finance market data
```

The frontend is responsible for user interaction and chart rendering. FastAPI exposes HTTP endpoints and delegates data retrieval and transformation to the data module.

## 2. Components

### 2.1 Frontend

- `index.html` provides the company selector, load control, and Chart.js canvas.
- JavaScript calls the FastAPI backend and renders closing prices as a line chart.
- During local development, the frontend calls `http://127.0.0.1:8000`.

### 2.2 API Service

- `app.py` creates the FastAPI application.
- `app.py` defines company, data, summary, and comparison endpoints.
- CORS middleware allows browser requests in development and deployment scenarios.

### 2.3 Data Access and Processing

- `data.py` downloads one year of historical data using `yfinance`.
- `preprocess_data()` normalizes DataFrame columns and adds indicators.
- Indicator calculations include daily return, 7-day moving average, 30-day moving average, and 52-week high/low.

## 3. API Interaction

| Endpoint | Purpose |
|---|---|
| `GET /companies` | Returns the supported stock symbols |
| `GET /data/{symbol}` | Returns the latest 30 prepared records |
| `GET /summary/{symbol}` | Returns summary statistics for a symbol |
| `GET /compare` | Compares the latest closing price for two symbols |

## 4. Error Handling

The backend should return a clear JSON error when a symbol is empty or no market data is available. Individual endpoint implementations must consistently validate their `yfinance` result before accessing DataFrame columns.

## 5. Deployment

The application can run with Uvicorn directly or through a container. In a container deployment, the application listens on port 8000 and serves the API through `uvicorn app:app --host 0.0.0.0 --port 8000`.

## 6. Scalability and Maintenance

- Cache or persist frequently requested market data to reduce external API calls.
- Replace `yfinance` with an approved market-data provider behind the existing data-access function if production limits require it.
- Move frontend API configuration to an environment-specific setting before deploying outside the local environment.
- Add automated tests around data validation, transformations, and endpoint responses.

