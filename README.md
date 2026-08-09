# SDET Automation Framework

[![CI](https://github.com/truptimahajan01/sdet_automation_framework/actions/workflows/test.yml/badge.svg)](https://github.com/truptimahajan01/sdet_automation_framework/actions)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)](https://selenium.dev)
[![pytest](https://img.shields.io/badge/pytest-8.x-orange.svg)](https://pytest.org)

A personal learning project demonstrating Python-based test automation skills.

UI tests run against [SauceDemo](https://www.saucedemo.com) and API tests run against [JSONPlaceholder](https://jsonplaceholder.typicode.com).

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| Selenium 4.x + WebDriver Manager | UI automation |
| pytest | Test runner |
| pytest-html + Allure | Reporting |
| Pydantic | API response validation |
| jsonschema | JSON schema validation |
| httpx | Async API testing |
| PyYAML | Environment configuration |
| Docker + Docker Compose | Containerised execution |
| GitHub Actions | CI/CD |

---

## 📁 Project Structure

```
sdet_automation_framework/
├── .github/workflows/      # CI/CD pipeline
├── api/
│   ├── base_api.py         # Centralised HTTP client (GET, POST, PUT, DELETE)
│   └── models/             # Pydantic response models
├── config/
│   ├── config.yaml         # Environment URLs and settings
│   └── config_loader.py    # Reads active environment via TEST_ENV
├── pages/
│   ├── base_page.py        # BasePage with Selenium WebDriverWait helpers
│   ├── login_page.py       # Login Page Object (SauceDemo)
│   └── dashboard_page.py   # Dashboard Page Object (SauceDemo)
├── tests/
│   ├── conftest.py         # Fixtures: browser, api_client, screenshot hook
│   ├── test_login.py       # UI tests — login flow
│   ├── test_dashboard.py   # UI tests — dashboard/inventory
│   ├── test_api.py         # API tests with schema validation
│   ├── test_api_advanced.py# API tests with Pydantic validation
│   ├── test_api_async.py   # Async API tests using httpx
│   └── test_api_auth.py    # Auth header fixture tests
├── utils/
│   ├── logger.py           # Dual-handler logger (console + file)
│   └── data_reader.py      # CSV test data reader
├── test_data/
│   └── data.csv            # Test credentials
├── reports/                # Auto-generated reports (gitignored)
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
└── requirements.txt
```

---

## ✅ Features

- **Page Object Model (POM)** — Clean separation between page logic and test logic
- **API Testing** — Schema validation (jsonschema) + type validation (Pydantic)
- **Async API Testing** — Using `httpx.AsyncClient`
- **Allure + HTML Reporting** — Rich test reports with screenshots on failure
- **Screenshot on Failure** — Auto-captured and attached to Allure report
- **Multi-environment Config** — Switch environments via `TEST_ENV` env var
- **Docker support** — Run tests in an isolated container
- **GitHub Actions CI/CD** — Triggers on push and pull request
- **Parallel execution** — `pytest-xdist` support
- **Data-driven testing** — CSV reader + `pytest.mark.parametrize`
- **Structured logging** — Console + file logging with timestamps

---

## 🚀 Setup & Running Tests

### Prerequisites
- Python 3.11+
- Google Chrome (latest)
- Java 11+ (for Allure CLI — optional)

### Install

```bash
git clone https://github.com/truptimahajan01/sdet_automation_framework.git
cd sdet_automation_framework

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### Run Tests

```bash
# All tests
pytest

# API tests only
pytest -m api

# UI tests only
pytest -m ui

# Smoke tests only
pytest -m smoke

# Parallel (4 workers)
pytest -n 4

# With Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

### Switch Environment

```bash
# Run against staging (default)
pytest -m api

# Run against prod
TEST_ENV=prod pytest -m api
```

---

## 🐳 Docker

```bash
# Build and run (API tests)
docker compose up --build

# Stop
docker compose down

# View logs
docker compose logs
```

---

## 📊 Test Markers

| Marker | Description |
|---|---|
| `smoke` | Quick sanity checks run on every deployment |
| `regression` | Full regression suite |
| `api` | API-only tests (no browser needed) |
| `ui` | Browser-based Selenium tests |

---

## ⚙️ Environment Configuration

Set the active environment using the `TEST_ENV` environment variable.
Configuration is loaded from `config/config.yaml`.

```bash
export TEST_ENV=staging   # Linux/macOS
set TEST_ENV=staging      # Windows
```

> ⚠️ Never commit real credentials. Copy `.env.example` to `.env` and fill in values locally.
