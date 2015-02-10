# openvpn-config-splitter
Splits (.ovpn) files into separate files for private key and certificates; creates an importable new (.ovpn) file for nm-connection-editor ( default GNOME network connection editor)

## Usage
```bash
python3 ovpn-config-splitter.py [-h] [--output-config OUTPUT_CONFIG]
                               [--ca-certificate CA_CERTIFICATE]
                               [--user-certificate USER_CERTIFICATE]
                               [--private-key PRIVATE_KEY]
                               [--tls-auth TLS_AUTH] [--overwrite]
                               source
```

You can also use it as a library; inspect <b>ovpn-config-splitter.py</b> for how to do that; it is simple. 
