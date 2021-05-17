import requests
import sys
from mdutils.mdutils import MdUtils

token = sys.argv[1]

headers = {
    'Authorization': "token " + token
}

mdFile = MdUtils(file_name='README')

#username = input("Enter the github username:")
username = 'iqb-berlin'                                                                                                                               
request = requests.get('https://api.github.com/users/'+username+'/repos',headers=headers)
repository_json = request.json()
for i in range(0,len(repository_json)):
  repo = repository_json[i]['name']
  releases = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/releases/latest', headers=headers)
  contributor = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/contributors', headers=headers)
  languages = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/languages', headers=headers)
  tags = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/tags', headers=headers)
  tags_json = tags.json()

  mdFile.new_line('********')
  
  if(releases.status_code == 200 and len(tags_json) != 0):
    releases_json = releases.json()
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']) + ' ' + 'Release: ' + mdFile.new_inline_link(link=releases_json['html_url'],text=releases_json['tag_name']))
  elif(releases.status_code != 200 and len(tags_json) != 0):
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']) + ' ' + 'Release: ' + mdFile.new_inline_link(link='https://github.com/'+username+'/'+repo+'/releases/tag/'+tags_json[0]['name'],text=tags_json[0]['name']))
  else:
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=repository_json[i]['html_url'],text=repository_json[i]['name']) )

  if(repository_json[i]['description'] != None):
    mdFile.new_line('Description: ' + repository_json[i]['description'])
  else: 
    mdFile.new_line(text='There is no description for this repository', bold_italics_code='i')  
  
  if(contributor.status_code == 200):
    contributor_json = contributor.json()
    for c in range(0,len(contributor_json)):
        mdFile.new_line('Contributor: ' + mdFile.new_inline_link(link=contributor_json[c]['html_url'],text=contributor_json[c]['login'])) 

  if(languages.status_code == 200):
    languages_json = languages.json()
    mdFile.new_line('Languages: ')
    for keys in languages_json.keys():
      mdFile.write(keys + " ")
 
  mdFile.new_line('********')

print("done")
mdFile.create_md_file()