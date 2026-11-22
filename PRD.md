# Product Requirements Document (PRD): Stock Market Dashboard

## 1. Overview

The Stock Market Dashboard is a web application that retrieves historical stock data and presents basic 52-week and closing-price insights for selected Indian equities. It uses a FastAPI backend and a simple browser-based frontend.

## 2. Problem Statement

Users need a small, accessible way to review recent market data for a set of common NSE stocks without using a full trading platform. The application should expose a short list of supported symbols, retrieve their market history, calculate summary values, and display recent closing prices.

## 3. Target Users

- Individual investors reviewing basic historical trends.
- Students learning stock-market data and application development.
- Developers using the project as an example of a FastAPI and Chart.js integration.

## 4. Functional Requirements

### 4.1 Supported Companies

- The API must return a list containing INFY.NS, TCS.NS, RELIANCE.NS, HDFCBANK.NS, and ICICIBANK.NS.
- The frontend must allow the user to select a supported symbol.

### 4.2 Stock Data

- The system must retrieve one year of historical data for a requested NSE symbol.
- The system must return the latest 30 records for charting.
- Invalid symbols must return an error response rather than a stock-data list.
- The data response must use JSON-safe date values.

### 4.3 Data Preparation

- The system must calculate a daily return.
- The system must calculate 7-day and 30-day moving averages.
- The system must calculate rolling 52-week high and low values.
- Missing calculated values must be represented safely in the returned dataset.

### 4.4 Summary

- The system must return the 52-week high and low.
- The system must return the average closing price.
- Duplicate or conflicting summary implementations must not return inconsistent results.

### 4.5 Frontend

- The frontend must provide a company dropdown and load button.
- Selecting a company and loading data must draw a closing-price line chart.
- The chart must use the API data returned for the selected symbol.

## 5. Non-Functional Requirements

- The API must expose interactive documentation through FastAPI.
- The frontend and API must support local development on separate local ports.
- CORS must allow the browser frontend to call the API.
- The application must be deployable as a container or on a process-based Python host.

## 6. Assumptions

- Market data is provided by Yahoo Finance through `yfinance`.
- A network connection is available when stock data is requested.
- The application is intended for basic analysis and not as a real-time trading or investment advisory service.

