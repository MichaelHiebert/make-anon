from redactme import image,faces
import cv2

if __name__ == "__main__":
    frame = image.load_image_to_array('assets/protest.jpg')
    boxes = faces.get_faces_from_frame(frame)
    redacted = image.redact_faces(frame, boxes)

    cv2.imwrite('assets/redacted.jpg', redacted)