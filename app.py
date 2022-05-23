from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api, reqparse
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from temperature_converter import TemperatureConverter

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    api = Api(app)
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"]
    )

    parser = reqparse.RequestParser()
    parser.add_argument("value")
    parser.add_argument("desired_unit")

    class ConvertTemperature(Resource):
        decorators = [limiter.limit("10/minute", override_defaults=False)]

        def post(self):
            args = parser.parse_args()
            return {
                "result": TemperatureConverter.get_conversion(
                    value=args["value"],
                    desired_unit=args["desired_unit"]
                )
            }

    api.add_resource(ConvertTemperature, "/convert/")

    @app.route("/")
    def main():
        return render_template("index.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)