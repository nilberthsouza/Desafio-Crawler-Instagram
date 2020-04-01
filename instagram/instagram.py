import requests
import json

class Convert:

    @staticmethod
    def from_key_to_link(key):
        link = 'http://instagram.com/explore/tags/'+str(key)+'/?__a=1'
        return link

class Publications:

    link = ''

    def takePublications(self):
        pubs = requests.get(self.link).text
        return pubs

    def takeTextPublications(self):
        publist = []
        rawpublications= self.takePublications()
        result = json.loads(rawpublications)
        result = result['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        print(type(result)) 
        for i in range (len(result)):
            text = result[i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            publist.append(text)
        return publist






