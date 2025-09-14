#!/usr/bin/env python3
"""
Basic Flask API to trigger Ansible playbooks via HTTP(S) 
-------------still need to test HTTPS 
"""

import os
import subprocess
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# If I want to use tokens I can use command "export API_TOKEN=use_this_token!!!"
API_TOKEN = os.environ.get("API_TOKEN") 


def _check_token(req):
    token = req.headers.get("X-API-Token")
    return token and API_TOKEN and token == API_TOKEN


@app.before_request
def require_token():
    if API_TOKEN:
        if not _check_token(request):
            abort(401, description="Unauthorized")


@app.route("/run-playbook", methods=["POST"])
def run_playbook():
    
    #Key value pair information is APPLICATION SPECIFIC! and is conveniently located in app documentation. Would've saved me a lot of time
    payload = request.get_json(force=True) #looks thru json for the POST req
    playbook  = payload.get("playbook",    "site.yml") # pulls the playbook value from JSON -- will default to "site.yml" if you don't specify a playbook
    inventory = payload.get("inventory",   "inventory.yaml") #SAME but for inventory
    extra_vars = payload.get("extra_vars", {}) #For passing variables to the API. Passing them thru the API has a higher priority than the playbook itself 
    print("Received JSON payload:", payload) # Print statement so I can see the JSON in a file I made for debugging

    # Build the base command
    cmd = ["ansible-playbook", playbook, "-i", inventory]

    # Vault password file (non-interactive decryption)
    vault_file = os.environ.get("ANSIBLE_VAULT_PASSWORD_FILE") 
    if vault_file:
        cmd += ["--vault-password-file", vault_file]  # If there is no vault pw (rn I disabled my vaulted keypath for testing) this will bypass

    # Adds in the extra vars along with the -e flag for passing them. This is also still in testing but can prove pretty useful later.
    if extra_vars:
        ev_str = " ".join(f"{k}='{v}'" for k, v in extra_vars.items())
        cmd += ["-e", ev_str]


#This "try" block basically runs the ansible command and returns JSON telling me
#if it was successful or not


    try:   #If a try line fails it jumps to the execpt line
        result = subprocess.run(
            cmd,                                              #refer to line 40 for command, then line 48 if any variables are being added 
            capture_output=True,                              #these lines are pretty readable, just capturing that output and will give an error if needed
            text=True,
            check=True
        )
        return jsonify({
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        })
    except subprocess.CalledProcessError as e:  #This block catches non-zero exits and gives them error status
        return jsonify({
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr
        }), 500


if __name__ == "__main__":  #Basically means "if you run this directly" an example of indirectly would be running it as a module
    # Configuration from environment or defaults
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    ssl_cert = os.environ.get("SSL_CERT_FILE")
    ssl_key  = os.environ.get("SSL_KEY_FILE")

    if ssl_cert and ssl_key:
        # HTTPS mode
        app.run(host=host, port=port, ssl_context=(ssl_cert, ssl_key)) #test with a curl using a self signed cert ---still need to do this
    else:
        # HTTP mode
        app.run(host=host, port=port, debug=True)
