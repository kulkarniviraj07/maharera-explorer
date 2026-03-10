# MahaRERA Project Explorer

A Flask web app that reads your Excel + JSON files live and serves them via a login-protected website.

---

## Folder Structure

```
maharera_server/
├── server.py           ← the server (don't edit)
├── config.py           ← YOUR settings go here
├── requirements.txt    ← dependencies
├── static/
│   └── index.html      ← the website (don't edit)
└── data/               ← put your files here
    ├── maharera_final_clean.xlsx
    └── graphs/
        ├── project_1.json
        ├── project_2.json
        └── ...
```

---

## Setup (One Time)

### Step 1 — Install Python
Make sure Python 3.8+ is installed.
Check by running: `python --version`

### Step 2 — Install dependencies
Open a terminal in this folder and run:
```
pip install -r requirements.txt
```

### Step 3 — Put your data files in place
Copy your Excel file and graphs folder into the `data/` folder:
```
data/maharera_final_clean.xlsx
data/graphs/project_1.json
data/graphs/project_2.json
...
```

Or if your files are somewhere else on your computer, open `config.py`
and set the full path:
```python
EXCEL_PATH = "C:/Users/YourName/Documents/maharera_final_clean.xlsx"
GRAPHS_DIR = "C:/Users/YourName/Documents/graphs"
```

### Step 4 — Set your login (optional)
Open `config.py` and change the username/password:
```python
LOGIN_ID       = "admin"
LOGIN_PASSWORD = "maharera2025"
```

---

## Running the Server

```
python server.py
```

Then open your browser and go to:
**http://localhost:5000**

---

## When Data Updates

- **Excel updated?** Just save the file. The next time someone clicks a project, the server reads the latest version automatically. No restart needed.
- **New graph JSONs?** Drop them in the `graphs/` folder. They'll appear instantly.
- **New projects added to Excel?** Refresh the browser — the dropdown updates automatically.

---

## Hosting on a Network (so others can access it)

If you want others on your local network to access it, run:
```
python server.py --host 0.0.0.0
```
Then they can visit: `http://YOUR_IP_ADDRESS:5000`

For internet hosting, look into deploying Flask on:
- **PythonAnywhere** (free, easy)
- **Railway** (free tier available)
- **Render** (free tier available)
