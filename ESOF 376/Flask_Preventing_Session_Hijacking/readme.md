
# Preventing Session Hijacking Demo Application

This is a web-based demo application that demonstrates Prevention of Session Hijacking.

## Running the Application

### Prerequisites

1. **Python 3** installed on your system.
2. SQLite extension by alexcvzz installed in VScode.

### Setup Instructions

#### Step 1: Navigate to the Project Directory

Open a terminal and navigate to the directory where the project is located:
```bash
cd /path/to/flask_sql_inj
```

#### Step 2: Create and Activate a Virtual Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

#### Step 3: Install Dependencies

Install the required Python packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Running the Application

Run the Flask application using the following command:
```bash
python3 app.py
```

By default, the application will be accessible at `http://127.0.0.1:5000/`.

### Deactivating the Virtual Environment

When you are done using the application, deactivate the virtual environment with:
```bash
deactivate
```

## Notes

- Ensure that the `database.db` file is in the same directory as `app.py` to avoid database connection issues.
- Use the templates folder for modifying the HTML structure if required.

