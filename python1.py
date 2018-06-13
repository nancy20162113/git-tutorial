#version test 1
#author='zhy'
import requests

url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
#print("status code:",r.status_code)
reposs_dict=r.json()

print("总共的仓库数量:",reposs_dict["total_count"])

reposs_list=reposs_dict["items"]
print("返回的仓库数量：",len(reposs_list))
for  repo1_dict in reposs_list:
    print("Name:",repo1_dict['name'])
    print("Owner:",repo1_dict['owner']['login'])
    print("Stars:",repo1_dict["stargazers_count"])
    print("Repository:",repo1_dict["html_url"])
    print("Description:",repo1_dict["description"])





