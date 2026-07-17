# Playwright Automation Practice

## Overview

This repository contains automation testing practice projects built using **Playwright**, **Python**, and **Pytest**.

The project demonstrates different automation concepts such as table handling, filtering, window handling, assertions, and reporting.

---

## Tech Stack

- Python
- Playwright
- Pytest

---

## Project Structure

```text
playwright_demo_project/
│
├── assets/
├── tests/
│   ├── conftest.py
│   ├── test_first.py
│   ├── test_search.py
│   ├── test_table.py
│   └── test_window_handling.py
│
├── pytest.ini
├── .gitignore
└── README.md
```

---

## Test Scenarios Implemented

- Open Practice Test Table
- Verify page title
- Verify table rows
- Search course by name
- Language Filter
- Level Filter
- Window Handling
- Assertions
- HTML Report Generation
- Video Recording

---

## Run Tests

```bash
pytest
```

---

## Run Specific Test

```bash
pytest tests/test_table.py
```

---

## Generate HTML Report

```bash
pytest --html=report.html --self-contained-html
```

---

## Record Video

```bash
pytest tests/test_table.py --video=on
```

---

## Author

**Daneshwari Kabade**

Learning Playwright Automation using Python and Pytest.