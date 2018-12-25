# from os.path import realpath, dirname
# import json
from scrapyuniversal.jsons import jsons


# 读取JSON文件
# def get_config(name):
#     path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
#     with open(path, 'r', encoding='utf-8') as f:
#         return json.loads(f.read())


def get_config(name):
    return jsons.get(name)
