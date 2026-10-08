# Employee Data Logger

A small Streamlit app for entering employee details, viewing the collected records in a pandas DataFrame, and downloading all records as a CSV file.

## Features

- Collects an employee's name, age, and city.
- Displays submitted employee records in a table.
- Downloads all records collected in the current Streamlit session as `employee_data.csv`.
- Offers Delhi, Gurgaon, and Noida as city choices.

## Requirements

- Python
- Streamlit
- pandas

Install the Python packages with:

```powershell
python -m pip install streamlit pandas
```

## Run the app

From PowerShell, change to this folder and start Streamlit:

```powershell
Set-Location "C:\Users\arjun\Documents\Lang_chain\Data logging"
python -m streamlit run logger.py
```

If `python` points to a different environment than the one where the packages are installed, use that environment's Python executable in both commands.

## Use

1. Enter the employee's name.
2. Select an age and city.
3. Click **Add employee**.
4. Repeat to add more employees.
5. Click **Download all employee data** to download the complete table as a CSV.

Employee records are kept in Streamlit session state; they are not saved permanently to a database or file by the app.

## Current source status

The current `logger.py` contains Python syntax errors, including missing quotation marks and colons. Correct those before running the app; otherwise Streamlit will report a syntax error.
