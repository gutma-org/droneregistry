## Drone Registry Sandbox

This is a GUTMA sandbox for working on a interoperable drone registry. It has three main things, you can start in the order below: 

1. Registry Landscape Whitepaper
2. Interoperatble API Specification, the technical specification for a registry. You can see the API specification and explore API endpoints at [https://droneregistry.herokuapp.com](https://droneregistry.herokuapp.com) 
3. A working API with all endpoints and sample data for you to explore [https://droneregistry.herokuapp.com/api/v1/](https://droneregistry.herokuapp.com/api/v1/)


## Contribute

You can open issues to this repository, review the Landscape document to review the background and look at open issues for  

## Technical Details  / Self-install

This is a Django project that uses Django and Django Rest Framework and the API Specification 

### 1. Install Dependencies
Python 3 is required for this and install dependencies using `pip install -r requirements.txt`.

### 2. Create Initial Database
Use `python manage.py migrate` to create the initial database tables locally. It will use the default SQLLite. 

### 3. Populate initial data
Use `python manage.py loaddata registry/defaultregistrydata.json` to populate initial data. 

### 4. Launch browser 
Launch browser to http://localhost:8000/api/v1/ to launch the API Explorer
