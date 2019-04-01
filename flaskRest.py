from flask import Flask, request, jsonify
from config.local import system_config
from database.UserModel import User
import mongoengine
import sys
import redis
import datetime
import json

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'PUT', 'POST'])
@app.route('/<path:path>', methods=['GET', 'PUT', 'POST'])
def process_request(path):

    def method_get_func():
        try:
            if cache.exists(request.full_path):
                return cache.get(request.full_path)

            data = dict(request.args.items())
            if len(data):
                response = {'status': 'OK',
                            'message': 'Requested user data',
                            'data': User.objects(**data).to_json()}
            else:
                response = {'status': 'ERROR',
                            'message': 'API take GET requests with [fullname, id, gender, birthdate, timestamp] params.'}
                cache.set(request.full_path, str(response))
                return response
        except mongoengine.errors.InvalidQueryError as e:
            response = {'status': 'ERROR',
                        'message': str(e)}
            cache.set(request.full_path, str(response))
            return response

    def method_post_func():
        if request.json:
            new_user = User(timestamp=datetime.datetime.now(),
                            **request.json)
            new_user.save(write_concern={"w": 1, 'j': True})
            return {'status': 'OK', 'message': 'User created'}
        else:
            return {'status': 'ERROR', 'message': 'API take POST data in json format '
                                                  '{fullname: fullname_value, '
                                                  'birthdate: birthdate_value, '
                                                  'gender: male or female}'}

    def method_put_func():
        if request.json:
            edited_user = User.objects.get(**request.json['search_terms'])
            edited_user.update(**request.json['update_data'])
            edited_user.save(write_concern={"w": 1, 'j': True})
            return {'status': 'OK', 'message': 'User edited'}
        else:
            return {'status': 'ERROR',
                    'message': 'API take PUT data in json format '
                               '{search_terms:'
                               '{fullname: fullname_value, birthdate: birthdate_value, gender: male or female},'
                               'update_data:'
                               '{fullname: fullname_value, birthdate: birthdate_value, gender: male or female}'}

    process_request_method = {
        'GET': method_get_func,
        'POST': method_post_func,
        'PUT': method_put_func
    }
    response = process_request_method[request.method]()
    if type(response).__name__ in ['string', 'tuple', 'bytes']:
        return response
    return json.dumps(response)


if __name__ == '__main__':
    cache = redis.Redis(system_config.REDIS_SERVER)
    mongoengine.connect(db=system_config.MONGODB_DB)
    app.run()

