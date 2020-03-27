import requests

class Convert:

    @staticmethod
    def from_key_to_link(key):
        link = 'http://instagram.com/explore/tags/'+str(key)+'/?__a=1'
        return link

class Publications:

    link = ''

    def showPublications(self):
        pubs = requests.get(self.link).text
        return pubs

