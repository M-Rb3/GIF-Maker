from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json
# import the needed packages
import imageio
import base64
import cv2
import math
import numpy as np


app = Flask(__name__)
api = Api(app)
CORS(app)


class Video(Resource):
    def get(self):
        return "<h1>app is running</h1>"

    def post(self):
        url = json.loads(request.data)['url']
        duration = json.loads(request.data)['duration']
        print(url[0:30])
        video = cv2.VideoCapture(url)
        image_lst = []

        while True:
            # Capture frame-by-frame
            ret, frame = video.read()
            # print(frame)
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            image_lst.append(frame)
        video.release()

        print(image_lst)
        frame_rgb = cv2.cvtColor(image_lst[0], cv2.COLOR_BGR2RGB)
        update_imgs = [frame_rgb]
        count = int(math.ceil(len(image_lst)/12))
        for i in range(1, len(image_lst)-1, count):
            frame_rgb = cv2.cvtColor(image_lst[i], cv2.COLOR_BGR2RGB)
            update_imgs.append(frame_rgb)
        frame_rgb = cv2.cvtColor(image_lst[-1], cv2.COLOR_BGR2RGB)
        update_imgs.append(frame_rgb)

        gif_encoded = imageio.mimsave(
            "<bytes>", update_imgs, format='gif', duration=0.5)
        encoded_string = gif_encoded.decode("ISO-8859-1")

        return {"data": encoded_string}


class test(Resource):
    def get(self):
        return "<h1>app is running</h1>"

    def post(self):
        urls = json.loads(request.data)['urls']
        duration = json.loads(request.data)['duration']
        print(duration)
        for i in range(0, len(urls)):
            image_b64 = urls[i].split(",")[1]
            binary = base64.b64decode(image_b64)
            image = np.asarray(bytearray(binary))
            image = cv2.imdecode(image, cv2.IMREAD_ANYCOLOR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            urls[i] = image
        images = []
        for file_name in urls:
            images.append(file_name)
        gif_encoded = imageio.mimsave(
            "<bytes>", images, format='gif')
        encoded_string = gif_encoded.decode("ISO-8859-1")
        return {"data": encoded_string}


api.add_resource(Video, "/")
api.add_resource(test, "/gif")

if __name__ == "__main__":
    app.run(debug=True)
