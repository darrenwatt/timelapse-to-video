#!/bin/python
import os
import shutil
import ffmpeg
from datetime import datetime, timedelta
from config import Config


# Requires ffmpeg installed on the host

def config_things():
    if Config.WEBCAM_PICS_DIR:
        print("WEBCAM_PICS_DIR: {}".format(Config.WEBCAM_PICS_DIR))
    else:
        print("Webcam pics directory is not set. Pass in ENVVAR WEBCAM_PICS_DIR. Exiting.")
        exit(1)

    topdir = Config.WEBCAM_PICS_DIR
    return topdir


def glue_those_images(topdir):
    print("Putting stuff together ...")


    yesterday = datetime.now() - timedelta(1) # yesterday (massive shock, james commented something!)
    datetoprocess = datetime.strftime(yesterday, '%Y/%m/%d')
    filename = datetime.strftime(yesterday,'%Y%m%d')
    filename = 'video-output'
    fileext = '.webm'
    print(datetoprocess)

    print(f'{topdir}{datetoprocess}')
    print(f'{topdir}')
    (
        ffmpeg
        .input(f'{topdir}{datetoprocess}/*.png', pattern_type='glob', framerate=25)
        .filter('deflicker',mode='pm',size=10)
        .filter('scale',size='480:270')
        .output(f'{topdir}video/{filename}{fileext}', crf=20, preset='slower', pix_fmt='yuv420p', vcodec='libvpx-vp9')
        .run()
    )

    shutil.copyfile(f'{topdir}video/{filename}{fileext}', f'{topdir}video/latest{fileext}')


if __name__ == "__main__":
    # config things
    topdir = config_things()

    # main
    glue_those_images(topdir)
