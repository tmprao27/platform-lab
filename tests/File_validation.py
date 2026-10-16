#file i have to validate /Users/madhavagumbe/Downloads/patient_note.txt

# this is a doctor notes. Generally contain petaint details and note about diagnosis

# our goal is to validate 1. if the note is empty or have any data 
#if the file has any data then check if file contain , Patine id, visit date and doctors name and prescription notes
# if all this exist then you mine those details and arrange it in structured way
# before i organise i want to validate if Pateint id follows the standard for P-NNNNN , Date in YYYY-MM-DD Dcotor name as text notes - redact any PII details if exist


import re
from pathlib import Path

# access file and read the content

file=Path("/Users/madhavagumbe/Downloads/patient_note.txt")
report=[] # This is list to store all erros about this validation

# 1. Validation - Check if file exist

if file.exists():
    report.append("file status - File available")
else:
    report.append("file status - File not found")
    exit()

# 2. Check if file is empty

if file.stat().st_size==0:
    report.append("file size - File is empty")
else:
    report.append(f"File size - {file.stat().st_size} bytes")   
    
#3 . Check if file is valid UTF-8 text

try:
    text=file.read_text(encoding="utf-8")
    report.append("file encoding - valid UTF-8 text")
except UnicodeDecodeError:
    report.append("file encoding - not valid UTF-8 text")
    exit()

#4. check if required fields are present
required_fields=["Patient ID:","Visit Date:","Doctor:","Notes:"]
for field in required_fields:
    if field not in text:
        report.append(f"Missing field - {field}")
    else:
        report.append(f"Field present - {field}")

#5 Check if values are in right format
if not re.search(r"Patient ID: P-\d{4}", text):
    report.append("Patient ID format is wrong (expected P-1234)")   

if not re.search(r"Visit Date: \d{4}-\d{2}-\d{2}", text):
    report.append("Visit Date format is wrong (expected YYYY-MM-DD)")

#6. Check if Notes section is filled in
notes=text.split("Notes:")[-1].strip()
print(notes)


#print(report)    


