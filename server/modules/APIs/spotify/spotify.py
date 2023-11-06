import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
import random
import string
from flask import Flask, request, redirect
import base64, json, requests
from flask_restful import Resource, abort, reqparse
from flasgger import Swagger, swag_from

class SpotifyLogin(Resource):
    def __init__(self) -> None:
        load_dotenv()
        # Access environment variables
        self.client_id = os.getenv('SPOTIPY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
        self.scope = "user-read-playback-state playlist-modify-public"
        self.state = self.generate_random_string(16)
        self.auth_manager = None
        self.access_token = None
        self.given_scope = None
        self.auth_url = None
        self.has_code = False

    def get(self) -> dict:
        state = self.generate_random_string(16)
        self.auth_manager = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri, scope=self.scope, state=state)
        self.auth_url = self.auth_manager.get_authorize_url()
        if request.args.get('code'):
            self.has_code = True
            code = request.args.get('code')
            token_info = self.auth_manager.get_access_token(code)
            self.access_token = token_info['access_token']
            self.given_scope = request.args.get('scope')
        else:
            self.has_code = False
            if self.access_token is None:
                return {'auth_url': self.auth_url}

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))