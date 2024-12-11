import os
from core import app  # Assuming 'core' is where your Flask app is defined

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from the environment variable, or default to 5000
    app.run(host='0.0.0.0', port=port)  # Listen on all network interfaces (0.0.0.0) with the correct port
