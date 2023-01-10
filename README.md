# python_fastapi_demo
This tutorial will help in understanding FASTAPI and python

### What Is FastAPI?
FastAPI is a modern, high-performance web framework for building APIs with Python based on standard type hints. It has the following key features:

Fast to run: It offers very high performance, on par with NodeJS and Go, thanks to Starlette and pydantic.
Fast to code: It allows for significant increases in development speed.
Reduced number of bugs: It reduces the possibility for human-induced errors.
Intuitive: It offers great editor support, with completion everywhere and less time debugging.
Straightforward: It’s designed to be uncomplicated to use and learn, so you can spend less time reading documentation.
Short: It minimizes code duplication.
Robust: It provides production-ready code with automatic interactive documentation.
Standards-based: It’s based on the open standards for APIs, OpenAPI and JSON Schema.

### Install FastAPI
As with any other Python project, it would be best to start by creating a virtual environment. If you are not familiar with how to do that, then you can check out the Primer on Virtual Environments.

The first step is to install FastAPI and Uvicorn using pip:

    $ python -m pip install fastapi uvicorn

### Run the First API App With Uvicorn
Run the live server using Uvicorn:

    $ uvicorn main:app --reload

### Check the Response
Open your browser to http://127.0.0.1:8000, which will make your browser send a request to your application. It will then send a JSON response with the following:

    {"message": "Hello World"}

### Check the Interactive API Documentation
Now open http://127.0.0.1:8000/docs in your browser.

### Check the Alternative Interactive API Documentation
Now, go to http://127.0.0.1:8000/redoc in your browser.


