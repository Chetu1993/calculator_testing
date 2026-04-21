import pytest

from pywinauto.application import Application
from pywinauto.timings import wait_until_passes
from pywinauto import Desktop
import time
import os


@pytest.fixture(scope="module")
def calc_app():
    os.system('taskkill /F /IM Calculator.exe > nul 2>&1')
    os.system('taskkill /F /IM ApplicationFrameHost.exe >nul 2>&1')
    Application(backend='uia').start('calc.exe')
    calc=wait_until_passes(timeout=30,retry_interval=1,func=lambda: Desktop(backend='uia').window(title_re='.*Calculator.*'))
    calc.wait("visible",timeout=30)
    calc.set_focus()
    yield calc
    calc.close()

@pytest.mark.sanity
def test_addition(calc_app):
    calc=calc_app
    calc.child_window(auto_id="num5Button", control_type="Button").click()
    calc.child_window(auto_id="plusButton", control_type="Button").click()
    calc.child_window(auto_id="num3Button", control_type="Button").click()
    calc.child_window(auto_id="equalButton", control_type="Button").click()
    time.sleep(0.5)
    result = calc.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
    assert "8" in result

@pytest.mark.sanity1
def test_substraction(calc_app):
    calc=calc_app
    calc.child_window(auto_id='num9Button',control_type='Button').click()
    calc.child_window(auto_id='minusButton',control_type='Button').click()
    calc.child_window(auto_id='num5Button',control_type='Button').click()
    calc.child_window(auto_id='equalButton',control_type='Button').click()
    time.sleep(0.5)
    result=calc.child_window(auto_id='CalculatorResults',control_type='Text').window_text()
    assert '4' in result
