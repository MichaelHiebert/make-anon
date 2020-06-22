from redactme import image,faces
import cv2

import sys

if __name__ == "__main__":
    rel_filepath = sys.argv[1]
    print('Loading image...')
    frame = image.load_image_to_array(rel_filepath)
    print('Finding faces...')
    boxes = faces.get_faces_from_frame(frame)
    print('Redacting...')
    redacted = image.redact_faces(frame, boxes)
    cv2.imwrite('redacted_{}'.format(rel_filepath), redacted)
    print('Saved to {}'.format('redacted_{}'.format(rel_filepath)))