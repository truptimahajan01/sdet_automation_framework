# SDET Automation Framework

A scalable, maintainable test automation framework built with Python, Selenium, and pytest.
Follows Page Object Model (POM) architecture with clear separation of concerns.

## Tech Stack
- **Language:** Python 3.11
- **UI Automation:** Selenium 4.x (with WebDriver Manager)
- **Test Runner:** pytest
- **Reporting:** pytest-html / Allure
- **CI/CD:** GitHub Actions (coming soon)

## Project Structure
```
sdet-automation-framework/
├── tests/          # Test cases organised by feature
├── pages/          # Page Object Model classes
├── utils/          # Reusable helpers (data readers, wait helpers, API client)
├── config/         # Environment configs (YAML)
├── reports/        # Auto-generated test reports (gitignored)
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup
```bash
# Clone the repository
git clone https://github.com/truptimahajan01/sdet_automation_framework.git
cd sdet-automation-framework

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Tests
```bash
# Run full suite
pytest

# Run smoke tests only
pytest -m smoke

# Run in parallel (4 workers)
pytest -n 4

# Run with Allure reporting
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Environment Configuration
Set the active environment in `config/config.yaml`.
Never commit `.env` files — copy `.env.example` and fill in secrets locally.

## Contributing
See `CONTRIBUTING.md` for branching strategy and PR guidelines.