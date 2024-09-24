'''
This script encrypts images by shuffling the pixels using a key. Key is the seed of the shuffle.
'''
import os
from PIL import Image
import numpy as np
import random
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('decrypt_or_encrypt', type=str, help='Decrypt(D) or encrypt(E) the image', choices=['D', 'E'])
argparser.add_argument('image_path', type=str, help='Path to the image')
argparser.add_argument('key', type=str, help='Seed of the shuffle')
argparser.add_argument('save_path', type=str, help='Path to save the encrypted image')
args = argparser.parse_args()

def encrypt_image(image_path:str, key:int, save_path:str):
    '''
    image_path: str, path to the image
    key: int, seed of the shuffle
    save_path: str, path to save the encrypted image
    '''
    img = Image.open(image_path)
    img = np.asarray(img)
    
    shape = img.shape
    random.seed(key)
    idx = list(range(shape[0] * shape[1]))
    random.shuffle(idx)
    img = img.reshape(-1, shape[2])
    img = img[idx].reshape(shape[0], shape[1], shape[2])
    img = Image.fromarray(img)
    img.save(save_path)

def decrypt_image(image_path:str, key:int, save_path:str):
    '''
    image_path: str, path to the encrypted image
    key: int, seed of the shuffle
    save_path: str, path to save the decrypted image
    '''
    img = Image.open(image_path)
    img = np.array(img)
    shape = img.shape
    random.seed(key)
    idx = list(range(shape[0] * shape[1]))
    random.shuffle(idx)
    img = img.reshape(-1, shape[2])
    idx = sorted(range(len(idx)), key=lambda x: idx[x])
    img = img[idx].reshape(shape[0], shape[1], shape[2])
    img = Image.fromarray(img)
    img.save(save_path)

if __name__ == '__main__':
    image_path = args.image_path
    key = args.key
    save_path = args.save_path
    if args.decrypt_or_encrypt == 'E':
        encrypt_image(image_path, key, save_path)
    elif args.decrypt_or_encrypt == 'D':
        decrypt_image(image_path, key, save_path)
    else:
        exit()
    print('Done')