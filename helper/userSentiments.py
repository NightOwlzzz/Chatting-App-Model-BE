import string
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('vader_lexicon')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def textPreprocess(text):
    #Lower case text
    lower_text=text.lower()
    # print(lower_text)

    #Remove punctuations
    clean_text=lower_text.translate(str.maketrans('', '', string.punctuation))
    # print(clean_text)

    #Tokenizing word
    tokenized_words=word_tokenize(clean_text,"english")
    # print(tokenized_words)

    #Removing stopwords
    final_words=[word for word in tokenized_words if word not in stopwords.words("english")]
    # print(final_words)

    #Lemmatization : From plural to singular form + Base form of verb (eg. better -> good)
    lemma_words=[]
    for word in final_words:
        word=WordNetLemmatizer().lemmatize(word)
        lemma_words.append(word)
    return lemma_words

def getEmotions(lemma_words):
    emotion_list={}
    with open('emotion.txt','r') as file:
        for line in file:
            clean_line=line.replace("\n","").replace("'","").replace(",","").strip()
            word,emotion=clean_line.split(":")

            if word in lemma_words:
                if emotion not in emotion_list:
                    emotion_list[emotion]=1
                else:
                    emotion_list[emotion]+=1
    total=sum(emotion_list.values())
    for key in emotion_list.keys():
        emotion_list[key]=round((emotion_list[key]*100)/total,2)
    # print(emotion_list)
    return emotion_list

def getEmotionsList(text):
    emotions = getEmotions(textPreprocess(text))
    return emotions
