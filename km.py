import argparse
from lib.process import Process
import os
import json

# parse arguments passed to this script
parser = argparse.ArgumentParser(description='Kuberentes Manager')
parser.add_argument('action', help='type of action', choices=['create', 'delete'])
parser.add_argument('cluster_name', help='name of cluster')
parser.add_argument('zone', help='gcloud zone')
args = parser.parse_args()

action = args.action
cluster_name = args.cluster_name
zone = args.zone
verbosity = 'info'
auth_json_content = os.environ['AUTH_JSON']
auth_json_filename = 'auth.json'

# write AUTH_JSON to file
f = open(auth_json_filename, 'w')
f.write(auth_json_content)
f.close()

# extract project_id from json
auth_json = json.loads(auth_json_content)
project = auth_json['project_id']

# set project
cmd = Process(f'gcloud config set project {project}')
cmd.run()

# authenticate
cmd = Process(f'gcloud auth activate-service-account --key-file={auth_json_filename}')
cmd.run()

# check for actions chosen
if action == 'create':
    cmd = Process(f'gcloud container clusters create {cluster_name} --enable-network-policy --zone {zone} -q --verbosity={verbosity}')
    exit(cmd.run())
elif action == 'delete':
    cmd = Process(f'gcloud container clusters delete {cluster_name} --zone {zone} -q --verbosity={verbosity}')
    exit(cmd.run())
