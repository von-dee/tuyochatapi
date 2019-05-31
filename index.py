# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is a sample for a weather fulfillment webhook for an Dialogflow agent
This is meant to be used with the sample weather agent for Dialogflow, located at
https://console.dialogflow.com/api-client/#/agent//prebuiltAgents/Weather

This sample uses the WWO Weather Forecast API and requires an WWO API key
Get a WWO API key here: https://developer.worldweatheronline.com/api/
"""

import json

from flask import Flask, request, make_response, jsonify

import api_commands

app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook

    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    if action == 'flips':
        res = flips(req)
    elif action == 'battery':
        res = battery_status(req)
    elif action == 'simpleflight':
        res = simple_flight(req)
    elif action == 'startmission':
        res = startmission(req)
    elif action == 'takeoff':
        res = takeoff(req)
    elif action == 'rotate':
        res = rotate(req)
    elif action == 'flip':
        res = flip(req)
    elif action == 'land':
        res = land(req)
    else:
        log.error('Unexpected action.')

    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))


def flips(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    response = "All right Flipping"

    return response


def takeoff(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    api_commands.takeoff()

    response = "Yep! Up we go"
    return response


def rotate(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    api_commands.rotate()

    response = "Yep! Im rotating"

    return response


def flip(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    api_commands.flip()

    response = "Watch me do a forward flip"

    return response


def land(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    api_commands.land()

    response = "Yep! Up we go"

    return response


def battery_status(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    response = "The battery percentage is " + api_commands.battery_status();

    # response = "The battery percentage is 67% " ;

    return response


def simple_flight(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    api_commands.simpleflight()

    response = "Oh yeah I can, watch me!"

    return response


def startmission(req):
    """
        Call the codes that does the flips
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    api_commands.startmission()

    response = "I'm on my way"

    return response




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
