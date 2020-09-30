import sys
sys.path.append('..')

import numpy as np
import torch
from typing import Tuple

from models.model import ResNetGenerator

class Sampler(object):
    
    @classmethod
    def sample_from_gen(cls, num_classes: int, batch_size: int, dim_z: int, label: int, device: str, gen: ResNetGenerator) \
        -> Tuple[np.ndarray, np.ndarray]:
        if label == None:
            pseudo_y = cls.__sample_pseudo_labels(num_classes, batch_size, device)
        else:
            pseudo_y = cls.__sample_pseudo_labels_const(num_classes, batch_size, label, device)
        z = cls.__sample_z(batch_size, dim_z, device)
        fake = gen(z, pseudo_y) 
        fake_img = fake.cpu().detach().numpy().transpose(0, 2, 3, 1)
        fake_img = 0.5 * fake_img + 0.5
        pseudo_y = pseudo_y.cpu().detach().numpy()
        return fake_img, pseudo_y
    
    @classmethod
    def __sample_z(cls, batch_size: int, dim_z: int, device: str) -> torch.Tensor:
        return torch.empty(batch_size, dim_z, dtype=torch.float32, device=device).normal_()

    @classmethod
    def __sample_pseudo_labels(cls, num_classes: int, batch_size: int, device: str) -> torch.LongTensor:
        pseudo_labels = torch.from_numpy(np.random.randint(low=0, high=num_classes, size=(batch_size)))
        pseudo_labels = pseudo_labels.type(torch.long).to(device)
        return pseudo_labels

    @classmethod
    def __sample_pseudo_labels_const(cls, num_classes: int, batch_size: int, label: int, device: str) -> torch.LongTensor:
        pseudo_labels = torch.ones(batch_size)*label
        pseudo_labels = pseudo_labels.type(torch.long).to(device)
        return pseudo_labels
        

