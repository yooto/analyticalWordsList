import pandas as pd
import datetime as dt

wordsTable = pd.read_csv("wordsTable.csv")
print(wordsTable)
words = input("英単語を入力").split()
group = input("グループを入力")
for i, word  in enumerate(words):
    wordsTable = wordsTable.append(pd.DataFrame({'idnumber':len(wordsTable) ,'group':group, 'word':[word], 'date':[dt.datetime.now()]}))

print(wordsTable)
wordsTable.to_csv("wordsTable.csv", index = False)
