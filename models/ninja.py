from config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls,data):
        query='INSERT INTO ninjas (first_name,last_name,age,dojos_id,created_at,updated_at) values(%(first_name)s,%(last_name)s,%(age)s,%(dojo)s,now(),now())'
        return connectToMySQL('dojos_ninjas').query_db(query,data)





