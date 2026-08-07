from flask import jsonify


def register_routes(app):

    @app.route("/")

    def home():

        return jsonify({

            "project": "AI Safety Monitoring System",

            "status": "Running"

        })