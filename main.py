

from flask import Flask
from src.logger.logs import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    logging.info("We are thesting our logging file")
    
    return "Hello worlds"

if __name__=="__main__":
    app.run(debug=True)