from app import app
import os

host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 5000))
app.run(host=host, port=port, debug=True)
