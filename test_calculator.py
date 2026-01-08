import pytest
from pywinauto import Application
import subprocess
import time


@pytest.fixture
def calc_app():
    # Kill any existing Calculator
    subprocess.run('taskkill /F /IM Calculator.exe', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Launch Calculator UWP app
    subprocess.Popen('start calculator:', shell=True)

    # Retry connecting to Calculator window
    app = Application(backend="uia")
    calc = None
    for _ in range(60):  # retry up to 30 sec
        try:
            # Connect to any window whose title contains "Calculator"
            calc = app.connect(title_re=".*Calculator.*").window(title_re=".*Calculator.*")
            if calc.exists() and calc.is_visible() and calc.is_enabled():
                break
        except Exception:
            pass
        time.sleep(0.5)
    else:
        raise RuntimeError("Calculator window did not appear in time")

    yield calc

    # Close Calculator safely
    try:
        calc.close()
    except Exception:
        pass

def test_addition(calc_app):
    calc = calc_app
    calc.child_window(auto_id="num5Button", control_type="Button").click()
    calc.child_window(auto_id="plusButton", control_type="Button").click()
    calc.child_window(auto_id="num3Button", control_type="Button").click()
    calc.child_window(auto_id="equalButton", control_type="Button").click()
    time.sleep(0.5)
    result = calc.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
    assert "8" in result

def test_subtraction(calc_app):
    calc = calc_app
    calc.child_window(auto_id="num9Button", control_type="Button").click()
    calc.child_window(auto_id="minusButton", control_type="Button").click()
    calc.child_window(auto_id="num4Button", control_type="Button").click()
    calc.child_window(auto_id="equalButton", control_type="Button").click()
    time.sleep(0.5)
    result = calc.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
    assert "5" in result
