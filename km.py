import argparse
from lib.process import Process


def run_command(cmd):
    process = Process(cmd)

    for line in process.run():
        print(line)

    print(f'CMD_EXIT_CODE: {process.exit_code}')

    exit(process.exit_code)


parser = argparse.ArgumentParser(description='Kuberentes Manager')
parser.add_argument('action', help='type of action', nargs='?', choices=['create', 'delete'])
parser.add_argument('cluster_name', help='name of cluster')

args = parser.parse_args()

action = args.action
cluster_name = args.cluster_name

if action == 'create':
    cmd = f'gcloud container clusters create {cluster_name} --enable-network-policy --zone europe-west3-a -q'
    exit(run_command(cmd))
elif action == 'delete':
    cmd = f'gcloud container clusters delete {cluster_name} --zone europe-west3-a -q'
    exit(run_command(cmd))
