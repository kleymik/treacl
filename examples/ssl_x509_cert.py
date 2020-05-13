from treacl import Treacl as t

# an x509 standard encoding of an SSL certificate


def sample_ssl_certificate():

    Certificate = t()
    Certificate.Data.Version = "3 (0x2)"
    Certificate.Data.SerialNumber = "45:12:a3:02:83:5a:73:84:08:00:00:00:00:3a:95:59"
    Certificate.Data.SignatureAlgorithm = "sha256WithRSAEncryption"
    Certificate.Data.Issuer.C  = "US"
    Certificate.Data.Issuer.O  = "Google Trust Services"
    Certificate.Data.Issuer.CN = "GTS CA 1O1"
    Certificate.Data.Validity.NotBefore = "Apr 15 20:25:34 2020 GMT"
    Certificate.Data.Validity.NotAfter  = "Jul  8 20:25:34 2020 GMT"
    Certificate.Data.Subject.C  = "US"
    Certificate.Data.Subject.ST = "California"
    Certificate.Data.Subject.L  = "Mountain View"
    Certificate.Data.Subject.O  = "Google LLC"
    Certificate.Data.Subject.CN = "mail.google.com"
    Certificate.Data.Subject.PublicKeyInfo.PublicKeyAlgorithm = "id-ecPublicKey"
    Certificate.Data.Subject.PublicKeyInfo.Public_Key = "(256 bit)"
    Certificate.Data.Subject.PublicKeyInfo.pub = ("04:dd:4f:35:71:0e:56:17:73:67:ec:25:30:32:68:"
                                                   "66:75:57:be:d8:3e:c9:5d:e7:3f:30:04:bb:76:76:"
                                                   "39:7b:4e:c3:e1:c0:50:2c:9a:61:8d:b1:5b:34:15:"
                                                   "e6:12:80:d5:24:ef:84:d8:00:7d:75:00:b3:10:cf:"
                                                   "ac:9e:c7:1d:47")
    Certificate.Data.Subject.PublicKeyInfo.ASN1_OID = "prime256v1"
    Certificate.Data.Subject.PublicKeyInfo.NIST_CURVE = "P-256"
    Certificate.Data.X509v3.extensions = [t() for _ in range(13)]
    Certificate.Data.X509v3.extensions[0].X509v3KeyUsage.critical                = "Digital Signature"
    Certificate.Data.X509v3.extensions[1].X509v3ExtendedKeyUsage                 = "TLS Web Server Authentication"
    Certificate.Data.X509v3.extensions[2].X509v3BasicConstraints.critical        = "CA:FALSE"
    Certificate.Data.X509v3.extensions[3].X509v3SubjectKeyIdentifier             = "FC:DA:68:51:CF:C4:D6:F7:96:CD:F0:E8:5F:59:3D:A3:2A:E3:A1:74"
    Certificate.Data.X509v3.extensions[4].X509v3AuthorityKeyIdentifier           = "keyid:98:D1:F8:6E:10:EB:CF:9B:EC:60:9F:18:90:1B:A0:EB:7D:09:FD:2B"
    Certificate.Data.X509v3.extensions[5].AuthorityInformationAccess.OCSP        = "URI:http://ocsp.pki.goog/gts1o1"
    Certificate.Data.X509v3.extensions[6].AuthorityInformationAccess.CAIssuers   = "URI:http://pki.goog/gsr2/GTS1O1.crt"
    Certificate.Data.X509v3.extensions[7].X509v3SubjectAlternativeName           = ["DNS:mail.google.com", "DNS:inbox.google.com"]

    Certificate.Data.X509v3.extensions[8].X509v3CertificatePolicies              = [t(), t()]
    Certificate.Data.X509v3.extensions[8].X509v3CertificatePolicies[0].Policy    = "2.23.140.1.2.2"
    Certificate.Data.X509v3.extensions[8].X509v3CertificatePolicies[1].Policy    = "1.3.6.1.4.1.11129.2.5.3"

    Certificate.Data.X509v3.extensions[11].X509v3CRLDistributionPoints.FullName  = " URI:http://crl.pki.goog/GTS1O1.crl"

    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs                  = [t(), t()]
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[0].SignedCertificateTimestamp.Version    = "v1 (0x0)"
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[0].SignedCertificateTimestamp.LogID      = ("B2:1E:05:CC:8B:A2:CD:8A:20:4E:87:66:F9:2B:B9:8A:"
                                                                                                            "25:20:67:6B:DA:FA:70:E7:B2:49:53:2D:EF:8B:90:5E")
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[0].SignedCertificateTimestamp.Timestamp  = "Apr 15 21:25:34.560 2020 GMT"
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[0].SignedCertificateTimestamp.Extensions = "none"
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[0].SignedCertificateTimestamp.Signature  = ["ecdsa-with-SHA256", ("30:45:02:21:00:F3:F8:59:47:48:5B:18:50:58:05:7B:"
                                                                                                                                  "3C:44:AA:64:EA:C6:76:C1:5D:66:40:8B:B6:87:38:83:"
                                                                                                                                  "F3:3F:08:3A:22:02:20:3D:78:3B:BA:7C:97:60:58:C0:"
                                                                                                                                  "C2:CA:4A:46:C1:50:64:8D:D4:EE:0D:90:60:70:90:E1:"
                                                                                                                                  "0D:BD:24:3D:BE:37:1B")]
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[1].SignedCertificateTimestamp.Version = "v1 (0x0)"
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[1].SignedCertificateTimestamp.LogID   = ("5E:A7:73:F9:DF:56:C0:E7:B5:36:48:7D:D0:49:E0:32:"
                                                                                                         "7A:91:9A:0C:84:A1:12:12:84:18:75:96:81:71:45:58")
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[1].SignedCertificateTimestamp.Timestamp = "Apr 15 21:25:34.607 2020 GMT"
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[1].SignedCertificateTimestamp.Extensions = "none"
    Certificate.Data.X509v3.extensions[12].CTPrecertificateSCTs[1].SignedCertificateTimestamp.Signature = ["ecdsa-with-SHA256", ("30:46:02:21:00:99:31:D8:08:EB:1D:60:83:78:DC:93:"
                                                                                                                                 "F3:A9:09:E4:E2:DD:73:3C:6F:94:2A:88:DC:5E:66:E9:"
                                                                                                                                 "7B:EC:A2:6B:7C:02:21:00:C9:BE:C7:14:92:EF:53:68:"
                                                                                                                                 "61:24:22:33:F9:03:87:20:FF:4F:62:0D:EE:FF:04:E0:"
                                                                                                                                 "D2:2A:56:D5:95:16:B6:00")]
    Certificate.SignatureAlgorithm = ["sha256WithRSAEncryption", ("91:86:56:b4:b0:24:9a:dc:2c:7a:16:a4:50:52:e5:ca:e5:10:"
                                                                  "41:5f:8e:b7:71:ba:3f:d9:fd:04:57:6a:07:1b:6a:60:7c:31:"
                                                                  "fe:0a:6e:67:80:08:71:c5:ae:47:7f:0e:2e:6e:36:1b:23:8d:"
                                                                  "e6:b8:55:bd:9f:dc:0e:4f:87:da:d2:2f:e8:76:52:02:53:89:"
                                                                  "ec:78:8f:5c:01:44:2e:ff:10:89:f8:6f:78:e7:19:8f:e9:9a:"
                                                                  "3d:b1:df:4f:e5:e4:bc:e8:eb:45:55:fc:57:85:11:36:f2:2a:"
                                                                  "22:56:aa:71:2a:08:9f:c6:3e:37:76:1f:2c:59:b7:04:1a:dd:"
                                                                  "fb:59:c9:49:9f:d3:b4:48:cb:26:80:67:e2:9d:61:80:b2:cb:"
                                                                  "cd:b1:d2:12:fa:3b:b1:ca:80:7b:db:20:df:8e:53:1a:d6:1b:"
                                                                  "f0:b2:dd:cd:3a:9c:4e:16:28:8b:e7:f2:67:4f:67:d4:6e:a1:"
                                                                  "07:be:7e:4a:83:d6:fd:39:b1:26:3b:68:a9:5c:02:6f:48:e1:"
                                                                  "ff:a7:79:13:10:b4:43:9b:49:2b:79:79:f1:b5:73:6b:44:da:"
                                                                  "7e:3a:c3:1d:b5:d9:13:83:19:20:2e:97:4f:ba:27:66:a2:36:"
                                                                  "1e:59:9d:14:85:cd:3b:6a:04:f7:8b:d1:72:64:7f:e0:5d:05:"
                                                                  "a3:a7:34:c7")]
    Certificate.encoded = ["-----BEGIN CERTIFICATE-----",
                           ("MIIE1DCCA7ygAwIBAgIQRRKjAoNac4QIAAAAADqVWTANBgkqhkiG9w0BAQsFADBC"
                           "MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMRMw"
                           "EQYDVQQDEwpHVFMgQ0EgMU8xMB4XDTIwMDQxNTIwMjUzNFoXDTIwMDcwODIwMjUz"
                           "NFowaTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcT"
                           "DU1vdW50YWluIFZpZXcxEzARBgNVBAoTCkdvb2dsZSBMTEMxGDAWBgNVBAMTD21h"
                           "aWwuZ29vZ2xlLmNvbTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABN1PNXEOVhdz"
                           "Z+wlMDJoZnVXvtg+yV3nPzAEu3Z2OXtOw+HAUCyaYY2xWzQV5hKA1STvhNgAfXUA"
                           "sxDPrJ7HHUejggJoMIICZDAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAwwCgYIKwYB"
                           "BQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU/NpoUc/E1veWzfDoX1k9oyrj"
                           "oXQwHwYDVR0jBBgwFoAUmNH4bhDrz5vsYJ8YkBug630J/SswZAYIKwYBBQUHAQEE"
                           "WDBWMCcGCCsGAQUFBzABhhtodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHMxbzEwKwYI"
                           "KwYBBQUHMAKGH2h0dHA6Ly9wa2kuZ29vZy9nc3IyL0dUUzFPMS5jcnQwLAYDVR0R"
                           "BCUwI4IPbWFpbC5nb29nbGUuY29tghBpbmJveC5nb29nbGUuY29tMCEGA1UdIAQa"
                           "MBgwCAYGZ4EMAQICMAwGCisGAQQB1nkCBQMwLwYDVR0fBCgwJjAkoCKgIIYeaHR0"
                           "cDovL2NybC5wa2kuZ29vZy9HVFMxTzEuY3JsMIIBBQYKKwYBBAHWeQIEAgSB9gSB"
                           "8wDxAHYAsh4FzIuizYogTodm+Su5iiUgZ2va+nDnsklTLe+LkF4AAAFxf7ue4AAA"
                           "BAMARzBFAiEA8/hZR0hbGFBYBXs8RKpk6sZ2wV1mQIu2hziD8z8IOiICID14O7p8"
                           "l2BYwMLKSkbBUGSN1O4NkGBwkOENvSQ9vjcbAHcAXqdz+d9WwOe1Nkh90EngMnqR"
                           "mgyEoRIShBh1loFxRVgAAAFxf7ufDwAABAMASDBGAiEAmTHYCOsdYIN43JPzqQnk"
                           "4t1zPG+UKojcXmbpe+yia3wCIQDJvscUku9TaGEkIjP5A4cg/09iDe7/BODSKlbV"
                           "lRa2ADANBgkqhkiG9w0BAQsFAAOCAQEAkYZWtLAkmtwsehakUFLlyuUQQV+Ot3G6"
                           "P9n9BFdqBxtqYHwx/gpuZ4AIccWuR38OLm42GyON5rhVvZ/cDk+H2tIv6HZSAlOJ"
                           "7HiPXAFELv8QifhveOcZj+maPbHfT+XkvOjrRVX8V4URNvIqIlaqcSoIn8Y+N3Yf"
                           "LFm3BBrd+1nJSZ/TtEjLJoBn4p1hgLLLzbHSEvo7scqAe9sg345TGtYb8LLdzTqc"
                           "ThYoi+fyZ09n1G6hB75+SoPW/TmxJjtoqVwCb0jh/6d5ExC0Q5tJK3l58bVza0Ta"
                            "fjrDHbXZE4MZIC6XT7onZqI2HlmdFIXNO2oE94vRcmR/4F0Fo6c0xw=="),
                           "-----END CERTIFICATE-----"]
    return Certificate

