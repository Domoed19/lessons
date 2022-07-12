from flask import Flask, request
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def dts(data: dict)->str:
    result = []
    for key, value in data.items():
        result.append(f"{key}: {value}")
    return ", ".join(result)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info(dts(request.form.to_dict()))
        return request.form.to_dict()
    logger.info(dts(request.args.to_dict()))
    return request.args.to_dict()


@app.route("/test/", methods=["GET"])
def test():
    return "Test URL"


if __name__ == "__main__":
    app.run()
