import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("ERRO CRÍTICO: TELEGRAM_TOKEN não configurado!")

TETO_GASTOS = {
    "Roma (4 dias)": {"moeda": "EUR", "valor": 60, "brl": 360},
    "Veneza (2 dias)": {"moeda": "EUR", "valor": 60, "brl": 360},
    "Praga (2 dias)": {"moeda": "CZK", "valor": 1150, "brl": 270},
    "Viena (2 dias)": {"moeda": "EUR", "valor": 60, "brl": 360},
    "Copenhague (4 dias)": {"moeda": "DKK", "valor": 560, "brl": 450}
}
