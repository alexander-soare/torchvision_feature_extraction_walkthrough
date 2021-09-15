import torch
import numpy as np


def prepare(img, mean, std):
    img = img / 255.
    img = img - np.array(mean)
    img = img / np.array(std)
    return torch.tensor(img).permute(2, 0, 1).unsqueeze(0).float()