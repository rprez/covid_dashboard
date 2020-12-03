from flask import Blueprint

# Set up a Blueprint
admin = Blueprint('admin',
                   __name__,
                  template_folder='templates',
                   static_folder='static')


@admin.route('/admin', methods=['GET'])
def index():
    return "OK"