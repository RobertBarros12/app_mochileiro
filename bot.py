import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TOKEN, TETO_GASTOS

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "✈️ *Mochileiro Raiz & Auditor Financeiro v1.0*\n\n"
        "📊 *Comandos Disponíveis:*\n"
        "/auditoria - Status de sobrevivência e documentos.\n"
        "/tetogastos - Limites diários estritos por país.\n"
        "/bagagem - Manual de sobrevivência de cabine."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def teto_comando(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "💰 *MATRIZ DE CONVERSÃO E TETOS DIÁRIOS*\n\n"
    for local, dados in TETO_GASTOS.items():
        text += f"📍 *{local}:* {dados['valor']} {dados['moeda']} (~R$ {dados['brl']}/dia)\n"
    await update.message.reply_text(text, parse_mode="Markdown")

async def bagagem_comando(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "🎒 *LOGÍSTICA DE BAGAGEM ULTRA LOW-COST*\n\n"
        "⚠️ *Dimensões Máximas:* 40x20x25 cm (Apenas mochila de bordo).\n"
        "❌ Proibido malas de rodinha ou despacho."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tetogastos", teto_comando))
    application.add_handler(CommandHandler("bagagem", bagagem_comando))
    application.run_polling()

if __name__ == "__main__":
    main()
