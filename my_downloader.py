# -*- coding: utf-8 -*-
# author: Rovin Yu
# Email: rovinyu@gmail.com

#from __future__ import print_function

import argparse
import os

import crawler
import downloader

def start_crawl(keywords, number, output, engine):
    crawled_urls = crawler.crawl_image_urls(keywords,
                                            engine=engine, max_number=number)
    downloader.download_images(image_urls=crawled_urls, dst_dir=output,
                               file_prefix=engine)

if __name__ == '__main__':
    #main(sys.argv[1:])
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image_dir',
        type=str,
        default='',
        help='Path to folders of labeled images.'
    )

    FLAGS, unparsed = parser.parse_known_args()
    if not os.path.isdir(FLAGS.image_dir):
        print("Path doens't exist: " + FLAGS.image_dir)
        exit(-1)
    sub_dirs = []
    for dirpath, dirnames, filenames in os.walk(FLAGS.image_dir):
        sub_dirs.append(dirpath)
    for sub_dir in sub_dirs:
        if sub_dir == FLAGS.image_dir:
            continue
        dir_name = os.path.relpath(sub_dir, FLAGS.image_dir)
        label_name = dir_name.split(os.path.sep)
        if len(label_name) > 1:
            number = len([lists for lists in os.listdir(sub_dir) if os.path.isfile(os.path.join(sub_dir, lists))])
            if number > 65:
                continue
            name = label_name[-1]
            number = 100
            engine = "Google"
            start_crawl(name, number, sub_dir, engine)
