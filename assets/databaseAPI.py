# Imports

from pysondb import db
from assets.stuff import *


# Initializing database
DATABASE = db.getDb('databases/users.json')


def new_user(user_id, nh_id=0):   # nh_id - NiceHash id
    if isUserExist(user_id):
        print(f'user {user_id} is already exist')
    else:
        DATABASE.add({
            'user_id': user_id,
            'nh_id': nh_id
        })
        log('new_user', user_id)


def add_nh_id(user_id, nh_id=0):
    if isUserExist(user_id):
        DATABASE.updateById(
            get_user_id_in_database(user_id),
            {'nh_id': nh_id}
        )
        log('nh_id_added')
    else:
        new_user(user_id, nh_id)


def get_user_id_in_database(user_id):
    return getUserInDataBase(user_id)[0].get('id')


def getUserInDataBase(user_id):
    return DATABASE.getByQuery({"user_id": user_id})     # Getting user in database


def isUserExist(user_id):    # Checking if user exist in database
    return len(getUserInDataBase(user_id)) != 0
