import os

from flask import abort, current_app, send_from_directory

from . import main


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def serve(path):
    base = current_app.root_path

    target_path = os.path.join(base, "../react-app/build/", path)
    current_app.logger.info(target_path)

    if path == "" or path == 'index.html':
        return send_from_directory('../react-app/build', 'index.html')
    elif path != "" and os.path.exists(target_path):
        return send_from_directory('../react-app/build', path)
    else:
        return abort(404)
