import requests
from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='README')

username = input("Enter the github username:")                                                                                                                               
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  repo_url = json[i]['html_url']
  repo = json[i]['name']
  releases = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/releases/latest')

  mdFile.new_line('********')
  if(releases.status_code == 200):
    json2 = releases.json()
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=json[i]['html_url'],text=json[i]['name']) + ' ' + 'Latest Release: ' + mdFile.new_inline_link(link=json2['html_url'],text=json2['tag_name']) + '\n')
  else:
    mdFile.new_line('Repository: ' + mdFile.new_inline_link(link=json[i]['html_url'],text=json[i]['name']) + "\n" )

  if(json[i]['description'] != None):
    mdFile.new_line('Description: ' + json[i]['description'])
  else: 
    mdFile.new_line(text='There is no description for this repository', bold_italics_code='i')  


  mdFile.new_line('********')

print("done")
mdFile.create_md_file()