import cv2

RECTANGLE_FILL = -1 # solid fill
BLACK = (0,0,0) # color black

def denormalize_bounding_box(image_dims, bounding_box):
    """
        Some bounding boxes are normalized, that is, they
        are given by what percentage of width/height they
        are across the screen, not necessarily how many
        pixels.

        This function converts all bounding boxes to pixels.

        Parameters
    """

    height, width, channels = image_dims

    tlx,tly,brx,bry = bounding_box

    tlx_int = int(tlx * width)
    brx_int = int(brx * width)
    tly_int = int(tly * height)
    bry_int = int(bry * height)

    return tlx_int,tly_int,brx_int,bry_int

    

def redact_faces(image, face_box_list):
    """
        Given an image and a list of face bounding boxes,
        return a new image with solid black rectangles where
        the faces used to be.

        Parameters
        ----------
        image :: height x width x channels numpy array :
            the image to redact
            
        face_box_list :: list of tuples of floats :
            list of tuples of format (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        Returns
        -------
        height x width x channels numpy array where all provided bounding boxes are black rectangles
    """

    for face_box in face_box_list:
        face_box_denorm = denormalize_bounding_box(face_box)
        top_left, bottom_right = face_box_denorm[:2], face_box_denorm[2:]
        cv2.rectangle(image, top_left, bottom_right, BLACK, thickness=RECTANGLE_FILL)

    return image