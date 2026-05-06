📄 docs/sessions/SESSION_001_initial_setup.md
# Session 001 — Initial Setup & Project Bootstrap

## 📅 Date
2026-05-06

---

## 🎯 Goal of this session

Set up the initial foundation of the Trading Intelligence Platform, including:

- GitHub repository structure
- FastAPI backend (mock portfolio service)
- Streamlit frontend dashboard
- Basic API communication between frontend and backend
- Virtual environment setup
- Initial project scaffolding for future expansion (Trading212 API, analytics, LLM integration)

---

## 🏗️ What was built

### 1. Project structure created


trading-intelligence-platform/
│
├── backend/
│ └── app/
│ ├── main.py
│ ├── config.py
│ ├── services/
│ ├── models/
│ ├── api/
│ └── core/
│
├── frontend/
│ └── streamlit_app.py
│
├── data/
│ ├── cache/
│ └── samples/
│
├── docs/
│ └── sessions/
│
├── scripts/
├── docker/
└── requirements.txt


---

### 2. Backend (FastAPI)

- Created FastAPI app in `backend/app/main.py`
- Added initial service layer:
  - `PortfolioService`
  - `mock_data.py`
- Basic endpoint:
  - `/portfolio`

---

### 3. Frontend (Streamlit)

- Created simple dashboard UI
- Fetches portfolio data from backend API
- Displays:
  - cash balance
  - stock holdings
  - total positions

---

### 4. Mock portfolio system

Initial data structure:

```json
{
  "cash": 1200,
  "stocks": [
    {"ticker": "AAPL", "quantity": 3, "avg_price": 170},
    {"ticker": "TSLA", "quantity": 2, "avg_price": 240},
    {"ticker": "MSFT", "quantity": 1, "avg_price": 380}
  ],
  "total_positions": 3
}
⚙️ Technical issues encountered
1. Python module import errors
ModuleNotFoundError: fastapi
ModuleNotFoundError: app
Root cause: incorrect execution context + module path confusion
2. Uvicorn startup issues
Incorrect usage of:
backend.app.main:app

Fixed by using:

uvicorn app.main:app --reload --app-dir backend
3. Streamlit backend connection error
Streamlit crashed when backend was not running
Fixed by running backend + frontend separately
4. Virtual environment confusion
Python interpreter mismatch caused missing packages initially
Fixed by consistently using .venv
🔧 Final working setup
Terminal 1 — Backend
cd backend
uvicorn app.main:app --reload
Terminal 2 — Frontend
streamlit run frontend/streamlit_app.py
📌 Current system state
Backend API running locally
Frontend dashboard functional
Mock portfolio service active
GitHub repository initialized and synced
Basic architecture validated
🚀 Next steps (Session 002)

Planned upgrades:

Data layer
Introduce SQLite or PostgreSQL
Persist portfolio history
Enable SQL querying capability
Trading212 integration
Replace mock data with API layer
Secure API key handling via .env
Analytics layer
Add:
RSI calculation
P/E ratio tracking
portfolio performance metrics
Visualization layer
Add charts in Streamlit dashboard
🧠 Long-term vision

Evolve into a system that:

Aggregates portfolio + market data
Runs analytics on holdings
Provides insights via dashboards + LLM interface
Supports future trade execution automation

---

# 🚀 Now let’s push it to GitHub

Run this from your project root:

```bash
git add docs/sessions/SESSION_001_initial_setup.md
git commit -m "Add Session 001: initial setup and system bootstrap notes"
git push