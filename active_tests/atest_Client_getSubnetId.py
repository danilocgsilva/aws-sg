from awssg.Client import Client
import argparse

arguments_list = [
    ['--profile', '-p'],
    ['--region', '-r'],
    ['--name', '-n']
]

client = Client()

results = client.getSubnetId()