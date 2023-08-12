from flask import abort


def authControl():
    return True
    abort(401, 'Token Is Invalid')


