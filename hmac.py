import hmac,hashlib
myhmac = hmac.new(b'mykey',None,hashlib.sha256)
myhmac.update(b'dddd')
print(myhmac.hexdigest())
