"""
    cloudplayer.api.http.proxy
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by the cloudplayer team
    :license: GPL-3.0, see LICENSE for details
"""
import tornado.gen
import tornado.web

from cloudplayer.api.http import HTTPHandler


class Proxy(HTTPHandler):

    @tornado.gen.coroutine
    def proxy(self, method, provider, path, **kw):
        response = yield self.fetch(
            provider, path, method=method, params=self.query_params,
            raise_error=False, **kw)
        if response.error:
            self.set_status(response.error.code)
        yield self.write_str(response.body)

    def write_str(self, data):
        tornado.web.RequestHandler.write(self, data)
        self.finish()

    @tornado.gen.coroutine
    def get(self, provider, path):
        yield self.proxy('GET', provider, path)

    @tornado.gen.coroutine
    def post(self, provider, path):
        yield self.proxy(
            'POST', provider, path,
            body=self.request.body,
            headers={'Content-Type': 'application/json'})

    @tornado.gen.coroutine
    def put(self, provider, path):
        yield self.proxy(
            'PUT', provider, path,
            body=self.request.body,
            headers={'Content-Type': 'application/json'})

    @tornado.gen.coroutine
    def delete(self, provider, path):
        yield self.proxy('DELETE', provider, path)