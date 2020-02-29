#!/usr/bin/env python3

try:
    from PIL import Image
    import argparse, os
    from time import sleep
except ImportError as imerr:
    print(imerr)

class msg(object):
    WHITE = u"\u001b[38;5;255m"
    BLACK = u"\u001b[38;5;0m"
    RED = u"\u001b[38;5;196m"
    GREEN = u"\u001b[38;5;40m"
    BLUE = u"\u001b[38;5;21m"
    YELLOW = u"\u001b[38;5;220m"
    MAG = u"\u001b[38;5;125m"
    BLINK = "\033[6m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    @staticmethod
    def failure(_msg, very=False):
        text = f""
        if very is True:
            text += f"{msg.RED}[+]{msg.WHITE} {_msg} {msg.RED}not found.{msg.WHITE}"
        else:
            text = f"{msg.RED}[+]{msg.WHITE} {_msg}{msg.WHITE}"
        print(text)

    @staticmethod
    def success(_msg, very=False):
        text = f""
        if very is True:
            text += f"{msg.GREEN}[+]{msg.WHITE} {_msg} {msg.GREEN}found.{msg.WHITE}"
        else:
            text = f"{msg.GREEN}[+]{msg.WHITE} {_msg}{msg.WHITE}"
        print(text)

    @staticmethod
    def warning(_msg, very=False):
        text = f""
        if very is True:
            text += f"{msg.YELLOW}[+]{msg.WHITE} {msg.YELLOW}{_msg}{msg.WHITE}"
        else:
            text = f"{msg.YELLOW}[+]{msg.WHITE} {_msg}{msg.WHITE}"
        print(text)

    @staticmethod
    def info(_msg, very=False):
        text = f""
        if very is True:
            text += f"{msg.BLUE}[+]{msg.WHITE} {msg.BLUE}{_msg}{msg.WHITE}"
        else:
            text = f"{msg.BLUE}[+]{msg.WHITE} {_msg}{msg.WHITE}"
        print(text)

def makePdf(pdfFileName, imagesList):
    sleep(1)
    msg.info('getting images information ...')
    sleep(1)
    imList = []
    f_size = Image.open(imagesList[0]).size
    for p in imagesList:
        imList.append(Image.open(p).resize(f_size))
        msg.info('adding '+repr(p)+' to PDF file.')
        sleep(2)
    msg.info('saving PDF file.')
    sleep(1)
    imList[0].save(pdfFileName, save_all=True, append_images=imList[1:])
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--images', help="Images to add, separated by ',' (coma)", required=True)
    parser.add_argument('-p', '--pdf', help='PDF File Name', required=True)
    args = parser.parse_args()

    X = [x for x in str(args.images).split(',')]
    sleep(1.5)
    msg.info('checking images existence ...')
    sleep(1)
    for ix in X:
        if os.path.exists(ix):
            msg.success(repr(ix), very=True)
        else:
            msg.failure(repr(ix), very=True)
            exit(msg.failure('please correct images path.'))
        sleep(1)
    if str(args.pdf)[-4:] != ".pdf":
        args.pdf = str(args.pdf)+'.pdf'
    
    if makePdf(args.pdf, X) is True:
        msg.success('done.')

try:
    main()
except KeyboardInterrupt:
    exit(msg.failure('Ctrl+C detected , closing ...'))
except Exception as err:
    exit(msg.failure(err))
