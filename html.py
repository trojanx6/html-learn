
{
  "area_code": null,
  "asn": "AS199484",
  "city": "Istanbul",
  "country_code": "TR",
  "country_name": "Turkey",
  "data": [
    {
      "_shodan": {
        "crawler": "40a81c583be35b43bfddd3126923ed489e6e2b2e",
        "id": "f77f565a-42db-4f8e-9230-d7b675ae7405",
        "module": "https",
        "options": {},
        "ptr": true,
        "region": "eu"
      },
      "asn": "AS199484",
      "cpe": [
        "cpe:/a:nginx:nginx"
      ],
      "cpe23": [
        "cpe:2.3:a:nginx:nginx"
      ],
      "data": "HTTP/1.1 404 Not Found\r\nserver: nginx\r\ndate: Fri, 31 Mar 2023 05:29:42 GMT\r\ncontent-type: text/html\r\ncontent-length: 548\r\nvary: Accept-Encoding\r\nx-content-type-options: nosniff\r\nx-xss-protection: 1; mode=block\r\nreferrer-policy: no-referrer-when-downgrade\r\nx-be-node: rdwww11\r\nstrict-transport-security: max-age=31536000; includeSubDomains; preload\r\nset-cookie: SERVERID-SAG=rdwww11; path=/; Secure\r\ncache-control: private\r\n\r\n",
      "domains": [
        "enuygun.com",
        "saglayici.net"
      ],
      "hash": 65730951,
      "hostnames": [
        "enuygun.com",
        "185-28-2-40.rdns.saglayici.net",
        "www.enuygun.com"
      ],
      "http": {
        "components": {
          "HSTS": {
            "categories": [
              "Security"
            ]
          },
          "Nginx": {
            "categories": [
              "Web servers",
              "Reverse proxies"
            ]
          }
        },
        "headers_hash": 2026481951,
        "host": "185.28.2.40",
        "html": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body>\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n",
        "html_hash": -2090962452,
        "location": "/",
        "redirects": [],
        "robots": null,
        "robots_hash": null,
        "securitytxt": null,
        "securitytxt_hash": null,
        "server": "nginx",
        "sitemap": null,
        "sitemap_hash": null,
        "status": 404,
        "title": "404 Not Found"
      },
      "ip": 3105620520,
      "ip_str": "185.28.2.40",
      "isp": "SAGLAYICI Teknoloji Bilisim Yayincilik Hiz. Ticaret Ltd. Sti.",
      "location": {
        "area_code": null,
        "city": "Istanbul",
        "country_code": "TR",
        "country_name": "Turkey",
        "latitude": 41.01384,
        "longitude": 28.94966,
        "region_code": "34"
      },
      "opts": {
        "heartbleed": "2023/03/31 05:30:19 185.28.2.40:443 - SAFE\n",
        "vulns": []
      },
      "org": "SAGLAYICI Teknoloji Bilisim Yayincilik Hiz. Ticaret Ltd. Sti.",
      "os": null,
      "port": 443,
      "ssl": {
        "acceptable_cas": [],
        "alpn": [],
        "cert": {
          "expired": false,
          "expires": "20231124235959Z",
          "extensions": [
            {
              "data": "0\\x16\\x80\\x14=\\xd3P\\xa5\\xd6\\xa0\\xad\\xee\\xf3J`\\ne\\xd3!\\xd4\\xf8\\xf8\\xd6\\x0f",
              "name": "authorityKeyIdentifier"
            },
            {
              "data": "\\x04\\x14\\x87E\\xa2\\x17\\x9d\\xea[\\xdb\\x8b\\x9fi\\x8e\\x95\\x9b#\\x0bV\\x05X\\x04",
              "name": "subjectKeyIdentifier"
            },
            {
              "data": "0\\x1e\\x82\\x0fwww.enuygun.com\\x82\\x0benuygun.com",
              "name": "subjectAltName"
            },
            {
              "critical": true,
              "data": "\\x03\\x02\\x05\\xa0",
              "name": "keyUsage"
            },
            {
              "data": "0\\x14\\x06\\x08+\\x06\\x01\\x05\\x05\\x07\\x03\\x01\\x06\\x08+\\x06\\x01\\x05\\x05\\x07\\x03\\x02",

"data": "\\x04\\x14\\x87E\\xa2\\x17\\x9d\\xea[\\xdb\\x8b\\x9fi\\x8e\\x95\\x9b#\\x0bV\\x05X\\x04",
              "name": "subjectKeyIdentifier"
            },
            {
              "data": "0\\x1e\\x82\\x0fwww.enuygun.com\\x82\\x0benuygun.com",
              "name": "subjectAltName"
            },
            {
              "critical": true,
              "data": "\\x03\\x02\\x05\\xa0",
              "name": "keyUsage"
            },
            {
              "data": "0\\x14\\x06\\x08+\\x06\\x01\\x05\\x05\\x07\\x03\\x01\\x06\\x08+\\x06\\x01\\x05\\x05\\x07\\x03\\x02",
              "nam

ame": "extendedKeyUsage"
            },
            {
              "data": "0l04\\xa02\\xa00\\x86.http://crl3.digicert.com/sha2-ev-server-g3.crl04\\xa02\\xa00\\x86.http://crl4.digicert.com/sha2-ev-server-g3.crl",
              "name": "crlDistributionPoints"
            },
            {
              "data": "0A0\\x0b\\x06\\t`\\x86H\\x01\\x86\\xfdl\\x02\\x0102\\x06\\x05g\\x81\\x0c\\x01\\x010)0\\'\\x06\\x08+\\x06\\x01\\x05\\x05\\x07\\x02\\x01\\x16\\x1bhttp://www.digicert.com/CPS",
              "name": "certificatePolicies"
            },
            {
              "data": "0z0$\\x06\\x08+\\x06\\x01\\x05\\x05\\x070\\x01\\x86\\x18http://ocsp.digicert.com0R\\x06\\x08+\\x06\\x01\\x05\\x05\\x070\\x02\\x86Fhttp://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt",
              "name": "authorityInfoAccess"
            },
            {
              "data": "0\\x00",
              "name": "basicConstraints"
            },
            {
              "data": "\\x04\\x82\\x01i\\x01g\\x00v\\x00\\xe8>\\xd0\\xda>\\xf5\\x0652\\xe7W(\\xbc\\x89k\\xc9\\x03\\xd3\\xcb\\xd1\\x11k\\xec\\xebi\\xe1w}m\\x06\\xbdn\\x00\\x00\\x01\\x84\\x08\\xd5z\\xd1\\x00\\x00\\x04\\x03\\x00G0E\\x02!\\x00\\xf2\\xde\\x87\\xffY\\xfdYR\\xf9m\\x9e\\xea\\xe6\\xc6\\xb9:C\\x92b\\xcbZ\\r!\\xe7\\x19aJU\\x0eq\\x90\\xe6\\x02 \\x01\\xdc\\x93o\\xaa\\'\\xfe\\xe3\\xf7\\xba1n\\xa3\\xcd\\x1a8E\\xaaq\\xa1\\x90\\xe4.\\xea\\x87\\xd7\\x15\\xb5\\x04\\xcd\\x19\\xdf\\x00v\\x00\\xb3sw\\x07\\xe1\\x84P\\xf8c\\x86\\xd6\\x05\\xa9\\xdc\\x11\\tJy-\\xb1g\\x0c\\x0b\\x87\\xdc\\xf0\\x03\\x0ey6\\xa5\\x9a\\x00\\x00\\x01\\x84\\x08\\xd5{P\\x00\\x00\\x04\\x03\\x00G0E\\x02!\\x00\\xb4\\x19\\x95\\xba\\x96\\xfa\\x03\\xe9\\x9et\\xcfN\\xde\\xf6\\xb3&P\\x81\\xf3l\\x885\\xe2#\\x10#\\xeap\\xbcT;\\r\\x02 Qo\\xfb\\x19\\xbc\\x1a\\x8c\\xcc;O\\xf3is[\\xaa\\x08\\xa1\\xe6\\x06p\\t\\xb4\\x16\\xfep\\xf7%)\\xe8\\x19Z#\\x00u\\x00\\xb7>\\xfb$\\xdf\\x9cM\\xbau\\xf29\\xc5\\xbaX\\xf4l]\\xfcB\\xcfz\\x9f5\\xc4\\x9e\\x1d\\t\\x81%\\xed\\xb4\\x99\\x00\\x00\\x01\\x84\\x08\\xd5{\\x1d\\x00\\x00\\x04\\x03\\x00F0D\\x02 \\x00\\xfb\\x9c\\xf64|\\xa0C}\\xb2\\x8a\\x97\\xbcos\\x91\\xccpq\\xd1\\x0fq\\xef:U\\x0e\"\\xaas:\\xa64\\x02 zB\\x1c\\xe7\\xfc\\x02\\xa8n\\xb2\\x92\\xd1\\x1a\\x97+G\\xd7F\\xe8G\\xc6\\x93\\'\\xfc\\xfd\\xc7E\\xbc\\xde\\xa4\\x9a\\x9c\\xf5",
              "name": "ct_precert_scts"
            }
          ],
          "fingerprint": {
            "sha1": "5d8848aff2171d8a44cc7e799921798ac73320f4",
            "sha256": "fb1f0331e78f8a74f17bcc154be143d505dbb63c4d7a77887b193074fe7b5184"
          },
          "issued": "20221024000000Z",
          "issuer": {
            "C": "US",
            "CN": "DigiCert SHA2 Extended Validation Server CA",
            "O": "DigiCert Inc",
            "OU": "www.digicert.com"
          },
          "pubkey": {
            "bits": 2048,
            "type": "rsa"
          },
          "serial": 20381722944494859165304560775121294461,
          "sig_alg": "sha256WithRSAEncryption",
          "subject": {
            "C": "TR",
            "CN": "www.enuygun.com",
            "L": "Ata\u015fehir",
            "O": "Enuygun Com Internet Bilgi Hizmetleri Teknoloji ve Ticaret A.S.",
            "ST": "\u0130stanbul",
            "businessCategory": "Private Organization",
            "jurisdictionC": "TR",
            "jurisdictionST": "\u0130stanbul",
            "serialNumber": "686116-0"
          },
          "version": 2
        },
        "chain": [
          "-----BEGIN CERTIFICATE-----\nMIIHdDCCBlygAwIBAgIQD1VghpdhW0KbJhoU4fNUfTANBgkqhkiG9w0BAQsFADB1\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\nd3cuZGlnaWNlcnQuY29tMTQwMgYDVQQDEytEaWdpQ2VydCBTSEEyIEV4dGVuZGVk\nIFZhbGlkYXRpb24gU2VydmVyIENBMB4XDTIyMTAyNDAwMDAwMFoXDTIzMTEyNDIz\nNTk1OVowgfwxEzARBgsrBgEEAYI3PAIBAxMCVFIxGjAYBgsrBgEEAYI3PAIBAgwJ\nxLBzdGFuYnVsMR0wGwYDVQQPDBRQcml2YXRlIE9yZ2FuaXphdGlvbjERMA8GA1UE\nBRMINjg2MTE2LTAxCzAJBgNVBAYTAlRSMRIwEAYDVQQIDAnEsHN0YW5idWwxEjAQ\nBgNVBAcMCUF0YcWfZWhpcjFIMEYGA1UEChM/RW51eWd1biBDb20gSW50ZXJuZXQg\nQmlsZ2kgSGl6bWV0bGVyaSBUZWtub2xvamkgdmUgVGljYXJldCBBLlMuMRgwFgYD\nVQ

QDEw93d3cuZW51eWd1bi5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQCz1ZidjviU3OIPq18jjqSlde5JexcHDbJzX1RWko1VZLxhJnpexYQFvbGQ\nyv6WYcAVZRGC6hIVwIOuO174cZo/zEkOM5rxkCFUxEU3k/w+DiynfwKFFTc6gza6\nnD9SHmZHUl9Me0izOb7YxQbB996QDUMg/Aj1F6r40ROisZSj/M72wbjUAPqx4L71\nFSQ4BaBoa1uAoV414cEmzoFP1tglEVySpHxy55JXV9E/Xojf8C5tG/OooBWpZqEO\nzMTtGE/jGxCe6YtxjRIZAXjLFHUt8yKlEkx28t3R/oVpMqEdjRcwGFiHOPNdKizu\n2I0RoxMdMeOoY7z3poZ8MB/eFm2JAgMBAAGjggN2MIIDcjAfBgNVHSMEGDAWgBQ9\n01Cl1qCt7vNKYApl0yHU+PjWDzAdBgNVHQ4EFgQUh0WiF53qW9uLn2mOlZsjC1YF\nWAQwJwYDVR0RBCAwHoIPd3d3LmVudXlndW4uY29tggtlbnV5Z3VuLmNvbTAOBgNV\nHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMHUGA1Ud\nHwRuMGwwNKAyoDCGLmh0dHA6Ly9jcmwzLmRpZ2ljZXJ0LmNvbS9zaGEyLWV2LXNl\ncnZlci1nMy5jcmwwNKAyoDCGLmh0dHA6Ly9jcmw0LmRpZ2ljZXJ0LmNvbS9zaGEy\nLWV2LXNlcnZlci1nMy5jcmwwSgYDVR0gBEMwQTALBglghkgBhv1sAgEwMgYFZ4EM\nAQEwKTAnBggrBgEFBQcCARYbaHR0cDovL3d3dy5kaWdpY2VydC5jb20vQ1BTMIGI\nBggrBgEFBQcBAQR8MHowJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0\nLmNvbTBSBggrBgEFBQcwAoZGaHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY29tL0Rp\nZ2lDZXJ0U0hBMkV4dGVuZGVkVmFsaWRhdGlvblNlcnZlckNBLmNydDAJBgNVHRME\nAjAAMIIBfQYKKwYBBAHWeQIEAgSCAW0EggFpAWcAdgDoPtDaPvUGNTLnVyi8iWvJ\nA9PL0RFr7Otp4Xd9bQa9bgAAAYQI1XrRAAAEAwBHMEUCIQDy3of/Wf1ZUvltnurm\nxrk6Q5Jiy1oNIecZYUpVDnGQ5gIgAdyTb6on/uP3ujFuo80aOEWqcaGQ5C7qh9cV\ntQTNGd8AdgCzc3cH4YRQ+GOG1gWp3BEJSnktsWcMC4fc8AMOeTalmgAAAYQI1XtQ\nAAAEAwBHMEUCIQC0GZW6lvoD6Z50z07e9rMmUIHzbIg14iMQI+pwvFQ7DQIgUW/7\nGbwajMw7T/Npc1uqCKHmBnAJtBb+cPclKegZWiMAdQC3Pvsk35xNunXyOcW6WPRs\nXfxCz3qfNcSeHQmBJe20mQAAAYQI1XsdAAAEAwBGMEQCIAD7nPY0fKBDfbKKl7xv\nc5HMcHHRD3HvOlUOIqpzOqY0AiB6Qhzn/AKobrKS0RqXK0fXRuhHxpMn/P3HRbze\npJqc9TANBgkqhkiG9w0BAQsFAAOCAQEAsIql3UxCOegSK8a7WjPJtzZn6fqdM75E\nQbEnVBlmzzxF7JBqxCQsiw+NVu4X06TNjiVExJWKqEmr8G9WIiKExZ7Isrb2JF+z\njq3XxVErES9Z+qQaUfynzJPjawOqAu0z9P/ajV2UBct43km6brQ9asGEfVENizHY\nVK8BRsu1EAt6YMWTmB3WXtQqL4pOHF+Iz9MM9XaASr7geK56biqJNcMRLpS8Lm8k\nXGXEEVg6ljESR3vv6jtmW3gOmWL0n1mmefKMSd//Numqm/XxNsljJpkM9AlTRk2p\nWg8AVI+01ecf0iNNpB7ozjHBeAohutra955Q9A/9ezIX/ItbM6gytg==\n-----END CERTIFICATE-----\n",
          "-----BEGIN CERTIFICATE-----\nMIIDxTCCAq2gAwIBAgIQAqxcJmoLQJuPC3nyrkYldzANBgkqhkiG9w0BAQUFADBs\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\nd3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5j\nZSBFViBSb290IENBMB4XDTA2MTExMDAwMDAwMFoXDTMxMTExMDAwMDAwMFowbDEL\nMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3\nLmRpZ2ljZXJ0LmNvbTErMCkGA1UEAxMiRGlnaUNlcnQgSGlnaCBBc3N1cmFuY2Ug\nRVYgUm9vdCBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMbM5XPm\n+9S75S0tMqbf5YE/yc0lSbZxKsPVlDRnogocsF9ppkCxxLeyj9CYpKlBWTrT3JTW\nPNt0OKRKzE0lgvdKpVMSOO7zSW1xkX5jtqumX8OkhPhPYlG++MXs2ziS4wblCJEM\nxChBVfvLWokVfnHoNb9Ncgk9vjo4UFt3MRuNs8ckRZqnrG0AFFoEt7oT61EKmEFB\nIk5lYYeBQVCmeVyJ3hlKV9Uu5l0cUyx+mM0aBhakaHPQNAQTXKFx01p8VdteZOE3\nhzBWBOURtCmAEvF5OYiiAhF8J2a3iLd48soKqDirCmTCv2ZdlYTBoSUeh10aUAsg\nEsxBu24LUTi4S8sCAwEAAaNjMGEwDgYDVR0PAQH/BAQDAgGGMA8GA1UdEwEB/wQF\nMAMBAf8wHQYDVR0OBBYEFLE+w2kD+L9HAdSYJhoIAu9jZCvDMB8GA1UdIwQYMBaA\nFLE+w2kD+L9HAdSYJhoIAu9jZCvDMA0GCSqGSIb3DQEBBQUAA4IBAQAcGgaX3Nec\nnzyIZgYIVyHbIUf4KmeqvxgydkAQV8GK83rZEWWONfqe/EW1ntlMMUu4kehDLI6z\neM7b41N5cdblIZQB2lWHmiRk9opmzN6cN82oNLFpmyPInngiK3BD41VHMWEZ71jF\nhS9OMPagMRYjyOfiZRYzy78aG6A9+MpeizGLYAiJLQwGXFK3xPkKmNEVX58Svnw2\nYzi9RKR/5CYrCsSXaQ3pjOLAEFe4yHYSkVXySGnYvCoCWw9E1CAx2/S6cCZdkGCe\nvEsXCS+0yx5DaMkHJ8HSXPfqIbloEpw8nL+e/IBcm2PN7EeqJSdnoDfzAIJ9VNep\n+OkuE6N36B9K\n-----END CERTIFICATE-----\n",
          "-----BEGIN

CERTIFICATE-----\nMIIEtjCCA56gAwIBAgIQDHmpRLCMEZUgkmFf4msdgzANBgkqhkiG9w0BAQsFADBs\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\nd3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5j\nZSBFViBSb290IENBMB4XDTEzMTAyMjEyMDAwMFoXDTI4MTAyMjEyMDAwMFowdTEL\nMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3\nLmRpZ2ljZXJ0LmNvbTE0MDIGA1UEAxMrRGlnaUNlcnQgU0hBMiBFeHRlbmRlZCBW\nYWxpZGF0aW9uIFNlcnZlciBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\nggEBANdTpARR+JmmFkhLZyeqk0nQOe0MsLAAh/FnKIaFjI5j2ryxQDji0/XspQUY\nuD0+xZkXMuwYjPrxDKZkIYXLBxA0sFKIKx9om9KxjxKws9LniB8f7zh3VF

NfgHk/\nLhqqqB5LKw2rt2O5Nbd9FLxZS99RStKh4gzikIKHaq7q12TWmFXo/a8aUGxUvBHy\n/Urynbt/DvTVvo4WiRJV2MBxNO723C3sxIclho3YIeSwTQyJ3DkmF93215SF2AQh\ncJ1vb/9cuhnhRctWVyh+HA1BV6q3uCe7seT6Ku8hI3UarS2bhjWMnHe1c63YlC3k\n8wyd7sFOYn4XwHGeLN7x+RAoGTMCAwEAAaOCAUkwggFFMBIGA1UdEwEB/wQIMAYB\nAf8CAQAwDgYDVR0PAQH/BAQDAgGGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEF\nBQcDAjA0BggrBgEFBQcBAQQoMCYwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRp\nZ2ljZXJ0LmNvbTBLBgNVHR8ERDBCMECgPqA8hjpodHRwOi8vY3JsNC5kaWdpY2Vy\ndC5jb20vRGlnaUNlcnRIaWdoQXNzdXJhbmNlRVZSb290Q0EuY3JsMD0GA1UdIAQ2\nMDQwMgYEVR0gADAqMCgGCCsGAQUFBwIBFhxodHRwczovL3d3dy5kaWdpY2VydC5j\nb20vQ1BTMB0GA1UdDgQWBBQ901Cl1qCt7vNKYApl0yHU+PjWDzAfBgNVHSMEGDAW\ngBSxPsNpA/i/RwHUmCYaCALvY2QrwzANBgkqhkiG9w0BAQsFAAOCAQEAnbbQkIbh\nhgLtxaDwNBx0wY12zIYKqPBKikLWP8ipTa18CK3mtlC4ohpNiAexKSHc59rGPCHg\n4xFJcKx6HQGkyhE6V6t9VypAdP3THYUYUN9XR3WhfVUgLkc3UHKMf4Ib0mKPLQNa\n2sPIoc4sUqIAY+tzunHISScjl2SFnjgOrWNoPLpSgVh5oywM395t6zHyuqB8bPEs\n1OG9d4Q3A84ytciagRpKkk47RpqF/oOi+Z6Mo8wNXrM9zwR4jxQUezKcxwCmXMS1\noVWNWlZopCJwqjyBcdmdqEU79OX2olHdx3ti6G8MdOu42vi/hw15UJGQmxg7kVkn\n8TUoE6smftX3eg==\n-----END CERTIFICATE-----\n"
        ],
        "chain_sha256": [
          "fb1f0331e78f8a74f17bcc154be143d505dbb63c4d7a77887b193074fe7b5184",
          "7431e5f4c3c1ce4690774f0b61e05440883ba9a01ed00ba6abd7806ed3b118cf",
          "403e062a2653059113285baf80a0d4ae422c848c9f78fad01fc94bc5b87fef1a"
        ],
        "cipher": {
          "bits": 128,
          "name": "TLS_AES_128_GCM_SHA256",
          "version": "TLSv1.3"
        },
        "dhparams": {
          "bits": 2048,
          "generator": 2,
          "prime": "ec86f870a03316ec051a7359cd1f8bf829e4d2cf52ddc2248db5389afb5ca4e4b2dace665074a6854d4b1d30b82bf310e9a72d0571e781df8b59523b5f430b68f1db07be086b1b23ee4dcc9e0e43a01edf438cecbebe90b45154b92f7b64764e5dd42eaec29eae514359c7779c503c0eed73045ff14c762ad8f8cffc3440d1b442618466423904f868b262d755ed1b747591e0c569c1315cdb7b442ece84580d1e660cc8449efd4008675dfba7768f001187e993f97dc4bc745520d44a412f43421ac1f297174927376b2f887e1ca0a1899227d9565a71c156377e3a9d05e7ee5d8f8217bce9c2933082f9f4c9ae49dbd054b4d9754dfa06b8d63841b71f77f3",
          "public_key": "112ddf59fb971734a619eb9878a50be051941203db5cabbe7046f3b7f57028a7f002090c4b21bb0cd06d13b3c0f6727438f2b34ea4881e714e6e8590a6dc6d3dd37523787c188763e2114275ae13dfca674d558c288749e60b333bd037d01c55e7aa46b81656c452652b95b166288968084cd7c0fd8019b1e16d67d7197db9db3dc9e76cdc7cd11470acb06133f9716de82c4d5ac5f4fb995ed69c4ae3fea21dd8b8ac7e713d85c0c9a319c1f2e670ef2523e8af3b23e20ce6d81adde8e384d315b74f33b117cef954c83d4215a06c4400e30bc879db977edb09716357ffbb7138cb90e2d6e74668a279ce7c5b0023a23a8968bd89bb2b55e98cdbc1b1109f83"
        },
        "handshake_states": [
          "before SSL initialization",
          "SSLv3/TLS write client hello",
          "SSLv3/TLS read server hello",
          "TLSv1.3 read encrypted extensions",
          "SSLv3/TLS read server certificate",
          "TLSv1.3 read server certificate verify",
          "SSLv3/TLS read finished",
          "SSLv3/TLS write change cipher spec",
          "SSLv3/TLS write finished",
          "SSL negotiation finished successfully"
        ],
        "ja3s": "b210411e648f206db393c31561686aea",
        "jarm": "29d29d15d29d29d00041d41d000000038eaaf490bec8dc33757f165ce01762",
        "ocsp": {},
        "tlsext": [
          {
            "id": 43,
            "name": "supported_versions"
          },
          {
            "id": 51,
            "name": "key_share"
          },
          {
            "id": 0,
            "name": "server_name"
          }
        ],
        "trust": {
          "browser": {
            "apple": true,
            "microsoft": true,
            "mozilla": true
          },
          "revoked": false
        },
        "versions": [
          "-TLSv1",
          "-SSLv2",
          "-SSLv3",
          "-TLSv1.1",
          "TLSv1.2",
          "TLSv1.3"
        ]
      },
      "timestamp": "2023-03-31T05:29:42.484162",
      "transport": "tcp"
    }
  ],
  "domains": [
    "enuygun.com",
    "saglayici.net"
  ],
  "hostnames": [

"enuygun.com",
    "185-28-2-40.rdns.saglayici.net",
    "www.enuygun.com"
  ],
  "ip": 3105620520,
  "ip_str": "185.28.2.40",
  "isp": "SAGLAYICI Teknoloji Bilisim Yayincilik Hiz. Ticaret Ltd. Sti.",
  "last_update": "2023-03-31T05:29:42.484162",
  "latitude": 41.01384,
  "longitude": 28.94966,
  "org": "SAGLAYICI Teknoloji Bilisim Yayincilik Hiz. Ticaret Ltd. Sti.",
  "os": null,
  "ports": [
    443
  ],
  "region_code": "34",
  "tags": []
}
