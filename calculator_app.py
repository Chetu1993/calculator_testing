from pywinauto.application import Application
import time

# Launch Calculator
app = Application(backend="uia").start("calc.exe")
calc = app.window(title_re=".*Calculator.*")
calc.wait('exists ready visible', timeout=15)

# Debug: print all controls
calc.print_control_identifiers()

# Perform addition: 5 + 3
calc.child_window(title="5", control_type="Button").click()
calc.child_window(title="Plus", control_type="Button").click()
calc.child_window(title="3", control_type="Button").click()
calc.child_window(title="Equals", control_type="Button").click()

result = calc.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
print("Addition Result:", result)

# Perform subtraction: 9 - 4
calc.child_window(title="9", control_type="Button").click()
calc.child_window(title="Minus", control_type="Button").click()
calc.child_window(title="4", control_type="Button").click()
calc.child_window(title="Equals", control_type="Button").click()

result = calc.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
print("Subtraction Result:", result)

# Close Calculator
calc.close()
