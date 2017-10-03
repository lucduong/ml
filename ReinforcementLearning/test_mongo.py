from pymongo import MongoClient
from SIModel import  SI

client = MongoClient('localhost', 27017)
db = client.si

si_collection = db.si

si = SI('/path/to/img.png', '/path/to/txt.png', 'XXX123456789')
inserted_id = si.insert_to(si_collection)
print('Inserted: ', inserted_id)

inserted_ids = SI.bulk_insert(si_collection, [si, SI('/path/to/img1.png', '/path/to/img1.png', '')])
print ('Inserted Ids: ', inserted_ids)