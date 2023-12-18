import logging
import torch
import tkinter as tk
from tkinter import messagebox
import seaborn as sns
import matplotlib.pyplot as plt
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

thod)
try:
    BOT_TOKEN = "YO"  
except Exception as ex:
    logger.info(ex)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I\'m an echobot!')

def echo(update: Update, context: CallbackContext) -> None:
  
    update.message.reply_text(update.message.text)

    
    torch_tensor = torch.tensor([1, 2, 3, 4, 5])
    logger.info("PyTorch Tensor Example: {}".format(torch_tensor_example))

   
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Telegram Bot", "Message received: {}".format(update.message.text))

    # Seaborn Visualization Example
    sns.set_theme()
    data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
    df = sns.load_dataset("iris")
    sns.scatterplot(x='sepal_length', y='sepal_width', data=df)
    plt.title('Seaborn Scatter Plot e')
    plt.show()

def main() -> None:
    
    updater = Updater(BOT_TOKEN)

  
    dp = updater.dispatcher

  
    dp.add_handler(CommandHandler("start", start))

 
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
