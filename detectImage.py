# import packages
import imutils
import numpy as np
import argparse
import cv2


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

# argument to use the tensorflow or caffe model
ap.add_argument("--method", default = "caffe", help = "Model for detection ex: caffe, tensorflow")

# Add arg for image file
ap.add_argument("--image", required=True, help = "path to image file")
args = ap.parse_args()

# LOAD MODEL
print("[INFO] loading model...")
#print(args.method)
#print(type(args.method))

# Check argument for caffe or tensorflow, then use selected model
if args.method == 'tensorflow-mobilenet':
    
    # Mobile net SSD from Tensorflow
    prtxt = "ssd_mobilenet_v1_coco_11_06_2017/ssd_mobilenet_v1_coco.pbtxt"
    model = "ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb"
      
    # Load the model
    net = cv2.dnn.readNetFromTensorflow(model, prtxt)
    
    # initialize list of classes for the tensorflow coco model
    CLASSES = { 0: 'background',
            1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
            7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
            13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
            18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
            24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
            32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
            37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
            41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
            46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
            51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
            56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
            61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
            67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
            75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
            80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
            86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush' }
  
# Incpetion tensorflow model
elif args.method == 'tensorflow-inception':
    
    # Inception SSD from Tensorflow
    prtxt = "ssd_inception_v2_coco_2017_11_17/graphFile.pbtxt"
    model = "ssd_inception_v2_coco_2017_11_17/frozen_inference_graph.pb"
      
    # Load the model
    net = cv2.dnn.readNetFromTensorflow(model, prtxt)
    
    # initialize list of classes for the tensorflow coco model
    CLASSES = { 0: 'background',
            1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
            7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
            13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
            18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
            24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
            32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
            37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
            41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
            46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
            51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
            56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
            61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
            67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
            75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
            80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
            86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush' }

elif args.method == 'caffe':
    # Mobile net SSD Model from Caffe
    prtxt = 'MobileNetSSD_deploy.prototxt.txt'
    model = 'MobileNetSSD_deploy.caffemodel' 
    
    # initialize the list of class labels MobileNet SSD was trained to
    # detect with the caffe model.
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
    
    # Load the Model
    net = cv2.dnn.readNetFromCaffe(prtxt, model)

# Custom bison detector
elif args.method == 'bison':
    
    # Get the tensorflow graph and pbtxt for bison detection
    prtxt = 'bison-detector/bison.pbtxt'
    model = 'bison-detector/frozen_inference_graph2.pb'
    
    # Load the model
    net = cv2.dnn.readNetFromTensorflow(model, prtxt)
    
    # initialize list of classes, this is just one class: bison
    CLASSES = {0: 'background', 1: 'bison'}
    

elif args.method == 'trafficSign':
    
    # Get the tensorflow graph and pbtxt for signdetection
    prtxt = 'trafficSign-detector/trafficSign.pbtxt'
    model = 'trafficSign-detector/frozen_inference_graph.pb'
    
    # Load the model
    net = cv2.dnn.readNetFromTensorflow(model, prtxt)
    
    # initialize list of classes, this is just one class: bison
    #CLASSES = {0: 'background', 1: 'Stop Sign', 2: 'Yield Sign', 3: 'Parking Sign'}
    CLASSES = {0: 'background', 1: 'Stop Sign'}

elif args.method == 'car':
    # Get the tensorflow graph and pbtxt for car detection
    prtxt = 'car-detector/car.pbtxt'
    model = 'car-detector/output_inference_graph.pb'
    
    # Load the model
    net = cv2.dnn.readNetFromTensorflow(model, prtxt)
    
    # initialize list of classes, this is just one class: bison
    CLASSES = {0: 'background', 1: 'car'}	

# Randomize some colors for each class
COLORS = np.random.uniform(0, 255, size=(len(CLASSES)+5, 3))

# Confidence threshold
conf = .2
 
# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] Reading image...")

# Read image
frame = cv2.imread(args.image)

# grab the frame dimensions and convert it to a blob
(h, w) = frame.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), (127.5, 127.5, 127.5))
 
# pass the blob through the network and obtain the detections and
# predictions
net.setInput(blob)
detections = net.forward()

# loop over the detections
for i in np.arange(0, detections.shape[2]):
	
    # extract the confidence (i.e., probability) associated with
	# the prediction
    confidence = detections[0, 0, i, 2]
 
	# filter out weak detections by ensuring confidence
	# greater than the minimum confidence
    if confidence > conf: #args["confidence"]:
	
	    # extract the index of the class label from the
	    # `detections`, then compute the (x, y)-coordinates of
        	# the bounding box for the object
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
 
	   # draw the prediction on the frame
       # print('idx: ',idx)
        label = "{}: {:.2f}%".format(CLASSES[idx],
				confidence * 100)
        cv2.rectangle(frame, (startX, startY), (endX, endY),
				COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(frame, label, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

# show the output frame
frame = imutils.resize(frame, width=800)
cv2.imshow("Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save image
cv2.imwrite('output/detectImage-output.png', frame)

