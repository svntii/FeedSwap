#!/usr/bin/env python3

import requests
import os
import json
import pandas as pd
import csv
import datetime
import dateutil.parser
import time



os.environ['TOKEN'] = 'YOUR_TOKEN'

def auth():
    return os.environ.get('TOKEN')


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers




def main():
    pass




if __name__ == "__main__":
    main()


