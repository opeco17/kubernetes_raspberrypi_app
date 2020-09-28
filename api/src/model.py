import base64

import glob


def get_encode_imgs(label, num):
    img_paths = glob.glob(f'./raw_images/{label}/*.png')[:num]

    img_bytes = []
    for img_path in img_paths:
        with open(img_path, 'rb') as f:
            img = f.read()
        img_byte = base64.b64encode(img).decode('utf-8')
        img_bytes.append(img_byte)
    return img_bytes
        