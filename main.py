from make_anon import image,faces
import cv2

if __name__ == "__main__":
    frame = image.load_image_to_array('protestorig.jpg')
    boxes = faces.get_faces_from_frame(frame)
    redacted = image.redact_faces(frame, boxes)

    cv2.imwrite('redacted.jpg', redacted)

    # cv2.imshow('1', redacted)
    # cv2.waitKey(0)