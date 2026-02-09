# Playwright Automation Testing Sample Project

This repository contains a sample automation testing framework built using Python and Playwright, demonstrating how to automate API testing, web UI testing, and data generation scripting.


## Project Overview

The framework showcases automation testing implementation using Playwright with Python, covering the following areas:

1. **API Automation**: Automated API test scenarios using a public demo REST API  
   ([Reqres](https://reqres.in/))

2. **Website Test Automation**: UI automation tests covering both positive and negative scenarios on a demo web application  
   ([Sauce Demo](https://www.saucedemo.com/))

3. **Data Generation Script**: A script that fetches user data from an API and exports it into a CSV file using custom formatting logic.

---


## Tech Stack & Prerequisites

- **Language**: Python 3.8+
- **Web Automation**: Playwright
- **API Interaction**: Requests
- **Reporting**: Allure Report
- **Test Runner**: Pytest

### ⚠️ Important: Allure Report Requirement

> **Disclaimer:** To generate and view the actual HTML visualization report, you must have **Java (JDK 8+)** and the **Allure Commandline** tool installed on your system.
>
> - **Windows:** `scoop install allure` (or download binary manually)
> - **Mac:** `brew install allure`
> - **Linux:** `sudo apt-get install allure`

---

## Setup & Installation

Follow these steps to set up the environment:

### 1. Clone the repository

Open your terminal in the project directory

### 2. Create Virtual Environment (Recommended)

Isolate dependencies by creating a virtual environment:

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Mac / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages (`requests`, `playwright`, `pytest`):

```bash
pip install requests playwright pytest pytest-html

```

### 4. Install Playwright Browsers

Download the necessary browser binaries (Chromium, Firefox, Webkit):

```bash
playwright install

```

---

## How to Run

### 1. Run Automation Tests (API & UI)

To execute the full test suite:

```bash
pytest"

```

**Run specific modes:**

- **Run with visual browser (Headed mode):**

```bash
cd ..folder
pytest test_01_status.py

```

### 2. Run Data Generation Script

To generate the CSV file from the API:

```bash
cd ..convert06
python additional.py

```

- **Output:** A file named `response.csv` will be created in the root folder.

- **Note:** The CSV file is created using a custom manual string-based formatting approach for demonstration purposes.

---

## Project Structure

```text
/techtest04-01
├── __pycache__/
├── .pytest_cache/
├── allure-results/
├── api/                   # API automation test suite
│   ├── test_01_status.py
│   └── test_02_latency.py
│   ├── test_03_schema.py
│   └── test_04_dataval.py
│   ├── test_05_format.py
│
├── conver06/              # Additional test
│   ├── additional.py      # Main script for Data Generation (CSV)
│
├── website/               # Website automation test suite
│   ├── test_negative.py   # 5 negative scenario
│   └── test_positive.py   # 5 positive scenario
│   └── test_positive.py   # 5 positive scenario
│
├── README.md              # Documentation
├── requirements.txt       # Python dependencies

```

---

