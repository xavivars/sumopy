import json
import logging.handlers
import requests


class Handler(logging.Handler):
    def __init__(self,
                 url,
                 host,
                 name=None,
                 compressed=False,
                 source_name=None,
                 scheme='https'
                 ):
        """
        Similar to HTTPHandler but with some custom Sumo-friendly headers
        """
        logging.Handler.__init__(self)
        self.host = host
        self.url = url
        self.name = name
        self.compressed = compressed
        self.source_name = source_name
        self.scheme = scheme
        self.endpoint = '{}://{}{}'.format(self.scheme, self.host, self.url)

    def emit(self, record):
        try:
            data = self.format(record)
            headers = self.get_headers(data)

            session = requests.Session()
            session.post(self.endpoint, headers=headers, data=data)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def get_headers(self, data):
        headers = {}
        if self.compressed:
            headers['Content-Encoding'] = 'gzip'
        if self.source_name:
            headers['X-Sumo-Name'] = self.source_name
        if self.is_json(data):
            headers['Content-Type'] = 'application/json'

        headers['Accept'] = 'application/json'

        return headers

    @staticmethod
    def is_json(data):
        try:
            json.loads(data)
            return True
        except:
            return False
