from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json
# import the needed packages
import imageio
import base64
import cv2
import math

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
        url = json.loads(request.data)['url']
        url = url.split(",")[1].encode()
        fh = open("video.mp4", "wb")
        fh.write(base64.b64decode(url))
        fh.close()


api.add_resource(Video, "/")
api.add_resource(test, "/test")

if __name__ == "__main__":
    app.run(debug=True)
