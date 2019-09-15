import argparse
import os

if __name__ == '__main__':
    #main(sys.argv[1:])
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--rfile',
        type=str,
        default='labels_cn.txt',
        help='reference file name'
    )
    parser.add_argument(
        '--sfile',
        type=str,
        default='synsets.txt',
        help='sync file name'
    )
    parser.add_argument(
        '--itree',
        type=str,
        default='',
        help='Path of folder to modify'
    )
    FLAGS, unparsed = parser.parse_known_args()
    rfile = open(FLAGS.rfile, 'rt', encoding="utf-8", errors="ignore")
    sfile = open(FLAGS.sfile, 'rt')
    rlines = [line.strip() for line in rfile]
    slines = [line.strip() for line in sfile]
    rfile.close()
    sfile.close()
    if not os.path.isdir(FLAGS.itree):
        print("Path doens't exist: " + FLAGS.itree)
        exit(-1)
    sub_dirs = []
    for dirpath, dirnames, filenames in os.walk(FLAGS.itree):
        sub_dirs.append(dirpath)
    #os.chdir(FLAGS.itree)
    for sub_dir in sub_dirs:
        if sub_dir == FLAGS.itree:
            continue
        base_name = os.path.basename(sub_dir)
        print("base_name is: " + base_name)
        idx = -1
        try:
            idx = slines.index(base_name)
        except Exception:
            continue
        if idx != -1:
            print("Index is: %d" % idx)
            new_base = rlines[idx+1]
            print("new_base is: " + new_base)
            new_dir = os.path.join(FLAGS.itree, new_base)
            os.rename(sub_dir, new_dir)

