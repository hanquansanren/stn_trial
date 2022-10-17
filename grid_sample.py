# encoding: utf-8

import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
import cv2

def vis_single(img, url):
    vis_output = img[0].detach().cpu().numpy().transpose(1,2,0) * 255 # NCHW-> NHWC (h, w, 3), dtype('float64')
    vis_output = vis_output.astype(np.uint8) # dtype('float32') -> dtype('uint8')
    cv2.imwrite(url, vis_output)

def grid_sample(input, grid, canvas = None):
    batch_num = input.size(0)
    output = F.grid_sample(input, grid, align_corners=True) # out: [64, 1, 28, 28]
    # vis_single(output,'./temp_img/mark_origin_located.png')
    if canvas is None:
        return output
    else:
        canvas = canvas.repeat(batch_num,1,1,1)
        input_mask = Variable(input.data.new(input.size()).fill_(1))        
        output_mask = F.grid_sample(input_mask, grid, align_corners=True)
        # vis_single(output_mask,'./temp_img/mark_mask.png')

        padded_output = output * output_mask + canvas * (1 - output_mask)
        # vis_single(padded_output,'./temp_img/padding_mask.png')

        return padded_output
