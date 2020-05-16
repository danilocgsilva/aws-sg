import sys
sys.path.insert(1, '..')
from src.Fetcher import Fetcher
from src.Client_Config import Client_Config

client_config = Client_Config()
fetcher = Fetcher()
fetcher.set_client(client_config.get_client())
security_groups_data = fetcher.sgs_data()

print(security_groups_data)
