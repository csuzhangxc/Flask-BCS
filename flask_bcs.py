# -*- coding: utf-8 -*-

import json
from urlparse import urljoin
import pybcs


class BCS(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._host = app.config.get('BCS_HOST', '')
        access_key = app.config.get('BCS_ACCESS_KEY', '')
        secret_key = app.config.get('BCS_SECRET_KEY', '')
        self._bucket_name = app.config.get('BCS_BUCKET_NAME', '')
        bcs = pybcs.BCS(self._host, access_key, secret_key)
        self._bucket = bcs.bucket(self._bucket_name)

    def save(self, data, filename, allow_referers=[]):
        filename = unicode(filename)
        if not filename.startswith('/'):
            filename = '/' + filename
        obj = self._bucket.object(filename)
        ret = obj.put(data)
        if isinstance(allow_referers, list) and allow_referers:
            # 设置允许的referer
            object_policy = {
                "statements":
                    [
                        {
                            "action": ["get_object"],
                            "effect": "allow",
                            "resource": [self._bucket_name + filename],
                            "user": ["*"],
                            "referer": allow_referers
                        }
                    ]
            }
            obj.set_acl(json.dumps(object_policy))
        else:
            # 设置为public
            obj.make_public()
        return ret

    def delete(self, filename):
        filename = unicode(filename)
        if not filename.startswith('/'):
            filename = '/' + filename
        obj = self._bucket.object(filename)
        return obj.delete()

    def url(self, filename):
        filename = unicode(filename)
        if not filename.startswith('/'):
            filename = '/' + filename
        base_url = 'http://' + self._host
        return urljoin(base_url, self._bucket_name + filename)