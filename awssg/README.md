`__main__.py` The file that is deployied to the environment.

`Client.py` General wrapper around the AWS Client. Emulates some methods from the AWS client.

`Client_Config.py` If necessary, takes the profile and/or region when necessary for the client. Have the `get_client` method to return the AWS client already setted.

`Client_Interface.py` Forces some methods for the custom AWS Client wrapper.

`Fetcher.py` Get AWS data.

`Helpers.py` Generics methods that don't fit to any other class's responsability.

`Parser_Interface.py` Sets mandatory methods for classes responsible for fetching data.

`RDS.py` Get RDS data.

`RDS_Parser.py` Deals with raw data returned from AWS Client from rds.

`Regions_Parser.py` Deals with raw data returned from AWS Client from regions.

`SG.py` Get data from security group.

`SG_Parser.py` Deals with security group data.
