#chat application
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def listen_from_server(client):
    while True:
        msg = client.recv(2048).decode('utf-8')
        if msg != '':
            username = msg.split(':')[0]
            content = msg.split(':')[1]
            print(f'[{username}] {content}')

            
def send_msg_to_server(client):
    while True:
        msg = input('MSG: ')
        if msg != '':
            client.sendall(msg.encode())



def communicate_with_server(client):
    username = input('USERNAME: ')
    if username != '':
        client.sendall(username.encode())
    else:
        print('USERNAME CANNOT BE EMPTY.')
        exit(0)

    threading.Thread(target=listen_from_server,args =(client, )).start()
    send_msg_to_server(client)


def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((HOST,PORT))
        print('CLIENT CONNECTED SUCCESSFULLY')
        communicate_with_server(client)
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    main()