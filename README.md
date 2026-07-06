# Playwright Python QA Portfolio

A test automation framework built with **Playwright** and **Python**, demonstrating UI, API, and end-to-end testing skills using industry-standard patterns like the Page Object Model (POM) and CI/CD integration.

## 🛠️ Tech Stack
- **Python 3.11**
- **Playwright** (sync API)
- **Pytest** + `pytest-html` for reporting
- **GitHub Actions** for CI

## 📁 Project Structure

## 🚀 Getting Started

```bash
git clone https://github.com/Aviral-QA/playwright-python-qa-portfolio.git
cd playwright-python-qa-portfolio
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## ▶️ Running Tests

```bash
pytest
```

HTML report generated at `reports/report.html`.

## ✅ CI/CD
Every push to `main` automatically runs the full test suite via GitHub Actions.
[![Playwright Tests](https://github.com/Aviral-QA/playwright-python-qa-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/Aviral-QA/playwright-python-qa-portfolio/actions)

## 📌 What This Project Demonstrates
- Page Object Model design pattern
- Reusable Pytest fixtures
- Data-driven and parameterized testing
- Automated CI pipeline with test reporting
- Clean, maintainable test architecture

## 📄 License
MIT