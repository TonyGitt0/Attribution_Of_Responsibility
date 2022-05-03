from googletrans import Translator
import os.path
from textblob import TextBlob

def transalateFile(data, data_translate):
    fileOpen = open(data, 'r')
    fileOpenWrite = open(data_translate, 'w+')

    translater = Translator()

    for line in fileOpen:
        line_to_write = translater.translate(line, "en")
        fileOpenWrite.write(str(line_to_write.text) + '\n')
    fileOpenWrite.close()

def sentimentPolarity(data_translate,data_sentiment):
    fileOpenWrite = open(data_translate, 'r')
    fileOpenSentiment = open(data_sentiment,'w+')
    total_sentiment = 0
    n_line = 0
    occurrence_kinder = 0

    for line in fileOpenWrite:
        blob = TextBlob(line)
        sentiment = blob.sentiment.polarity

        total_sentiment += sentiment
        n_line += 1

        if("Kinder" in line):
            occurrence_kinder +=1

        new_line = ("{ Comment: "+str(line).rstrip("\n")+"}  , {Sentiment: "+str(sentiment)+"}"+"  {Kinder Occurrence:  "+str(occurrence_kinder)+"}\n")
        occurrence_kinder = 0
        fileOpenSentiment.write(new_line)

    fileOpenSentiment.close()
    avarage = total_sentiment/n_line
    print("\n")
    print("Total Sentiment: "+str(total_sentiment)+"\n")
    print("Avarage Sentiment for total Comment: "+str(avarage)+"\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Traduciamo il file di Analisi iniziale
    data = './data/data.txt'
    data_translate = './data/data_translate.txt'
    data_sentiment = './data/data_sentiment.txt'
    if os.path.exists('./data/data_translate.txt'):
        print("The file <data_translate> with translation exists!!\n")
    else:
        transalateFile(data,data_translate)

    if os.path.exists('./data/data_sentiment.txt'):
        print("The file <data_sentiment> with sentiment analyses exists!!\n")
    else:
        sentimentPolarity(data_translate,data_sentiment)
