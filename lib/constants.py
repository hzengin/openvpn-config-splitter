defaultFileNames = {
    "caCert": "ca.crt",
    "userCert": "user.crt",
    "privateKey": "private.key",
    "tlsAuth": "tls.key",
    "configOutput": "client.new.ovpn",
}

parserMatchers = {
    "caCert": "<ca>([\s\S]*?)<\/ca>",
    "userCert": "<cert>([\s\S]*?)<\/cert>",
    "privateKey": "<key>([\s\S]*?)<\/key>",
    "tlsAuth": "<tls-auth>([\s\S]*?)<\/tls-auth>",
}

keyDirMatcher = "key-direction\s+([10])"

textToInsertRefs = {
    "caCert": "ca",
    "userCert": "cert",
    "privateKey": "key",
    "tlsAuth": "tls-auth",
}

insertLocationMatcher = "(## -----BEGIN \w+ SIGNATURE-----)"


