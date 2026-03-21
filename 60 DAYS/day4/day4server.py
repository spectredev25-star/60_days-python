#chat application
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234#port can be from 0 to 65535
LISTERNER_LIMIT = 5
connected_client = []

def msg_listener(client,username):
    while True:
        msg = client.recv(2048).decode('utf-8')
        if msg != '':
            final_msg = username + ':' + msg
            send_msg_to_all(final_msg)
def send_msg_to_client(client,msg):
    client.sendall(msg.encode())

def send_msg_to_all(msg):
    for user in connected_client:
        send_msg_to_client(user[1],msg)

def clientHandler(client):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            connected_client.append((username,client))
            print(f'{username} HAS JOINED THE CHAT')
            break
        else:
            print('USERNAME IS EMPTY.')
    threading.Thread(target=msg_listener, args=(client,username, )).start()

def main():
    #AF_INET means IPv4 address
    #SOCK_STREAM means using tcp transmission communication protocol
    #SOCK.DGRAM means using upd user datagram protocol
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        server.bind((HOST,PORT))
        print('SERVER IS RUNNING')
    except Exception as e:
        print(e)
    server.listen(LISTERNER_LIMIT)

    while True:
        client,address = server.accept()
        print(f'SUCCESSFULLY CONNECTED TO CLIENT {address[0]} {address[1]}')

        threading.Thread(target=clientHandler, args=(client, )).start()
if __name__ == '__main__':
    main()