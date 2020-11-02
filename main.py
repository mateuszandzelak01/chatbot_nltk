import spacy
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pandas as pd

data = pd.read_csv('base/tekst.txt', encoding='windows-1250')

bot = ChatBot('Friend') #create the bot
trainer = ListTrainer(bot)

BotMemory = open('base/tekst.txt', 'r').readlines()
trainer.train(BotMemory)

app = Flask(__name__)

@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']

	bot_response=bot.get_response(user_input)
	bot_response=str(bot_response)
	print("Friend: "+bot_response)
	return render_template('index.html',user_input=user_input,
		bot_response=bot_response
		)


if __name__=='__main__':
	app.run(debug=True,port=5002)