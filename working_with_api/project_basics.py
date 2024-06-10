###Make an API call and store the response

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'} 
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Process results.                                                                                                                                                           
print(response_dict.keys())

###Working with Response Dictionary

# import requests

# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept':'application/vnd.github.v3+json'} 
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")

##Explore information about repositories
# repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")

##Examine the first repository
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
    # print(key)

###Details of first repository
# 
# import requests
# 
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept':'application/vnd.github.v3+json'} 
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")
# 
# response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")
# 
##Explore information about repositories
# repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")
# 
##Examine the first repository
# repo_dict = repo_dicts[0]
# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")
# 
###Summarizing the Top Repositories

# import requests

# url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
# headers = {'Accept':'application/vnd.github.v3+json'} 
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")

##Explore information about repositories
# repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")

##Examine the first repository
# repo_dict = repo_dicts[0]
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
    # print(f"Name: {repo_dict['name']}")
    # print(f"Owner: {repo_dict['owner']['login']}")
    # print(f"Stars: {repo_dict['stargazers_count']}")
    # print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    # print(f"Description: {repo_dict['description']}")

###Monitoring API Rate Limits

# import requests

# from plotly.graph_objs import Bar
# from plotly import offline

# url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
# headers = {'Accept':'application/vnd.github.v3+json'} 
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# response_dict = r.json()
# repo_dicts = response_dict['items']
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
##Visualization
# data = [{
    # 'type' : 'bar',
    # 'x' : repo_names,
    # 'y' : stars,
# }]
# layout = {
    # 'title' : 'Most-Starred Python Projects on Github',
    # 'xaxis' : {'title':'Repository'},
    # 'yaxis' : {'title':'Stars'}
# }
# figure = {'data':data, 'layout':layout}
# offline.plot(figure, filename='python_repos.html')

###Refining plotly Charts

# import requests

# from plotly.graph_objs import Bar
# from plotly import offline

# url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
# headers = {'Accept':'application/vnd.github.v3+json'} 
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# response_dict = r.json()
# repo_dicts = response_dict['items']
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
##Visualization
# data = [{
    # 'type' : 'bar',
    # 'x' : repo_names,
    # 'y' : stars,
    # 'marker' : {'color' : 'rgb(60, 100, 150)',
                # 'line' : {'width':1.5, 'color':'rgb(25, 25, 25)'}
                # },
    # 'opacity' : 0.6
# }]
# layout = {
    # 'title' : 'Most-Starred Python Projects on Github',
    # 'titlefont' : {'size':28},
    # 'xaxis' : {
        # 'title':'Repository',
        # 'titlefont' : {'size':24},
        # 'tickfont' : {'size':14},
        # },
    # 'yaxis' : {
        # 'title':'Stars',
        # 'titlefont' : {'size':24},
        # 'tickfont' : {'size':14},
        # },
# }
# figure = {'data':data, 'layout':layout}
# offline.plot(figure, filename='python_repos.html')

###Adding Custom Tooltips

# import requests

# from plotly.graph_objs import Bar
# from plotly import offline

# url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
# headers = {'Accept':'application/vnd.github.v3+json'} 
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# response_dict = r.json()
# repo_dicts = response_dict['items']
# repo_names, stars, labels = [], [], []
# for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])

    # owner = repo_dict['owner']['login']
    # description = repo_dict['description']
    # label = f"{owner}<br />{description}"       ###(html element->line break, plotly allows to use html code within text elements)
    # labels.append(label)

##Visualization
# data = [{
    # 'type' : 'bar',
    # 'x' : repo_names,
    # 'y' : stars,
    # 'hovertext' : labels,
    # 'marker' : {'color' : 'rgb(60, 100, 150)',
                # 'line' : {'width':1.5, 'color':'rgb(25, 25, 25)'}
                # },
    # 'opacity' : 0.6
# }]
# layout = {
    # 'title' : 'Most-Starred Python Projects on Github',
    # 'titlefont' : {'size':28},
    # 'xaxis' : {
        # 'title':'Repository',
        # 'titlefont' : {'size':24},
        # 'tickfont' : {'size':14},
        # },
    # 'yaxis' : {
        # 'title':'Stars',
        # 'titlefont' : {'size':24},
        # 'tickfont' : {'size':14},
        # },
# }
# figure = {'data':data, 'layout':layout}
# offline.plot(figure, filename='python_repos.html')

###Hacker News API

# import requests
# import json
# 
###Make an API call and store the response.
# url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
# r = requests.get(url)
# print(f"Status code: {r.status_code}")
# 
##Explore the structure of the data.
# response_dict = r.json()
# readable_file = 'data/readable_hn_data.json'
# with open(readable_file, 'w') as f:
    # json.dump(response_dict, f, indent=4)