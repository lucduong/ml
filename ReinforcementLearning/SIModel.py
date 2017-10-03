# Need to install `pymongo` first
import re
import datetime


class SI:
    regex = re.compile(r"[a-zA-Z]{3}[0-9]{9}")

    def __init__(self, image_path, text_path, bn):
        self.image = image_path
        self.text = text_path
        self.booking_number = bn

    def insert_to(self, collection):
        if self.image == '' or self.text == '':
            return False
        else:
            today = datetime.datetime.today()
            si = {
                'image': self.image,
                'text': self.text,
                'booking_number': self.booking_number,
                'created_at': today.strftime('%H:%M:%S %Y-%m-%d')
            }
            return collection.insert_one(si).inserted_id

    @staticmethod
    def bulk_insert(collection, si_list):
        today = datetime.datetime.today()
        si_s = []
        for itm in si_list:
            if itm.image != '' and itm.text != '':
                si = {
                    'image': itm.image,
                    'text': itm.text,
                    'booking_number': itm.booking_number,
                    'created_at': today.strftime('%Y-%m-%d %H:%M:%S')
                }
                si_s.append(si)
        if len(si_s) > 0:
            result = collection.insert_many(si_s)
            return result.inserted_ids
        return []
