#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       _                              
#      | |                             
#    __| |_ __ ___  __ _ _ __ ___  ___ 
#   / _` | '__/ _ \/ _` | '_ ` _ \/ __|
#  | (_| | | |  __/ (_| | | | | | \__ \
#   \__,_|_|  \___|\__,_|_| |_| |_|___/ .
#
# A 'Fog Creek'–inspired demo by Kenneth Reitz™

import os
os.system('pip install flask')
#os.system('pip install dotenv')
os.system('pip install autogenstudio')
from flask import Flask, request, render_template, jsonify
import test
from dotenv import load_dotenv, find_dotenv
#from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import json
from autogenstudio import AutoGenWorkFlowManager
from autogenstudio import AgentWorkFlowConfig
import time



####################---

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')



#load_dotenv('appauto2/.gitignore/.env')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# Dream database. Store dreams in memory for now. 
DREAMS = ['Python. Python, everywhere.']

@app.route('/workflow')
def run_workflow():
    return None


@app.after_request
def apply_kr_hello(response):
    """Adds some headers to all responses."""
  
    # Made by Kenneth Reitz. 
    if 'MADE_BY' in os.environ:
        response.headers["X-Was-Here"] = os.environ.get('MADE_BY')
    
    # Powered by Flask. 
    response.headers["X-Powered-By"] = os.environ.get('POWERED_BY')
    return response


@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

@app.route('/lol')
def rlol():
    return jsonify(test.lol())
  
@app.route('/dreams', methods=['POST'])
def dreams():
    """Simple API endpoint for dreams. 
    In memory, ephemeral, like real dreams.
    """
  
    # Add a dream to the in-memory database, if given. 
    if 'dream' in request.args:
        

        task_query = request.args['dream']
        agent_work_flow.run(message=task_query)
        DREAMS.append(agent_work_flow.agent_history[-1]["message"]["content"])
    return "done"

@app.get('/dreams_get')
def dreams_get():
    time.sleep(10)

    for i in DREAMS:
        if i == 'TERMINATE':
            DREAMS.remove(i)
    if "TERMINATE" in DREAMS: DREAMS.remove("TERMINATE")

    DREAMS.append(agent_work_flow.agent_history[-1]["message"]["content"])
    print("the dream does equal = = ",DREAMS)
    
    # Return the list of remembered dreams. 
    return jsonify(DREAMS)

#load config file and replace text with key information
text = None
with open('appauto2/configlist.json') as r:
  text = r.read().replace("<OPEN_API_KEY>", os.environ.get('OPEN_API_KEY'))

# load an agent specification in JSON
agent_spec = json.loads(text)

# Create an AutoGen Workflow Configuration from the agent specification
agent_work_flow_config = AgentWorkFlowConfig(**agent_spec)

# Create a Workflow from the configuration
agent_work_flow = AutoGenWorkFlowManager(agent_work_flow_config)

# Run the workflow on a task
#task_query = "What is the height of the Eiffel Tower?"
#agent_work_flow.run(message=task_query)

if __name__ == '__main__':
    app.run()