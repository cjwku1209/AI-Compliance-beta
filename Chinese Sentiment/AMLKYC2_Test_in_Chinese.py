import AMLKYC2_Sentiment_mod_in_Chinese as s

Test_News =open("Database/Test.txt","r", encoding="utf-8").read() 

#Read testing articles from file.
i = 1
for p in Test_News.split('/////'):
    print(i, "  ", s.sentiment(p))
    i = i + 1
