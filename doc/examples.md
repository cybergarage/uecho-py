![logo](img/logo.png)

The `uecho-py` includes some sample implementations for controller and device of ECHONET Lite in the `examples` directory.

## Examples for ECHONET Lite Controller

### uechosearch

The [`uechosearch`](bin/uechosearch.py) is a sample controller to search all [ECHONET Lite][enet] nodes in the same local area network as the following usage.

```
  -h, --help     show this help message and exit
  -v, --verbose  output all mandatory read properties of found nodes
  -d, --debug    output raw debug messages
```

The [`uechosearch`](bin/uechosearch.py) searches all [ECHONET Lite][enet] device and profile objects in the local area network, and prints all found objects with the IP address as the following:

```
$ uechosearch
192.168.aaa.bbb [0] 05FF01 
192.168.aaa.cc  [0] 0F2001 [1] 029101 
```

### uechopost

The [`uechopost`](bin/uechopost.py) is a sample controller to post a message to a [ECHONET Lite][enet] node in the same local network as the following usage.


```
Usage : uechopost <address> <obj> <esv> <property (code, data) ...>
```

The [`uechopost`](bin/uechopost.py) can send any request message of [ECHONET Lite][enet] to an object in the specified node, and print the response message. The following example controls the power status of a [ECHONET Lite][enet] standard light device.

```
$ uechopost 192.168.aaa.bbb 029101 62 8A    --> READ REQ (62) : Manufacture Code (0x8A)
192.168.aaaa.bbb 0EF001 72 8A 00000B        --> READ RES (72) : Panasonic (0x00000B)

$ uechopost 192.168.aaa.bbb 029101 62 80    --> READ REQ (62) : Operation status (0x80)
192.168.aaa.bbb 029101 72 80 31             --> READ RES (72) : OFF (0x31)

$ uechopost 192.168.aaa.bbb 029101 61 80 30 --> WRITE REQ (61) : Operation status (0x80) ON (0x30)
192.168.aaa.bbb 029101 71 80                --> WRITE RES (71) : (No Data)

$ uechopost 192.168.aaa.bbb 029101 62 80    --> READ REQ (62) : Operation status (0x80)
192.168.aaa.bbb 029101 72 80 30             --> READ RES (72) : ON (0x30)
```
## Examples for ECHONET Lite Devices

### monolight

The `monolight` is an implementation example of the standard mono functional light device object which is specified in the [ECHONET Lite][enet], and the usage is below.

```
Usage : uecholight
  -h, --help     show this help message and exit
  -v, --verbose  output all mandatory read properties of found nodes
  -d, --debug    output raw debug messages
 ```

The example device object is specified as the 'Requirements for mono functional lighting class' in the Detailed Requirements
for ECHONET Device objects[\[1\]][enet-spec], and the object code is below.

- mono functional lighting class
  - Class group code : 0x02
  - Class code : 0x91
  - Instance code 0x01

# References

- \[1\] [Detailed Requirements for ECHONET Device objects][enet-spec]

[enet]:http://echonet.jp/english/
[enet-spec]:http://www.echonet.gr.jp/english/spec/index.htm
