import pandas
import numpy
import requests

response = requests.get("https://api.jotform.com/user/forms", headers={
    "APIKEY": "ab612859cb740357ec912f07c79e2fe9"
})
response.json

#%%
