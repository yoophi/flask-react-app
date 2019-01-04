from flask import jsonify

from . import api


@api.route('/v1.0/sample')
def sample():
    return jsonify({'ok': True})
