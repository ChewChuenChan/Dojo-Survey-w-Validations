from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

#set up the dojo object
class Dojo:
    # declare the database schema here
    db = "dojo_survey_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#class method for function create
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos ( name ,location, language, comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s, %(language)s,%(comment)s, NOW() , NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result

    @classmethod
    def show_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query)
        print(result)
        return Dojo(result[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if  len(dojo['location']) < 1:
            flash("Location must be select.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Language must be select.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid

