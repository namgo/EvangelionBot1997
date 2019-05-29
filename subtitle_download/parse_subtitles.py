import sys
import os
import pysrt
from google.cloud import firestore

try:
    sys.argv[1]
except:
    print('{} [files.srt]'.format(sys.argv[0]))
print('parsing', len(sys.argv[1:]), 'files')

output = []
for filename in sys.argv[1:]:
    tmp_output = {'filename': filename, 'subs': {}}
    srt = pysrt.open(filename, encoding='iso-8859-1')
    subs = {}
    for i in range(len(srt)):
        tmp_output['subs'].update({str(i): srt[i].text})
        
    output.append(tmp_output)

db = firestore.Client()
for o in output:
    filename = os.path.basename(o['filename'])
    doc_ref = db.collection(u'subtitles').document(filename)
    doc_ref.set(o['subs'])
