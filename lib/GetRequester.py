import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #sends a GET request to the URL passed in on initialization. This method should return the body 
        #of the response
        #why do i use self.url insead of url? 
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        #use get_response_body to send a request, then return a Python list or dictionary made up of 
        #data converted from the response of that request
        #why do i need to call self on the get_response_body??  
        return json.loads(self.get_response_body())
