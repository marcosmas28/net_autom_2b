# Jumphost

## SSH Config for Jumphost

```
host jumphost
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes
  user root
  hostname netsim.octupus.com


host 10.2.*
  ProxyCommand ssh jumphost nc %h %p


host 10.2.*
  KexAlgorithms +diffie-hellman-group1-sha1
  Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc
  StrictHostKeyChecking no
  UserKnownHostsFile=/dev/null
  #LogLevel=quiet
```

