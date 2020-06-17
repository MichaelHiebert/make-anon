from facenet_pytorch import MTCNN
import torch
import numpy as np
import cv2

DEVICE = 'cpu'

def get_faces_from_frame(frame):
    """
        Given a frame, return a list of bounding boxes.

        Parameters
        ----------
        frame :: height x width x channels numpy array
        
    """
    frame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)
    mtcnn = MTCNN(keep_all=True, device=DEVICE)
    # mtcnn = MTCNN(
    #     image_size=500, margin=0, min_face_size=20,
    #     thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
    #     device=DEVICE
    # )

    boxes, _ = mtcnn.detect(frame)

    return [box.tolist() for box in boxes]
