"""
A simple Lambda function that has simplejson as a function level dependency
And uses code from common_files/common1.py
"""
import requests
import jinja2
from common1 import common1_function

def handler(event,context):
    return "Successfully imported requests, jinja2 and common1_function"
