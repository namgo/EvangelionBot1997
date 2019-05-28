from google.cloud import firestore
import sys

try:
    sys.argv[2]
except:
    print('{} [titles.lst] [title type]'.format(sys.argv[0]))

with open(sys.argv[1], 'r') as f:
    titles_list = f.readlines()
    titles = {}
    for i in range(len(titles_list)):
        titles[str(i)] = titles_list[i].strip('\n')


db = firestore.Client()
doc_ref = db.collection(u'titles').document(sys.argv[2])
doc_ref.set(titles)
