from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json
# import the needed packages
import imageio
import base64
import cv2
import time
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

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        # Convert to gif using the imageio.mimsave method
        # imageio.mimsave('video1.gif', image_lst)
        # start_time = time.time()
        # myclip = ImageSequenceClip(image_lst, fps=30)
        # myclip.to_gif('myClip.gif', logger=None)
        # print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()

        gif_encoded = imageio.mimsave(
            "<bytes>", image_lst, format='gif', fps=60)
        print("--- %s seconds ---" % (time.time() - start_time))
        encoded_string = gif_encoded.decode("ISO-8859-1")

        # encoded_string = base64.b64encode(gif_encoded)
        # encoded_string = b'data:image/gif;base64,'+encoded_string
        # decoded_string = encoded_string.decode()
        return {"data": encoded_string}


api.add_resource(Video, "/")

if __name__ == "__main__":
    app.run(debug=True)
