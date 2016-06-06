# run as :: python3.4 05_*py
# then view in vlc :: file --> open network --> URL=tcp/h264://192.168.1.233:8001/

import socket
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264')
        camera.wait_recording(10)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()

