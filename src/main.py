from vision_wrapper import VisionWrapper

print("Main is starting")


isTrain = False

# Example for using with a folder whcih contains many images
# isFolder = True
# dataset = 'dataset'

# Example for using with an image
isFolder = False
dataset = 'test_image\\5451.png'

visionWrapper = VisionWrapper(dataset, isFolder, isTrain)
classificationResult = visionWrapper.ExecuteClassification()

print("Main end.")

# import zmq

# print("Initialize connection")
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://127.0.0.1:5555")
# print("start listening...")

# while True:
#     print("Receiving message...")
#     message = socket.recv_string()
#     print(f"Received message: {message}")

#     # Perform your machine learning task here

#     print("Sending message...")
#     result = f"Processed: {message}"
#     socket.send_string(result)
#     print("Message sent")