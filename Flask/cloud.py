from sqlite3 import connect
from cloudant.client import Cloudant
client = Cloudant.iam("dbd80534-7627-4421-97b3-4500743da231-bluemix", "_KZ0TBX2o1SS-tcJb7AZ4JBdVwl8Yds5At9hgmMzSGnp", connect = True)
my_database = client.create_database('my_database')
