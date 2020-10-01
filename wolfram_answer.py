import requests
import json

# Enter your own API key below
key = ''
question = str(input('Input the question you want Wolfram Alpha to answer > '))

r = requests.get('https://api.wolframalpha.com/v2/query?input={}&appid={}&format=plaintext&output=json'.format(question.replace(' ', '+'), key))

json_data = r.json()

print(json_data['queryresult']['pods'][1]['subpods'][0]['plaintext'])

"""Add it so that you can have show multiple solutions"""
