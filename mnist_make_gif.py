# encoding: utf-8

import os
import glob
# from this import d
import imageio
import argparse
import matplotlib.pyplot as plt
import numpy as np

def mk_gif(args):
    gif_dir = 'gif/%s_angle%d_grid%d/' % (args.model, args.angle, args.grid_size)
    if not os.path.isdir(gif_dir):
        os.makedirs(gif_dir)

    max_iter = 100
    for i in range(max_iter): # 100张gif图
        print('sample %d' % i)
        paths = sorted(glob.glob('image/%s_angle%d_grid%d/sample%03d_*.png' % (
            args.model, args.angle, args.grid_size, i,
        )))
        images = [np.array(plt.imread(path)*255,dtype=np.uint8) for path in paths]
        for _ in range(2): 
            images.append(images[-1]) # delay at the end #最后一张图停顿20次 
        imageio.mimsave(gif_dir + 'sample%03d.gif' % i, images, duration=1)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='unbounded_stn')
    parser.add_argument('--angle', type = int, default = 60)
    parser.add_argument('--grid_size', type = int, default = 4)
    args = parser.parse_args()
    parser.parse_args()
    
    mk_gif(args)