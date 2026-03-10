import os

BASE_DIR = os.path.dirname(__file__)

EXCEL_PATH = os.path.join(BASE_DIR, "data", "maharera_final_clean.xlsx")
GRAPHS_DIR = os.path.join(BASE_DIR, "data", "graphs")

PORT = int(os.environ.get("PORT", 5000))

SECRET_KEY = "SERTyhu7654EDFGhbhY^%$5678ijHBVCDEr"