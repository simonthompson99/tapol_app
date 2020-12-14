import random
from app import app, db, models

@app.shell_context_processor
def make_shell_context():
    """
    allows you to run flask shell and prepare the ground with various imports
    """
    return {'db': db, 'models': models}

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)