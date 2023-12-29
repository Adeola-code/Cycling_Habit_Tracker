import requests
from datetime import datetime
import random
import os
from decouple import config

# Load environment variables from .env
USERNAME = config('USERNAME')
TOKEN = config('TOKEN')
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)



# Create graph
# graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params={
#     "id":"graph2",
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu"
# }
# headers={
#     "X-USER-TOKEN": TOKEN
# }
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)




#POST PIXEL
graph_post=f"{pixela_endpoint}/{USERNAME}/graphs/graph2"
today=datetime(year=2023, month=random.randint(1,9), day=random.randint(1,29))

post_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many Kilometres did you cycle today?: "),

}
headers={
    "X-USER-TOKEN": TOKEN
}
response=requests.post(url=graph_post,json=post_params,headers=headers)
print(response.text)




# #UPDATE A PIXEL
# today=datetime(year=2023, month=10, day=19)
# DATE= today.strftime("%Y%m%d")
# update_pixel=f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{DATE}"
#
# update_params={
#     "quantity":"34",
#
# }
# head={
#     "X-USER-TOKEN": TOKEN
# }
# response=requests.put(url=update_pixel,json=update_params,headers=head)
# print(response.text)



#DELETE PIXEL
today=datetime(year=2023, month=10, day=19)
DATE= today.strftime("%Y%m%d")
update_pixel=f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{DATE}"


head={
    "X-USER-TOKEN": TOKEN
}
# response=requests.delete(url=update_pixel,headers=head)
# print(response.text)