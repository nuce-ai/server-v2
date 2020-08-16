import tensorflow as tf
import numpy as np 
import cv2
from utils import  label_map_util
from flask import Response, request
from flask_restful import Resource,reqparse
from werkzeug.utils import secure_filename
from PIL import Image
import json
import os
import subprocess
import base64

PATH_TO_MODEL = 'model/frozen_inference_graph.pb'
PATH_TO_LABELS = 'label/label_map.pbtxt'
NUM_CLASSES = 92

class Classifier(object):
    def __init__(self):
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            # Works up to here.
            with tf.compat.v2.io.gfile.GFile(PATH_TO_MODEL, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
            self.d_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
            self.d_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
            self.d_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
            self.num_d = self.detection_graph.get_tensor_by_name('num_detections:0')
        self.sess = tf.compat.v1.Session(graph=self.detection_graph)
    def get_classification(self, img):
    # Bounding Box Detection.
        with self.detection_graph.as_default():
            # Expand dimension since the model expects image to have shape [1, None, None, 3].
            img_expanded = np.expand_dims(img, axis=0)  
            (boxes, scores, classes, num) = self.sess.run(
                [self.d_boxes, self.d_scores, self.d_classes, self.num_d],
                feed_dict={self.image_tensor: img_expanded})
        return boxes, scores, classes, num
# init classifier 
classifier = Classifier()
# load labelmap 
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# print(categories)
# print(category_index[classes[0][0]])

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif','pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class ClassifierController(Resource):
    
    def post(self):
       file = request.files['file']
       filename = secure_filename(file.filename)
       # image_string = base64.b64encode(file.read())
       # print(image_string)
       # print(file.filename)
       # print(filename)
       if file and allowed_file(file.filename):
              upload = os.path.join('./upload/',filename)
              file.save(upload)
              wraped = cv2.imread(upload)       
              boxes,scores,classes,num = classifier.get_classification(wraped)
              return Response(json.dumps(category_index[classes[0][0]]), mimetype="application/json", status=200)
       else:
              return Response(json.dumps({"message": "upload image failed","status":"400"}), mimetype="application/json", status=400)