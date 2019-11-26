import socketio
import sys

oof = 1
sio = socketio.Client()
sio.connect('http://localhost:8080')


@sio.event
def send_data(a, b):
    sio.emit('chat', {'handle': a, 'message': b})


def main():
    print("python main function")


if __name__ == '__main__':
    while oof == 1:
        name = "fuck"
        mess = input('Input message:')
        send_data(name, mess)
