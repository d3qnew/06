import json
from collections import OrderedDict
from flask import jsonify

with open('resource/txt.json', encoding='utf8') as json_file:
    txt = json.load(json_file,object_pairs_hook=OrderedDict)
    #txt = json.dumps(json.load(json_file), ensure_ascii=False)

