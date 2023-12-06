#!/bin/bash

remote_ssh_user=ctf
remote_ssh_host=141.85.224.104
remote_ssh_port=34622

# Compute private SSH key for login.
python compute_private_key.py

# Login using the private SSH key.
ssh -i sol_key "$remote_ssh_user"@"$remote_ssh_host" -p "$remote_ssh_port" -o StrictHostKeyChecking=no "cat /home/ctf/flag"
