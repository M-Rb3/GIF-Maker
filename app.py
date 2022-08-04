from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json

# import the needed packages
import imageio
import base64
import cv2

app = Flask(__name__)
api = Api(app)
CORS(app)


class Video(Resource):
    def get(self):
        return "<h1>app is running</h1>"

    def post(self):
        url = json.loads(request.data)['url']
        cap = cv2.VideoCapture(url)
        image_lst = []

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_lst.append(frame_rgb)

            # cv2.imshow('a', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        # Convert to gif using the imageio.mimsave method
        # imageio.mimsave('video1.gif', image_lst)
        gif_encoded = imageio.mimsave("<bytes>", image_lst, format='gif')
        encoded_string = base64.b64encode(gif_encoded)
        encoded_string = b'data:image/gif;base64,'+encoded_string
        decoded_string = encoded_string.decode()
        return {"data": decoded_string}


api.add_resource(Video, "/")

if __name__ == "__main__":
    app.run(debug=True)
