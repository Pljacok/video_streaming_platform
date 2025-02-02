from flask import Flask, send_file
app = Flask(__name__)

@app.route('/video')
def stream_video():
    return send_file("video.mp4", mimetype="video/mp4")

if __name__ == '__main__':
    app.run(debug=True)
