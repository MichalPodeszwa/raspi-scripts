# Matrix

## Running

Everything is started as `python -m <module_name>`

### Available modules

*Listeners*:

* `listeners.bluetooth` starts Bluetooth listener module, which sends data to one of the drawers
* `listeners.web` starts json web server on 0.0.0.0:800, which sends data to one of the drawers
* `listeners.console` starts a console view waiting for you to send commands, sending it to one of the drawers

You can enable all listeners at once.

*Handlers*:

* `handlers.matrix` starts 8x8 matrix drawer.

You can only start a single handler at the same time.
