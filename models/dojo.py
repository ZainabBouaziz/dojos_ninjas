from config.mysqlconnection import connectToMySQL
from models.ninja import Ninja

class Dojo :
    def __init__(self,data):
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

        self.ninjas=[]

    @classmethod
    def show(cls):
        query="SELECT * FROM dojos"
        results=connectToMySQL('dojos_ninjas').query_db(query)
        for result in results:
            result=cls(result)
        return results
    
    @classmethod
    def ninjas_dojos(cls,id):
        query="select * from dojos LEFT JOIN ninjas on ninjas.dojos_id=dojos.id where dojos.id=%(id)s"
        results=connectToMySQL('dojos_ninjas').query_db(query,id)

        dojo=cls(results[0])

        for data in results:
            ninja_data={
                'first_name':data['first_name'],
                'last_name':data['last_name'],
                'age':data['age'],
                'created_at':data['created_at'],
                'updated_at':data['updated_at'],
            }

            dojo.ninjas.append(Ninja(ninja_data))
        return dojo