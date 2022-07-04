import base64
import hashlib
import hmac
import json
import time

import requests

from django.conf import settings


class PaymentGateWay:
    @staticmethod
    def encode_hmac(key, msg, digest_mod=hashlib.sha256):
        return hmac.new(key.encode(), msg=msg, digestmod=digest_mod).hexdigest()


class CryptoChill(PaymentGateWay):
    @staticmethod
    def get_headers(x_cc_payload, x_cc_signature, extra_headers=None):
        headers = {
            'X-CC-KEY': settings.WWT_CRYPTOCHILL_API_KEY,
            'X-CC-PAYLOAD': x_cc_payload,
            'X-CC-SIGNATURE': x_cc_signature,
        }

        if extra_headers:
            headers.update(extra_headers)

        return headers

    @staticmethod
    def api_request(endpoint, version='v1', payload=None, method='GET'):
        nonce = str(int(time.time() * 1000))
        path = '/%s/%s/' % (version, endpoint)
        payload = payload or {}

        payload.update({'request': path, 'nonce': nonce})

        encoded_payload = json.dumps(payload).encode()
        b64 = base64.b64encode(encoded_payload)

        signature = CryptoChill.encode_hmac(settings.WWT_CRYPTOCHILL_API_SECRET, b64)
        headers = CryptoChill.get_headers(b64, signature)

        response = requests.request(
            method,
            '%s%s' % (settings.WWT_CRYPTOCHILL_API_URL, path),
            headers=headers
        )

        return response.json()
