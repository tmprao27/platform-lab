import re
from pathlib import Path

file = Path("/Users/madhavagumbe/Downloads/patient_note.txt")
errors = []

# 1. Does the file exist?
if not file.exists():
    print("FAIL: file not found")
    exit()

# 2. Is it empty?
if file.stat().st_size == 0:
    print("FAIL: file is empty")
    exit()

# 3. Can we read it as text?
try:
    text = file.read_text(encoding="utf-8")
except UnicodeDecodeError:
    print("FAIL: file is not valid UTF-8 text")
    exit()

# 4. Are the required fields there?
for field in ["Patient ID:", "Visit Date:", "Doctor:", "Notes:"]:
    if field not in text:
        errors.append(f"Missing field: {field}")

# 5. Are the values in the right format?
if not re.search(r"Patient ID: P-\d{4}", text):
    errors.append("Patient ID format is wrong (expected P-1234)")

if not re.search(r"Visit Date: \d{4}-\d{2}-\d{2}", text):
    errors.append("Visit Date format is wrong (expected YYYY-MM-DD)")

# 6. Is the Notes section actually filled in?
notes = text.split("Notes:")[-1].strip()
if len(notes.split()) < 5:
    errors.append("Notes section is empty or too short")

# 7. Any personal data leaking? (email / UK mobile)
if re.search(r"[\w.]+@[\w.]+", text):
    errors.append("PII found: email address")
if re.search(r"07\d{9}", text):
    errors.append("PII found: phone number")

# Result
if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
else:
    print("PASS: file is valid")