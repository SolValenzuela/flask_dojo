from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        #self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]
    
    @classmethod
    def add_dojo(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s)"
        results=connectToMySQL('dojos_y_ninjas').query_db(query,data)
        print(results)
        return results

    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        results=connectToMySQL('dojos_y_ninjas').query_db(query)    
        #print(results)
        all_data=[]
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_dojos_y_ninjas(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id WHERE dojos.id=%(dojo_id)s"
        results=connectToMySQL('dojos_y_ninjas').query_db(query,data)    
        print(results)
        dojo_data=results[0]
        dojo=Dojo(dojo_data)
        all_ninjas=[]
        for data in results:
            ninja_data={
                'id':data['ninjas.id'],
                'first_name':data['first_name'],
                'last_name':data['last_name'],
                'age':data['age'],
                'created_at':data['ninjas.created_at'],
                'updated_at':data['ninjas.updated_at']
            }
            new_ninja=Ninja(ninja_data)
            all_ninjas.append(new_ninja)
        dojo.ninjas=all_ninjas
        return dojo