# Proxy Switch

Test [mitmproxy](https://mitmproxy.org) via rewriting their [mitmwrapper.py example](https://github.com/mitmproxy/mitmproxy/blob/master/examples/mitmproxywrapper.py)

## Install

```sh
pip install "git+https://github.com/arnau/proxyswitch.git#egg=proxyswitch"
```


## Combo

The combo script combines the proxyswitch with a mitmproxy script so it ensures
the OS configuration is enabled when starting the proxy and it is disabled when
the proxy is stopped.

```sh
make combo
```
