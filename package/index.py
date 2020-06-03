from package import app

@app.route('/')
def index():
    return 'package'
