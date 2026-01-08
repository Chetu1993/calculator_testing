
# Calculator Automation Testing

This project automates basic **Windows Calculator** operations such as **addition and subtraction** and generates test reports using **PyTest + Allure**.

---

## 📂 Project Structure

```text
calculator_testing/
│
├── calculator_app.py          # Standalone automation script
├── test_calculator.py         # Pytest-based automation tests
├── allure-results/            # Generated during pytest execution
├── allure-report/             # Generated Allure HTML report
└── README.md


---

## 🛠️ Technologies Used

- Python 3.x
- Pywinauto (Windows Desktop Automation)
- Pytest (Test Framework)
- Allure (Test Reporting)
- Windows Calculator (UWP Application)

---

## ⚙️ Prerequisites

- Windows Operating System
- Python installed and added to PATH
- Allure Commandline installed
- Virtual environment (recommended)

---

## 📦 Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
````

Install required dependencies:

```bash
pip install pywinauto pytest allure-pytest
```

Verify Allure installation:

```bash
allure --version
```

---

## ▶️ Standalone Calculator Automation

**File:** `calculator_app.py`

### Script Functionality

* Launches Windows Calculator
* Waits until the Calculator window is ready
* Prints all UI control identifiers (for debugging)
* Performs:

  * Addition: `5 + 3`
  * Subtraction: `9 - 4`
* Prints results in the console
* Closes the Calculator application

### Run the Script

```bash
python calculator_app.py
```

### Sample Output

```
Addition Result: Display is 8
Subtraction Result: Display is 5
```

---

## 🧪 Pytest Automation (Test Cases)

**File:** `test_calculator.py`

### Test Scenarios Covered

* ✅ Verify addition operation: `5 + 3 = 8`
* ✅ Verify subtraction operation: `9 - 4 = 5`

### Key Implementation Details

* Uses **pytest fixtures** to manage Calculator lifecycle
* Kills any existing Calculator instances before execution
* Launches Calculator using UWP protocol
* Connects using **UI Automation (UIA)** backend
* Uses **Automation IDs (`auto_id`)** for stable element identification
* Validates results using assertions

### Run Tests

```bash
pytest test_calculator.py -v -s
```

---

## 📊 Allure Report Generation

### Step 1: Run pytest with Allure results enabled

```bash
pytest test_calculator.py -v -s --alluredir=allure-results
```

### Step 2: Generate and open Allure report

```bash
allure serve allure-results
```

### Allure Report Features

* Test execution summary
* Passed/failed test cases
* Execution time
* Assertion details
* Clean and interactive HTML dashboard

---

## 📌 Important Notes

* Automation uses **UI Automation (UIA)** backend
* Windows Calculator is a **UWP application**
* Automation IDs (`auto_id`) are more reliable than titles
* UI language or OS version changes may affect element locators

---


## 🚀 Future Enhancements

* Add multiplication and division test cases
* Capture screenshots on test failure
* Integrate with CI/CD pipelines (GitHub Actions / Jenkins)
* Convert into a reusable Windows automation framework

---

## 👤 Author

**Chetan Kumar**
Python | Windows Automation | Pytest | Allure



