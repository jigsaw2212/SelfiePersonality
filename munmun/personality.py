import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV2
import csv,pandas, os


personality_insights = PersonalityInsightsV2(
    username='b216eb07-5f7c-48b6-8574-f629592a4b95',
    password='yNHh7gxb41Ez')

df = pandas.read_csv('EquiPartition.csv')

count = 0

for item in range(len(df['Name'])):

	count += 1

	if count >= 200:

		personality_text = df['img_txt'][item]

		name = df['Name'][item]

		print name

		f = json.dumps(personality_insights.profile(
		text=personality_text ), indent=2)

		# print f
		
		with open("Jsons" + '/' + name + ".json","a") as j:
			j.write(f)

# with open(join(dirname(__file__), '../resources/personality.txt')) as \
#         personality_text:
#     personality_insights_json = {"contentItems": [
#         {"id": "245160944223793152", "userid": "bob", "sourceid": "twitter",
#          "created": 1427720427, "updated": 1427720427,
#          "contenttype": "text/plain", "charset": "UTF-8",
#          "language": "en-us", "content": personality_text.read(),
#          "parentid": "", "reply": "false", "forward": "false"}]}
# print(json.dumps(personality_insights.profile(
#     text=personality_insights_json), indent=2))
#
# with open(join(dirname(__file__), '../resources/personality.es.txt')) as \
#         personality_text:
#     print(json.dumps(personality_insights.profile(
#         text=personality_text.read(), language='es'), indent=2))
