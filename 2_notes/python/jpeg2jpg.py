#!/usr/bin/python
import os, re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='print log', action="store_true")
parser.add_argument('-r', '--recurse', help='directory recursion', action="store_true")
parser.add_argument('--dryrun', help='no file modification done', action="store_true")
parser.add_argument('--verify', help='Verify file is JPEG format', action="store_true")
parser.add_argument('--fixjpgcase', help='str.lower() to all .JPG suffixes', action="store_true")
args = parser.parse_args()
if args.verbose:
    print(args)

RE_MATCH_REGEX_JPEG = '.+\.jpeg$'
RE_MATCH_REGEX_JPG = '.+\.jpg$'
jpeg2jpg_counter = 0
files_counter = 0
directories_counter = 0
renames_counter = 0

if args.verify:
    import imghdr

def verify_jpeg(direntry):
    if (not args.verify) or (direntry.is_file() and imghdr.what(direntry.name) == 'jpeg'):
        return True
    else:
        return False

def jpeg2jpg(direntry):
    if args.verbose:
        print('# # # # # # # # # # ')
        print(direntry.name)
        global jpeg2jpg_counter
        global files_counter
        global directories_counter
        global renames_counter
        jpeg2jpg_counter += 1

    if direntry.is_file():
        if args.verbose:
            print('> is file')
            files_counter += 1

        if re.match(RE_MATCH_REGEX_JPEG, direntry.name, flags=re.IGNORECASE) and verify_jpeg(direntry):
            print('RENAMING {} --> {}jpg'.format(direntry.name, direntry.name[:-4]))
            if not args.dryrun:
                os.rename(direntry.name, '{}{}'.format(direntry.name[:-4], 'jpg'))
                if args.verbose:
                    renames_counter += 1
        elif args.fixjpgcase and re.match(RE_MATCH_REGEX_JPG, direntry.name, flags=re.IGNORECASE) and verify_jpeg(direntry):
            print('RENAMING {} --> {}jpg'.format(direntry.name, direntry.name[:-3]))
            if not args.dryrun:
                os.rename(direntry.name, '{}{}'.format(direntry.name[:-3], 'jpg'))
                if args.verbose:
                    renames_counter += 1
    elif direntry.is_dir():
        if args.verbose:
            print('> is directory')
            directories_counter += 1


if __name__ == "__main__":
    if args.recurse:
        for root, subs, files in os.walk('.'):
            for direntry in os.scandir(root):
                jpeg2jpg(direntry)
    else:
        for direntry in os.scandir():
            jpeg2jpg(direntry)

    if args.verbose:
        print('\n\n# # # # # # # # # # ')
        print('SUMMARY:')
        print('jpeg2jpg_counter {}'.format(jpeg2jpg_counter))
        print('files_counter {}'.format(files_counter))
        print('directories_counter {}'.format(directories_counter))
        print('renames_counter {}'.format(renames_counter))
