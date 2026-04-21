from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.timings import wait_until_passes
import time
import os


os.system("taskkill /F /IM Calculator.exe >nul 2>&1")
os.system("taskkill /F /IM ApplicationFrameHost.exe >nul 2>&1")

# Start Calculator
Application(backend="uia").start("calc.exe")

# Attach to Calculator
calc = wait_until_passes(
    timeout=30,
    retry_interval=1,
    func=lambda: Desktop(backend="uia").window(title_re=".*Calculator.*")
)

calc.wait("visible", timeout=30)
calc.set_focus()
time.sleep(1)

# ---- 5 + 3 ----
calc.type_keys("5+3=", with_spaces=True)
time.sleep(1)

result = calc.child_window(auto_id="CalculatorResults").window_text()
print("Addition Result:", result)

# ---- Clear ----
calc.type_keys("{ESC}")
time.sleep(1)

# ---- 9 - 4 ----
calc.type_keys("9-4=", with_spaces=True)
time.sleep(1)

result = calc.child_window(auto_id="CalculatorResults").window_text()
print("Subtraction Result:", result)

calc.close()
