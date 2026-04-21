from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import asyncio
import os

TOKEN = os.getenv("TOKEN")

data = {
    "geography": ["PUT_FILE_ID"],
    "history": ["PUT_FILE_ID"]
}

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text in data:
        for file_id in data[text]:
            msg = await update.message.reply_video(file_id)

            await asyncio.sleep(600)
            try:
                await msg.delete()
            except:
                pass
    else:
        await update.message.reply_text("Not found")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
