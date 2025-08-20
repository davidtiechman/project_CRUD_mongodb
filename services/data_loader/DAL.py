from data_loader.connection import Connection

class Client:
    def __init__(self):
        self.conn = Connection()

    def create_document(self,Document):
        col = self.conn.get_collection()
        id =  Document.Id
        firstname = Document.First_name
        lastname =  Document.Last_name
        phon =  Document.Phone_number
        rank = Document.Rank
        col.insert_one({'id':id,'firstname':firstname,'lastname':lastname,'phon':phon,'rank':rank})
        return
    def update_document(self,id):
        return
    def delete_document(self,id):
        return
    def read_document(self):
        col = self.conn.get_collection()
        doc =  col.find()
        return doc