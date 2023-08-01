# GIF-Maker - Flask REST API

GIF-Maker is a Flask-based RESTful API that allows users to create GIF animations from multiple images or a video. It provides a simple and efficient service for developers and enthusiasts who want to programmatically generate GIFs from their image collections.

## Features

- Create GIF animations from a series of images.
- Customize GIF duration, loop count, and image sequence.
- Lightweight and easy-to-use REST API.

## Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.
- Install the required dependencies by running: `pip install -r requirements.txt`

### Running the API

1. Clone this repository to your local machine.
2. Navigate to the project directory: `cd GIF-Maker`
3. Start the Flask development server: `python app.py`
4. The API will be accessible at `http://localhost:5000`.

## Usage

### Request

Send a POST request to the `/video` endpoint with the video to be used for the GIF animation.

Params:
```bash
{
    "url":"data:video/webm;base64,GkXfowEAAAAAAAAfQoaB....,
    "duration":"1"
}
```

Example using `curl`:

```bash
curl -X POST -F "video=data:video/webm;base64,GkXfowEAAAAAAAAfQoaB...." -F "duration=1" http://localhost:5000/video
```

### Request

Send a POST request to the `/images` endpoint with the images to be used for the GIF animation.

params:
```bash
{
    "url":["data:image/png;base64,GkXfowEAAAAAAAAfQoaB....","data:image/png;base64,GkXfowEAAAAAAAAfQoaB...."],
    "duration":"1"
}
```


### Response

The API will respond with a JSON object containing the URL of the generated GIF file.

Example Response:

```json
{
    "data": "data:image/gif;base64,R0lGODlhEA...."
}
```


## Customization

You can customize the GIF output by passing additional parameters in the request. Supported parameters are:

- `duration`: The duration of the GIF in seconds.


## Contributing

Contributions are welcome! If you have any feature suggestions, bug reports, or code improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
