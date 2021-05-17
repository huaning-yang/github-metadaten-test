import requests
from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='README')

#username = input("Enter the github username:")
username = 'iqb-berlin'                                                                                                                               
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  repo_url = json[i]['html_url']
  repo = json[i]['name']
  releases = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/releases/latest')
  contributor = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/contributors')
  pages = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/pages')
  

  mdFile.new_line('********')
  
  if(releases.status_code == 200):
    json2 = releases.json()
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=json[i]['html_url'],text=json[i]['name']) + ' ' + 'Latest Release: ' + mdFile.new_inline_link(link=json2['html_url'],text=json2['tag_name']))
  else:
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=json[i]['html_url'],text=json[i]['name']) )

  if(json[i]['description'] != None):
    mdFile.new_line('Description: ' + json[i]['description'])
  else: 
    mdFile.new_line(text='There is no description for this repository', bold_italics_code='i')  
  
  if(contributor.status_code == 200):
    contributor_json = contributor.json()
    for c in range(0,len(contributor_json)):
        mdFile.new_line('Contributor: ' + mdFile.new_inline_link(link=contributor_json[c]['html_url'],text=contributor_json[c]['login']))

  if(pages.status_code == 200):
    pages_json = pages.json()
    mdFile.new_line(mdFile.new_inline_link(link=pages_json['html_url'],text='Github Pages'))    

  mdFile.new_line('********')

print("done")
mdFile.create_md_file()