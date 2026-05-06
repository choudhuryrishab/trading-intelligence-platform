# System Diagram

```text
                ┌────────────────────┐
                │   Trading212 API   │
                └─────────┬──────────┘
                          │
                          ▼
        ┌────────────────────────────────┐
        │      Backend (Python API)      │
        │  - Data Fetcher               │
        │  - RSI / Metrics Engine      │
        │  - Portfolio Processor       │
        └─────────┬──────────────────────┘
                  │
                  ▼
        ┌────────────────────────────┐
        │     Database Layer        │
        │  - Portfolio history      │
        │  - Indicators storage     │
        └─────────┬──────────────────┘
                  │
                  ▼
        ┌────────────────────────────┐
        │   API Layer (FastAPI)     │
        └─────────┬──────────────────┘
                  │
                  ▼
        ┌────────────────────────────┐
        │   Frontend Dashboard      │
        │   (Streamlit / Web UI)    │
        └─────────┬──────────────────┘
                  │
                  ▼
        📱 Laptop / Phone Browser Access