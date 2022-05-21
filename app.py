from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api, reqparse

from temperature_converter import TemperatureConverter

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    api = Api(app)

    parser = reqparse.RequestParser()
    parser.add_argument("value")
    parser.add_argument("desired_unit")

    class ConvertTemperature(Resource):
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


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)