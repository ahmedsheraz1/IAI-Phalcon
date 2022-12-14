Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'IAI Phalcon')
m.hexdigest()
'8845beae3bc199400baf01008a6e8cf71b8da534ce2a6538276789e5b5c0d85f'
