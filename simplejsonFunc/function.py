"""
A simple Lambda function that has simplejson as a function level dependency
And uses code from common_files/common2.py
"""

import requests
import simplejson
from common2 import common2_function

def handler(event,context):
    return "Successfully imported requests, simplejson and common2_function"
