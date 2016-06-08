# -*- coding: utf-8 -*-
import os
import logging
from urlparse import urljoin

import requests
import argparse

HOST = 'https://avapi.cdnzz.com'
PATH = '/video/upload'
CONFIRM_PATH = '/video/confirm'


def get_token(user, secret_key):
    """根据secret_key和user(email)获取用户上传token
    params:
        user: 用户邮箱
        secret_key: 用户secret_key
    """
    rd = {"method": "FetchToken", "secretkey": secret_key, "user": user}
    rv = requests.post('https://www.cdnzz.com/apiv3/json', data=rd)
    rv = rv.json()
    token = rv['result']['token']
    return token


def upload_video(local_file, user, path, space, token):
    """终端上传视频
    params:
        local_file: 待上传视频的full path
        user: 用户账户 email
        path: 具体文件存储路径
    """
    local_name = os.path.split(local_file)[-1]
    token = get_token(user, token)
    kw = {'user': user, 'path': path, 'space': space, 'token': token}
    files = {'file': (local_name, open(local_file, 'rb'))}
    url = urljoin(HOST, PATH)
    rv = requests.post(url, data=kw, files=files)
    print "status_code ", rv.status_code
    print "response ", rv.text


def confirm_video(user, path, token):
    token = get_token(user, token)
    kw = {'user': user, 'path': path, 'token': token}
    url = urljoin(HOST, CONFIRM_PATH)
    rv = requests.post(url, data=kw)
    print "status_code ", rv.status_code
    print "response ", rv.text


def handle_args():
    parser = argparse.ArgumentParser(description='Video upload client')
    parser.add_argument('operation', type=str, help='operation, upload or confirm.',
                        choices=['upload', 'confirm'])
    parser.add_argument('-f', '--local_file',
                        help=u'local file full path to upload')
    parser.add_argument('-u', '--user',
                        help=u'user accout email')
    parser.add_argument('-p', '--path',
                        help=u'storage path on server')
    parser.add_argument('-s', '--space',
                        help=u'space on server')
    parser.add_argument('-t', '--token',
                        help=u'user token(securt key)')

    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s# %(message)s",
                        datefmt="%Y/%m/%d-%H:%M:%S")
    args = handle_args()
    user = args.user
    path = args.path
    space = args.space
    token = args.token
    if not user:
        user = 'kim@tunegold.net'
        #user = 'lisenhe@gmail.com'
    if not token:
        token = '6f20934b4e7c31466dcf057fd4fdb964'
        #token = 'd304833048933eed8e0e2c5401ca5ec9'

    if args.operation == 'upload':
        local_file = args.local_file
        if not (local_file and path):
            print "args wrong"
            exit(0)
        upload_video(local_file, user, path, space, token)
    elif args.operation == 'confirm':
        confirm_video(user, path, token)

