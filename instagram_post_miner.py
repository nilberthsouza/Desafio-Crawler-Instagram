# -*- coding: utf-8 -*-
#!pip install pymongo
import requests
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.socialnetwork


def return_comments(shortcode_id):
    knowed_page = str(
        'https://www.instagram.com/p/' +
        shortcode_id +
        '/?__a=1')
    coments = json.loads(str(requests.get(knowed_page).text))
    total_comments = []
    for j in range(len(coments['graphql']['shortcode_media']
                       ['edge_media_to_parent_comment']['edges']) - 1):
        total_comments.append(coments['graphql']['shortcode_media'][
                              'edge_media_to_parent_comment']['edges'][j]['node']['text'])
    return total_comments


def crawling_page(newDictionary, searchedTerm):
    for i in range(
            len(newDictionary['graphql']['hashtag']['edge_hashtag_to_media']['edges'])):
        user_id = newDictionary['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['id']
        short_code = newDictionary['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['shortcode']
        text_post = newDictionary['graphql']['hashtag']['edge_hashtag_to_media'][
            'edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
        comments = list(return_comments(str(short_code)))

        userdata = {
            '_id': user_id,
            'short_code': short_code,
            'text_content': text_post,
            'comments': comments}

        db[str(searchedTerm)].insert_one(userdata)


def create_colection(tag):
    '''make a colection with the tag specified'''
    colection = db[str(tag)]
    return True


def register_new_tag():
    print('item a ser pesquisado:\n')
    searchedTerm = str(input())

    phraselSearchTerm = str(
        'https://www.instagram.com/explore/tags/' +
        searchedTerm +
        '/?__a=1')

    pageTotal = requests.get(phraselSearchTerm)

    newDictionary = json.loads(str(pageTotal.text))

    create_colection(str(searchedTerm))

    crawling_page(newDictionary, searchedTerm)
    return None


def fetch(colection):
    for colect in colection.find():
        pprint.pprint(colect)


def select_by_id(colection, id):
    return colection.find_one({'__id': id})


def delete_by_od(colection, id):
    return colection.delete_one({'_id': id})


def return_registered_colections():
    return db.list_collection_names()


register_new_tag()
