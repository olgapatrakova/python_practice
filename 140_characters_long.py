headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

### Create news_ticker that is exactly 140 characters long
news_ticker = ""
i = 0
while len(news_ticker) < 140:
    news_ticker += headlines[i] + " "
    i += 1
    print(news_ticker)
    if len(news_ticker) > 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)