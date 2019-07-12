import datetime
import json
import eml_parser
import glob


def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial


with open('sample.eml', 'rb') as fhdl:
        print(fhdl.read())
        raw_email = fhdl.read()

s = open('sample.eml', 'r').read()
print(s)

# print(json.dumps(parsed_eml, default=json_serial))