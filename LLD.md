# Low-Level Design (LLD): Stock Market Dashboard

## 1. Module Structure

```text
app.py          FastAPI application and HTTP routes
data.py         yfinance access and DataFrame preparation
index.html      Browser UI and Chart.js rendering
requirement.txt Python dependencies
docker          Container build configuration
procfile        Process-host startup command
```

## 2. Data Module

### `get_stock_data(symbol)`

1. Calls `yfinance.download(symbol, period="1y")`.
2. Checks whether the returned DataFrame is empty.
3. Resets the DataFrame index.
4. Returns the DataFrame to the caller.

### `preprocess_data(df)`

1. Normalizes DataFrame column names.
2. Calculates `Daily Return` as `(Close - Open) / Open`.
3. Calculates `7 Day MA` over seven rows.
4. Calculates `30 day MA` over thirty rows.
5. Calculates rolling `52 High` and `52 Low` values over 252 rows.
6. Replaces missing values with zero.

## 3. API Module

### Companies

`GET /companies` returns a static list:

```text
INFY.NS
TCS.NS
RELIANCE.NS
HDFCBANK.NS
ICICIBANK.NS
```

### Data

`GET /data/{symbol}`:

1. Calls `get_stock_data(symbol)`.
2. Returns `{"error": "Invalid symbol"}` for an empty result.
3. Calls `preprocess_data(df)`.
4. Converts the `Date` column to text when present.
5. Returns the final 30 records with `to_dict(orient="records")`.

### Summary

`GET /summary/{symbol}`:

1. Retrieves one year of data.
2. Rejects an empty result.
3. Returns the maximum closing price as `52 High`.
4. Returns the minimum closing price as `52 Low`.
5. Returns the mean closing price as `Average Close`.

### Comparison

`GET /compare` receives `symbol1` and `symbol2` query parameters and returns their latest closing prices:

```json
{
  "INFY.NS": 1500.0,
  "TCS.NS": 3500.0
}
```

## 4. Frontend Behavior

1. Read the selected symbol from the company dropdown.
2. Request `/data/{symbol}` from the API.
3. Use the `Date` field for chart labels.
4. Use the `Close` field for chart values.
5. Create a Chart.js line chart in the `chart` canvas.

## 5. CORS Configuration

The FastAPI application enables CORS for all origins and all methods. Credentials are enabled in the current configuration, so deployment environments should restrict origins and credentials according to their security requirements.

## 6. Implementation Notes

- `app.py` contains a duplicate `/summary/{symbol}` route; remove the earlier implementation or merge the behavior into one route.
- `data.py` should validate that required `Open` and `Close` columns exist before preprocessing.
- The Docker configuration references `requirements.txt`, but the repository currently uses `requirement.txt`; these names must be aligned.
- Frontend requests should use a deployment-configurable API base URL instead of a hard-coded localhost address.
