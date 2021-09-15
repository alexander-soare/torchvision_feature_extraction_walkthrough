from typing import Union, Tuple

import cv2
import numpy as np


def center_crop(img: np.ndarray, crop_size: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        img - Image to be cropped
        crop_size - Size of crop. Must be smaller than or equal to the image
            size
    """
    assert (img.shape[0] >= crop_size[0]) and (img.shape[1] >= crop_size[1])
    y0 = img.shape[0] // 2 - crop_size[0] // 2
    y1 = y0 + crop_size[0]
    x0 = img.shape[1] // 2 - crop_size[1] // 2
    x1 = x0 + crop_size[1]
    return img.copy()[y0:y1, x0:x1]


def resize_shortest_edge(
        img: np.ndarray, length: int,
        interpolation: Union[int, str]=cv2.INTER_LINEAR) -> np.ndarray:
    """
    Resize image with locked aspect ratio such that its shortest side is `length`
    pixels long.
    `interpolation` specifies the cv2 interpolation type and defaults to
    cv2.INTER_LINERAR It may be specified as 'auto' in which case either
    cv2.INTER_AREA or cv2.INTERCUBIC is used depnding on whether we are
    downsizing or upsizing (respectively)
    """
    f = length/np.min(img.shape[:2])
    if isinstance(interpolation, str):
        assert interpolation == 'auto', \
            "If `interpolation` is a str it can only be 'auto'"
        interpolation = cv2.INTER_AREA if f < 1 else cv2.INTER_CUBIC
    return cv2.resize(img, (0,0), fx=f, fy=f, interpolation=interpolation)