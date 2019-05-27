from xmlrpc import client
import gzip
import base64
import json
import logging
import sys
import glob
import time
import os
debug = True

def chunk(l, n):
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

def process(token, server, subs):
    for s in chunk(subs, 19):
        while True:
            try:
                download = server.DownloadSubtitles(token, s)
                print(download)
                for d in download['data']:
                    with open('subs/{}'.format(d['idsubtitlefile']), 'wb') as f:
                        f.write(gzip.decompress(base64.b64decode(d['data'])))
                print('wrote', d['idsubtitlefile'])
            except Exception as e:
                logging.error(e)
                time.sleep(4)
                continue
            break

def get_all_seasons(token, server, show_name, seasons, episodes):
    subs = []
    for season in seasons:
        for episode in episodes:
            while True:
                try:
                    search_list = [
                        {
                            'query': show_name, 'season': season, 'episode': episode,
                            'sublanguageid': 'en'
                        }
                    ]
                    output = server.SearchSubtitles(token, search_list)
                    for d in output['data']:
                        if d['LanguageName'] == 'English':
                            if sys.argv[3].lower() in d['MovieReleaseName'].lower():
                                subs.append(d['IDSubtitleFile'])
                    print(season, episode, len(output['data']))
                except KeyboardInterrupt:
                    process(token, server, subs)
                except Exception as e:
                    try:
                        if debug:
                            logging.error(e)
                        time.sleep(4)
                        continue
                    except KeyboardInterrupt:
                        process(token, server, subs)
                
                break
    process(subs)
        
try:
    sys.argv[5]
except:
    print('{} [username] [password] [show name] [seasonstart]-[seasonend] [episodestart]-[episodeend]'.format(sys.argv[0]))
server = client.Server('http://api.opensubtitles.org/xml-rpc')
try:
    with open('token', 'r') as f:
        token = f.read()
except:
    token = server.LogIn(sys.argv[1], sys.argv[2], 'en', 'TemporaryUserAgent')['token']
    with open('token', 'w') as f:
        f.write(token)

print('hit Ctrl-c when you don\' see any more subtitles being grabbed')

get_all_seasons(token, server, sys.argv[3])
