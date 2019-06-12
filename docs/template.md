# iotery.io Embedded Python SDK

The python iotery.io SDK is intended to be used on your embedded device to interact with the itoery.io IoT Platform. The SDK is a fully featured wrapper for the [REST API](https://iotery.io/docs/embedded).

## Getting Started

Setup your free account on [iotery.io](https://dashboard.iotery.io) and go to your [dashboard](https://iotery.io/devices) get started with creating device types and devices.

After you get your key, install the SDK:

```bash
pip install iotery-embedded-python-sdk
```

> Note: Make sure you are using Python 3.5+!

And finally, some simple example usage:

```python
from iotery_embedded_python_sdk import Iotery
TEAM_ID="265fcb74-8889-11f9-8452-d283610663ec" # team ID found on the dashboard: https://iotery.io/system
iotery = Iotery()
d = iotery.getDeviceTokenBasic(data={"key": "thermal_sensor_001",
                                     "serial": "THERMAL_SENSOR_001", "secret": "thermal_sensor_001_secret", "teamUuid": TEAM_ID})
iotery.set_token(d["token"])
me = iotery.getMe()

print(me["name"])

```

## API

This SDK simply wraps the [REST API](https://iotery.io/docs/embedded), so more information and specifics can be found there. Since the API is a wrapper around the REST API, the syntax is standard for each of the Create, Read, Update, and Delete operations on iotery.io resources. All methods return a dictonary containing the API response. If there is an error, the method will `raise` an expection.

### Creating Resources

The generalized syntax for creating resources in iotery.io python sdk looks like:

```python
iotery.methodName(inputParameter="parameter", data={ "data": "variables" })
```

For example, to create a device, the python would look like

```python
createDeviceCommandInstanceEmbedded(
  deviceUuid="a-valid-device-type-uuid",
  commandTypeUuid="a-valid-command-type-uuid",
  data={}
)
```

where `createDeviceCommandInstanceEmbedded` maps to `methodName`, `deviceUuid` maps to `inputParameter`, and `data={}` and maps to the dictonary `{data : "variables"}` in the generalized form given above.

The available resource creation (POST) methods are

[[POSTS]]

### Reading Resources

The generalized syntax for reading (getting) resources in iotery.io python sdk looks like:

```python
iotery.methodName(inputParameter="parameter", opts={"query":"parameter"})
```

For example, to get a device by it's unique identifier `uuid`, the python would look like

```python
getDeviceTypeFirmwareRecord(
  deviceUuid="a-valid-device-uuid",
  version="valid version",
  opts={ "limit": 1 }
)
```

where `getDeviceTypeFirmwareRecord` maps to `methodName`, `deviceUuid` maps to `inputParameter`, and `{ "limit": 1 }` maps to the dictonary `{"query" : "parameters"}` in the generalized form given above.

> The `limit` option is for instructive purposes only. By definition, a `uuid` is unique and so there will never be more than one device for a given `uuid`.

The available resource creation methods are

[[GETS]]

### Updating Resources

The generalized syntax for updating resources in iotery.io python sdk looks like:

```python
iotery.methodName(inputParameter="parameter", data={ "data": "variables" })
```

For example, to update a device type, the code would look like

```python
updateDeviceChannel(
  deviceUuid="a-valid-device-type-uuid",
  channelId="1",
  data={}
)
```

where `updateDeviceChannel` maps to `methodName`, `deviceUuid` maps to `inputParameter`, and `{}` maps to the dictonary `{data : "variables"}` in the generalized form given above (if there was a body).

The available resource creation methods are

[[PATCHES]]

### Deleting Resources

The generalized syntax for reading (getting) resources in iotery.io python sdk looks like:

```python
iotery.methodName(inputParameter="parameter", opts={"query":"parameter"})
```

For example, to get a device by it's unique identifier `uuid`, the python would look like

```python
deleteDevice(
  deviceUuid="a-valid-device-uuid",
  opts={ "some": "option" }
)
```

where `deleteDevice` maps to `methodName`, `deviceUuid` maps to `inputParameter`, and `{ "some": "option" }` maps to the dictonary `{"query" : "parameters"}` in the generalized form given above.

The available resource creation methods are

[[DELETES]]

## Contributing

We welcome contributors and PRs! Let us know if you are interested.
