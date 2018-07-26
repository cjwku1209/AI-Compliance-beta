import AMLKYC2_Sentiment_mod as s

Test_News =open("short_reviews/Test.txt","r").read() 

#Read testing articles from file.
i = 1
for p in Test_News.split('/////'):
    print(i, "  ", s.sentiment(p))
    i = i + 1

#Read testing articles from quotes.
i = 10
print(i, "  ", s.sentiment("This movie was so great and awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
i = i + 1

print(i, "  ",s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
i = i + 1

print(i, "  ",s.sentiment("據歐洲新聞網（Euronews）報導，空中巴士集團（Airbus）於當地時間19日、在法國土魯斯（Toulouse）基地，讓旗下最新型號貨機「超級大白鯨」（Beluga XL）進行首度試飛。這款新型貨機，在經過10多個月嚴格測試後，以可愛、由於大白鯨的外貌飛上天空，不僅成功完成起降任務，也讓地面上萬名粉絲興奮不已。"))
i = i + 1

print(i, "  ",s.sentiment("06/23/2000, The Federal Reserve Board today announced the execution of a Written Agreement by and among Banco Bilbao Vizcaya Argentaria, S.A., Madrid, Spain; Banco Bilbao Vizcaya, S.A. Miami Agency, Miami, Florida; Banco Bilbao Vizcaya, S.A. New York Branch, New York, New York; the Federal Reserve Bank of Atlanta; the Federal Reserve Bank of New York; the New York State Banking Department; and the State of Florida Department of Banking and Finance. DOCKET NUMBER: 00-010-WA/RB-FA DOCKET NUMBER: 00-010-WA/RB-FB DOCKET NUMBER: 00-010-WA/RB/FBR"))
i = i + 1

print(i, "  ",s.sentiment("Federal Reserve Board issues termination of enforcement actions with Community Banks of Georgia, Inc., and Grand Mountain Bancshares, Inc."))
i = i + 1

print(i, "  ",s.sentiment("Federal Reserve Board issues enforcement action with United Bank Limited and former employee of Hinsdale Bank & Trust and announces termination of enforcement action with United Bank Limited"))
i = i + 1

print(i, "  ",s.sentiment("Kotwali police arrested two professional drug traffickers Dulal Mian, and Abdul Halim and seized 800 gram smuggled ganja from their possession last night."))
i = i + 1

print(i, "  ",s.sentiment("The State Bureau of Investigation for Economic Offences has submitted a challan against Ashok Kumar Jain in connection with an old '1.83 crore fraud and embezzlement case"))
i = i + 1                  

print(i, "  ",s.sentiment("Fariduddin Ahmed Chowdhury was also accused in the police officer murder case."))
i = i + 1

print(i, "  ",s.sentiment("The Asian Development Bank (ADB) declares firms and individuals ineligible to participate in ADB-financed activity for committing fraudulent or corrupt acts as defined by ADB's Anticorruption Policy. The entity in this record appears on the ADB's sanctioned/debarred entities list. ~~ Grounds: Sanction violation."))
i = i + 1

print(i, "  ",s.sentiment("Zaki found Ismail Ibrahim was sentenced to death for trafficking in 20.052kg of cannabis."))
i = i + 1

print(i, "  ",s.sentiment("A case has been registered by the Lokayukta Special Police Establishment against him in a corruption case.Jhabua Collector and the nagar panchayat CEO had got publicity material printed from a private printer instead of a government printer."))
i = i + 1

print(i, "  ",s.sentiment("Amy Zhang of Alger and Sandy Villere of Villere & Co. are portfolio managers invested in small-cap stocks that have outperformed their peers. The Alger Small Cap Focus Fund Class A (AOFAX) has returned nearly 31 percent to investors and ranks in the first percentile of the “small growth” category, according to data from Morningstar. Meanwhile, the Villere Balanced Fund (VILLX) has posted a return of 12.9 percent this year and ranks in the first percentile among balanced funds with 70-to-85 percent equity allocation."))
i = i + 1

print(i, "  ",s.sentiment("However, not many people think of investing in the smaller stocks since they are not as popular and are not talked about nearly as much as the larger companies. Small caps also tend to be more volatile than large-cap stocks given their size. CNBC talked to Zhang and Villere about how they pick stocks and their investment process."))
i = i + 1

print(i, "  ",s.sentiment("the performances are an absolute joy . "))
i = i + 1

print(i, "  ",s.sentiment("a quasi-documentary by french filmmaker karim dridi that celebrates the hardy spirit of cuban music .")) 
i = i + 1

print(i, "  ",s.sentiment("grant carries the day with impeccable comic timing , raffish charm and piercing intellect .")) 
i = i + 1

print(i, "  ",s.sentiment("a sensitive and astute first feature by anne-sophie birot . "))
i = i + 1

print(i, "  ",s.sentiment("both exuberantly romantic and serenely melancholy , what time is it there ? may prove to be [tsai's] masterpiece . "))
i = i + 1

print(i, "  ",s.sentiment("mazel tov to a film about a family's joyous life acting on the yiddish stage . "))
i = i + 1

print(i, "  ",s.sentiment("standing in the shadows of motown is the best kind of documentary , one that makes a depleted yesterday feel very much like a brand-new tomorrow . "))
i = i + 1

print(i, "  ",s.sentiment("it's nice to see piscopo again after all these years , and chaykin and headly are priceless .")) 
i = i + 1

print(i, "  ",s.sentiment("provides a porthole into that noble , trembling incoherence that defines us all . "))
i = i + 1


print(i, "  ",s.sentiment("The Shanghai factory is to produce up to 500,000 vehicles a year, a significant scale for an auto plant, and Musk's appearance was a win for China, now locked in a fierce trade war with the U.S., home of Tesla."))
i = i + 1

print(i, "  ",s.sentiment("The city of Shanghai is seen in a good light these days, having been at the forefront of China's policy of opening up to the outside world. But the commercial hub is now in the political spotlight for a separate reason."))
i = i + 1

print(i, "  ",s.sentiment("In the spring of 2023, China's No. 2, Premier Li Keqiang, 63, will most certainly step down. With President Xi Jinping and Vice President Wang Qishan now in office for indefinite terms, the fight to replace Li will be the most contested political battle for years to come."))

