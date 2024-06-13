from vision_wrapper import VisionWrapper

print("Main is starting")

# Example for inferencing with input a folder whcih contains many images
isFolder = True
dataset = 'dataset'

# Example for inferencing with input a single image
# isFolder = False
# dataset = 'test_image\\5451.png'

isTrain = False

visionWrapper = VisionWrapper(dataset, isFolder, isTrain)

classificationResult = visionWrapper.ExecuteTipQCClassification()

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