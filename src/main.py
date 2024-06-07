import zmq

print("Initialize connection")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")
print("start listening...")

while True:
    print("Receiving message...")
    message = socket.recv_string()
    print(f"Received message: {message}")

    # Perform your machine learning task here

    print("Sending message...")
    result = f"Processed: {message}"
    socket.send_string(result)
    print("Message sent")
