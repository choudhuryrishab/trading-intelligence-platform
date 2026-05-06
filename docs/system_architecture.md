📊 Trading Intelligence Platform — System Architecture
🎯 Purpose

A personal trading intelligence system that aggregates portfolio data from Trading212, calculates financial indicators (RSI, valuation metrics), and presents insights through a dashboard accessible from anywhere.

🧠 High-Level Architecture
Trading212 API
      │
      ▼
Backend Data Layer (Python)
- API client
- Data fetcher
- Scheduler
      │
      ▼
Analytics Engine
- RSI calculation
- Moving averages
- Portfolio metrics
- Risk scoring
      │
      ▼
Database Layer
- Portfolio snapshots
- Historical prices
- Indicators storage
      │
      ▼
API Layer (FastAPI)
- /portfolio
- /indicators
- /summary
      │
      ▼
Frontend Dashboard (Streamlit / Web UI)
- Portfolio view
- Charts
- Alerts
      │
      ▼
Access Anywhere (Laptop / Phone Browser)
🔐 Security Model
Trading212 API token stored in .env
Never committed to GitHub
Backend reads env variables only
Optional future encryption layer
📦 Project Modules
backend/

Handles all logic

app/api/ → API routes
app/services/ → Trading, analytics
app/models/ → data structures
app/core/ → config + utilities
frontend/

User interface

Streamlit dashboard (initial)
Future: React dashboard
data/
cached API responses
historical snapshots
local development datasets
docker/
containerized backend + frontend
future deployment-ready setup
🚀 Future Expansion
Phase 2: Intelligence Layer
LLM portfolio assistant
"Why did my portfolio drop today?"
risk explanations
Phase 3: External Data
news sentiment analysis
macro indicators
earnings data
Phase 4: Automation (optional future)
trade suggestions
alerts
signal generation
📱 Design Principle

Desktop-first analytics, mobile-readable insights, cloud-accessible system.