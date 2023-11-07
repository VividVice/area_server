from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from modules.database.DB import DataBaseOpps as DB
from modules.config.config import Config
from modules.utils.jsonToken import UnpackToken
from modules.APIs.AREA_lists import delete_methods

app = Config().GetApp()
db = Config().GetDb()

class END(Resource):
    def get(self):
        """ DELETE EVERYTHING
            run delete_methods() from modules/APIs/AREA_lists.py on every user
        """
        Users = DB.GetAllUsers()
        for user in Users:
            for service in delete_methods:
                delete_methods[service]["all"](user)
        return {"message": "everything deleted"}, 200