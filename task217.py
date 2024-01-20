from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text)

    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


sample_text = ''' 
As of my last update in January 2022, the Indian economy is a diverse and rapidly growing one. It encompasses agriculture, 
manufacturing, and a robust services sector, with a particular focus on IT services. The nation's large and youthful population
provides both opportunities and challenges. India has undertaken economic reforms to encourage liberalization, privatization, and
globalization, aiming to attract foreign investment and foster growth. However, income and wealth inequality persist as significant issues. 
The country faces challenges in inclusive growth, infrastructure development, and addressing bureaucratic hurdles.
 '''


generate_word_cloud(sample_text)
