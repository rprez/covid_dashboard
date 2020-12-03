from flask import  render_template

def page_not_found(e):
    return render_template('error-404.html'), 404

def internal_server_error(e):
    return render_template('error-500.html'), 500