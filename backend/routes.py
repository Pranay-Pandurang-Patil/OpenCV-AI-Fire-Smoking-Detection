from flask import jsonify, request, send_file
import cv2
import numpy as np
import os
import tempfile

from services.image_service import process_image


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "project": "AI Safety Monitoring System",
            "status": "Running"
        })

    @app.route("/detect/image", methods=["POST"])
    def detect_image():

        if "image" not in request.files:
            return jsonify({
                "error": "No image uploaded"
            }), 400

        image_file = request.files["image"]

        mode = request.form.get("mode", "fire")

        image_bytes = image_file.read()

        image_array = np.frombuffer(
            image_bytes,
            np.uint8
        )

        image = cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR
        )

        if image is None:
            return jsonify({
                "error": "Invalid image"
            }), 400

        result, count = process_image(
            mode,
            image
        )

        output_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ).name

        cv2.imwrite(
            output_path,
            result
        )

        return send_file(
            output_path,
            mimetype="image/jpeg",
            as_attachment=False
        )