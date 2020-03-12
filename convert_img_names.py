import numpy as np
import os
from shutil import copyfile

DAVIS_DATASET_DIR = '/Volumes/MyPassport/raw_davis/DAVIS-2016/JPEGImages/480p'
NEXT_DIR = '/Volumes/MyPassport/raw_davis/flow_pairs/next'
PREV_DIR = '/Volumes/MyPassport/raw_davis/flow_pairs/prev'
TRAIN_TXT = '/Volumes/MyPassport/raw_davis/DAVIS-2016//train_seqs.txt'
VAL_TXT = '/Volumes/MyPassport/raw_davis/DAVIS-2016//val_seqs.txt'


def main():
    with open(TRAIN_TXT) as f:
        seqs = f.readlines()

    ## 图和它的前一张图
    for seq in seqs:
        if not os.path.exists(os.path.join(PREV_DIR, seq.strip())):
            os.mkdir(os.path.join(PREV_DIR, seq.strip()))
        images = np.sort(os.listdir(os.path.join(DAVIS_DATASET_DIR, seq.strip())))
        images_path = list(map(lambda x: os.path.join(DAVIS_DATASET_DIR, seq.strip(), x), images))
        i = 0
        for img_path in images_path:

            # 第一张图没prev pair
            if i == 0:
                i += 1
                continue

            # copy 这张图
            src_path = img_path
            dst_path = os.path.join(PREV_DIR, seq.strip(),
                                    os.path.basename(img_path)[:-4] + '_1' + os.path.basename(img_path)[-4:])
            copyfile(src_path, dst_path)

            # copy 前一张图
            src_path = images_path[i - 1]
            dst_path = os.path.join(PREV_DIR, seq.strip(),
                                    os.path.basename(img_path)[:-4] + '_0' + os.path.basename(img_path)[-4:])
            copyfile(src_path, dst_path)

            i += 1

    # ## 图和它的下一张图
    # for seq in seqs:
    #     if not os.path.exists(os.path.join(NEXT_DIR, seq.strip())):
    #         os.mkdir(os.path.join(NEXT_DIR, seq.strip()))
    #     images = np.sort(os.listdir(os.path.join(DAVIS_DATASET_DIR, seq.strip())))
    #     images_path = list(map(lambda x: os.path.join(DAVIS_DATASET_DIR, seq.strip(), x), images))
    #     i = 0
    #     for img_path in images_path:
    #
    #         # 最后一张图没有next pair
    #         if i == len(images_path)-1:
    #             break
    #
    #         # copy 这张图
    #         src_path = img_path
    #         dst_path = os.path.join(NEXT_DIR, seq.strip(),os.path.basename(img_path)[:-4] + '_0' + os.path.basename(img_path)[-4:])
    #         copyfile(src_path, dst_path)
    #
    #         #copy 下张图
    #         src_path = images_path[i+1]
    #         dst_path = os.path.join(NEXT_DIR, seq.strip(),os.path.basename(img_path)[:-4] + '_1' + os.path.basename(img_path)[-4:])
    #         copyfile(src_path, dst_path)
    #
    #         i += 1


if __name__ == '__main__':
    main()
