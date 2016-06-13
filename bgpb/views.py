from bgpb import app

@app.route('/')
def index():
    return '<h1>Welcome to the Brian Gillespie Personal Blog!</h1>'