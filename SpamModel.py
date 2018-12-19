import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer as Count
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump, load

import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('spam.csv', encoding = "ISO-8859-1")

one_encoder = LabelEncoder()

text = df.iloc[:,1]
labels = df.iloc[:,0]

vectorizer = Count()
model = LogisticRegression()

X = vectorizer.fit_transform(text)
y = one_encoder.fit_transform(labels)

X_train, X_test , y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=40)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('train score:',model.score(X_train, y_train))
print('test score:',model.score(X_test, y_test))


# visualize the data
def visualize(label):
  words = ''
  for msg in df[df['v1'] == label]['v2']:
    msg = msg.lower()
    words += msg + ' '
  wordcloud = WordCloud(width=1024, height=840).generate(words)
  plt.imshow(wordcloud)
  plt.axis('off')
  plt.show()

#visualize('spam')
#visualize('ham')

#dump(model, 'spammodel.joblib')
#dump(vectorizer, 'vectorizer.joblib')