if __name__ == '__main__':

        # https://en.wikipedia.org/wiki/X.509

    ssl_cert = '''
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            45:12:a3:02:83:5a:73:84:08:00:00:00:00:3a:95:59
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, O = Google Trust Services, CN = GTS CA 1O1
        Validity
            Not Before: Apr 15 20:25:34 2020 GMT
            Not After : Jul  8 20:25:34 2020 GMT
        Subject: C = US, ST = California, L = Mountain View, O = Google LLC, CN = mail.google.com
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:dd:4f:35:71:0e:56:17:73:67:ec:25:30:32:68:
                    66:75:57:be:d8:3e:c9:5d:e7:3f:30:04:bb:76:76:
                    39:7b:4e:c3:e1:c0:50:2c:9a:61:8d:b1:5b:34:15:
                    e6:12:80:d5:24:ef:84:d8:00:7d:75:00:b3:10:cf:
                    ac:9e:c7:1d:47
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage:
                TLS Web Server Authentication
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Subject Key Identifier:
                FC:DA:68:51:CF:C4:D6:F7:96:CD:F0:E8:5F:59:3D:A3:2A:E3:A1:74
            X509v3 Authority Key Identifier:
                keyid:98:D1:F8:6E:10:EB:CF:9B:EC:60:9F:18:90:1B:A0:EB:7D:09:FD:2B

            Authority Information Access:
                OCSP - URI:http://ocsp.pki.goog/gts1o1
                CA Issuers - URI:http://pki.goog/gsr2/GTS1O1.crt

            X509v3 Subject Alternative Name:
                DNS:mail.google.com, DNS:inbox.google.com
            X509v3 Certificate Policies:
                Policy: 2.23.140.1.2.2
                Policy: 1.3.6.1.4.1.11129.2.5.3

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.pki.goog/GTS1O1.crl

            CT Precertificate SCTs:
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : B2:1E:05:CC:8B:A2:CD:8A:20:4E:87:66:F9:2B:B9:8A:
                                25:20:67:6B:DA:FA:70:E7:B2:49:53:2D:EF:8B:90:5E
                    Timestamp : Apr 15 21:25:34.560 2020 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
                                30:45:02:21:00:F3:F8:59:47:48:5B:18:50:58:05:7B:
                                3C:44:AA:64:EA:C6:76:C1:5D:66:40:8B:B6:87:38:83:
                                F3:3F:08:3A:22:02:20:3D:78:3B:BA:7C:97:60:58:C0:
                                C2:CA:4A:46:C1:50:64:8D:D4:EE:0D:90:60:70:90:E1:
                                0D:BD:24:3D:BE:37:1B
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : 5E:A7:73:F9:DF:56:C0:E7:B5:36:48:7D:D0:49:E0:32:
                                7A:91:9A:0C:84:A1:12:12:84:18:75:96:81:71:45:58
                    Timestamp : Apr 15 21:25:34.607 2020 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
                                30:46:02:21:00:99:31:D8:08:EB:1D:60:83:78:DC:93:
                                F3:A9:09:E4:E2:DD:73:3C:6F:94:2A:88:DC:5E:66:E9:
                                7B:EC:A2:6B:7C:02:21:00:C9:BE:C7:14:92:EF:53:68:
                                61:24:22:33:F9:03:87:20:FF:4F:62:0D:EE:FF:04:E0:
                                D2:2A:56:D5:95:16:B6:00
    Signature Algorithm: sha256WithRSAEncryption
         91:86:56:b4:b0:24:9a:dc:2c:7a:16:a4:50:52:e5:ca:e5:10:
         41:5f:8e:b7:71:ba:3f:d9:fd:04:57:6a:07:1b:6a:60:7c:31:
         fe:0a:6e:67:80:08:71:c5:ae:47:7f:0e:2e:6e:36:1b:23:8d:
         e6:b8:55:bd:9f:dc:0e:4f:87:da:d2:2f:e8:76:52:02:53:89:
         ec:78:8f:5c:01:44:2e:ff:10:89:f8:6f:78:e7:19:8f:e9:9a:
         3d:b1:df:4f:e5:e4:bc:e8:eb:45:55:fc:57:85:11:36:f2:2a:
         22:56:aa:71:2a:08:9f:c6:3e:37:76:1f:2c:59:b7:04:1a:dd:
         fb:59:c9:49:9f:d3:b4:48:cb:26:80:67:e2:9d:61:80:b2:cb:
         cd:b1:d2:12:fa:3b:b1:ca:80:7b:db:20:df:8e:53:1a:d6:1b:
         f0:b2:dd:cd:3a:9c:4e:16:28:8b:e7:f2:67:4f:67:d4:6e:a1:
         07:be:7e:4a:83:d6:fd:39:b1:26:3b:68:a9:5c:02:6f:48:e1:
         ff:a7:79:13:10:b4:43:9b:49:2b:79:79:f1:b5:73:6b:44:da:
         7e:3a:c3:1d:b5:d9:13:83:19:20:2e:97:4f:ba:27:66:a2:36:
         1e:59:9d:14:85:cd:3b:6a:04:f7:8b:d1:72:64:7f:e0:5d:05:
         a3:a7:34:c7
-----BEGIN CERTIFICATE-----
MIIE1DCCA7ygAwIBAgIQRRKjAoNac4QIAAAAADqVWTANBgkqhkiG9w0BAQsFADBC
MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMRMw
EQYDVQQDEwpHVFMgQ0EgMU8xMB4XDTIwMDQxNTIwMjUzNFoXDTIwMDcwODIwMjUz
NFowaTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcT
DU1vdW50YWluIFZpZXcxEzARBgNVBAoTCkdvb2dsZSBMTEMxGDAWBgNVBAMTD21h
aWwuZ29vZ2xlLmNvbTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABN1PNXEOVhdz
Z+wlMDJoZnVXvtg+yV3nPzAEu3Z2OXtOw+HAUCyaYY2xWzQV5hKA1STvhNgAfXUA
sxDPrJ7HHUejggJoMIICZDAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAwwCgYIKwYB
BQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU/NpoUc/E1veWzfDoX1k9oyrj
oXQwHwYDVR0jBBgwFoAUmNH4bhDrz5vsYJ8YkBug630J/SswZAYIKwYBBQUHAQEE
WDBWMCcGCCsGAQUFBzABhhtodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHMxbzEwKwYI
KwYBBQUHMAKGH2h0dHA6Ly9wa2kuZ29vZy9nc3IyL0dUUzFPMS5jcnQwLAYDVR0R
BCUwI4IPbWFpbC5nb29nbGUuY29tghBpbmJveC5nb29nbGUuY29tMCEGA1UdIAQa
MBgwCAYGZ4EMAQICMAwGCisGAQQB1nkCBQMwLwYDVR0fBCgwJjAkoCKgIIYeaHR0
cDovL2NybC5wa2kuZ29vZy9HVFMxTzEuY3JsMIIBBQYKKwYBBAHWeQIEAgSB9gSB
8wDxAHYAsh4FzIuizYogTodm+Su5iiUgZ2va+nDnsklTLe+LkF4AAAFxf7ue4AAA
BAMARzBFAiEA8/hZR0hbGFBYBXs8RKpk6sZ2wV1mQIu2hziD8z8IOiICID14O7p8
l2BYwMLKSkbBUGSN1O4NkGBwkOENvSQ9vjcbAHcAXqdz+d9WwOe1Nkh90EngMnqR
mgyEoRIShBh1loFxRVgAAAFxf7ufDwAABAMASDBGAiEAmTHYCOsdYIN43JPzqQnk
4t1zPG+UKojcXmbpe+yia3wCIQDJvscUku9TaGEkIjP5A4cg/09iDe7/BODSKlbV
lRa2ADANBgkqhkiG9w0BAQsFAAOCAQEAkYZWtLAkmtwsehakUFLlyuUQQV+Ot3G6
P9n9BFdqBxtqYHwx/gpuZ4AIccWuR38OLm42GyON5rhVvZ/cDk+H2tIv6HZSAlOJ
7HiPXAFELv8QifhveOcZj+maPbHfT+XkvOjrRVX8V4URNvIqIlaqcSoIn8Y+N3Yf
LFm3BBrd+1nJSZ/TtEjLJoBn4p1hgLLLzbHSEvo7scqAe9sg345TGtYb8LLdzTqc
ThYoi+fyZ09n1G6hB75+SoPW/TmxJjtoqVwCb0jh/6d5ExC0Q5tJK3l58bVza0Ta
fjrDHbXZE4MZIC6XT7onZqI2HlmdFIXNO2oE94vRcmR/4F0Fo6c0xw==
-----END CERTIFICATE-----
'''

    print(ssl_cert)

    ct = sample_ssl_certificate()

    ct.pptree()

