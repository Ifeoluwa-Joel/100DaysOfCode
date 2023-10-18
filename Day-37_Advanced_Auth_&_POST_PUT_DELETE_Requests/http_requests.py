import requests

"""
1. GET -> requests.get()
2. POST -> requests.post()
3. PUT -> requests.put()
4. DELETE -> requests.delete()
https://requests.readthedocs.io/en/latest/api/
"""

# ### POST EXAMPLE: Create pixela user ###############
# pixela_new_user_endpoint = "https://pixe.la/v1/users"
#
# user_params = {
#     "token": os.environ["PIXELA_API_TOKEN"],
#     "username": "wreckitralph",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_new_user_endpoint, json=user_params)
# print(response.text)

