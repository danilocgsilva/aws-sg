import sys
import argparse
sys.path.insert(1, '..')
from src.Fetcher import Fetcher
from src.Client_Config import Client_Config

parser = argparse.ArgumentParser()
client_config = Client_Config()
fetcher = Fetcher()
fetcher.set_client(client_config.get_client())
fetcher.sgs_data()

