#!/usr/bin/env python3
import hashlib
import sys
import time

import requests

CT_URL = 'https://www.conftool.net/demo/dhdtest_26j/rest.php'

def gen_passhash(nonce, preshared):
    bytestring = f"{nonce}{preshared}".encode()
    return hashlib.sha256(bytestring).hexdigest()

def gen_nonce():
    return str(int(time.time()))

def remoteLogin_request(user, nonce, passhash):
    params = {
        'user': user,
        'page': 'remoteLogin',
        'command': 'request',
        'nonce': nonce,
        'passhash': passhash,
    }
    r = requests.get(CT_URL, params=params)
    print(r.url)
    return r.content

def adminExport_papers(nonce, passhash):
    params = {
        'page': 'adminExport',
        'export_select': 'papers',
        'form_include_deleted': '0',
        'form_export_format': 'xml',
        'cmd_create_export': 'true',
        'nonce': nonce,
        'passhash': passhash,
    }
    r = requests.get(CT_URL, params=params)
    print(r.url)
    return r.content

def downloadPaper(nonce, passhash, form_id=100, user_id=1002):
    params = {
        'page': 'downloadPaper',
        'form_id': f'{form_id}',
        'form_userID': f'{user_id}',
        'nonce': nonce,
        'passhash': passhash,
    }
    r = requests.get(CT_URL, params=params)
    print(r)
    print(r.content)
    return r.content

def main(cmd):
    user = 'gebhard'
    preshared_key = 'PF3fuZhQu'
    u_pw = 'RN_3AzHTeo'
    nonce = gen_nonce()
    ph = gen_passhash(nonce, preshared_key)

    if cmd == "user":
        content = remoteLogin_request('gebhard', nonce, ph)
    elif cmd == "papers":
        content = adminExport_papers(nonce, ph)
    elif cmd == "download":
        content = downloadPaper(nonce, ph)
    else:
        content = 'ERROR: no valid command'
    print(content)


if __name__ == '__main__':
    main(sys.argv[1])
