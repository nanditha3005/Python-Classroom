from fastapi import FastAPI

#create fastapi app
app=FastAPI()
'''
Usage: Home Page
API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get('/')
def home_page():
    return{'msg':'Home page'}

'''
Usage: About Page
API URL: http://127.0.0.1:8000/About
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get('/About')
def about_page():
    return{'msg':'About page'}

'''
Usage: Contact Page
API URL: http://127.0.0.1:8000/Contact
Method Type:GET
Required Fields: None
Access Type:Public
''' 

@app.get('/Contact')
def contact_page():
    return{'msg':'contact page'}

