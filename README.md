# veritas
Veritas is a tool that validates the Credentials/Tokens.

## How to run
``` python3 veritas.py```

## Sample Request
```
import requests
data = {"tag": "slack_token", "key": "<Token>"}
res = requests.post(http://127.0.0.1:4444/credentialVerifier, json=data)
print(res.json())
------------------
output: {'status': 'False'}
```
Possible values for status:
- False (Credentials are not valid)
- True (Credentials are valid)
- unknown (Not sure)
## Currently supported tags
- slack_token
- slack_webhook
- google
- npm
- jwt



It uses the APIs mentioned in the [Keyhacks](https://github.com/streaak/keyhacks) repo. 
