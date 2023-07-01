#!/usr/bin/env python3
import os
import json

# Retrieve the necessary environment variables
ssh_ip = os.environ.get('SSH_IP')
ansible_user = os.environ.get('ANSIBLE_USER')

# Define the inventory dictionary
inventory = {
    'api': {
        'hosts': [],
        'vars': {
            'ansible_user': ansible_user
        }
    }
}

# Add the target host to the inventory
inventory['api']['hosts'].append(ssh_ip)

# Print the inventory as JSON
print(json.dumps(inventory))
