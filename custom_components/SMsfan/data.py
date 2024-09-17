import SMsfan
API = SMsfan
DOMAIN = "SMsfan"
NAME_PREFIX = "smsf"
SM_MAP = {
    """
    "button": {
        "opto_cnt_rst": {
            "chan_no": 8,
            "com": {
                "set": "rstOptoCount",
            },
        }
    },
    "binary_sensor": {
        "opto": {
                "chan_no": 8,
                "uom": "",
                "com": {
                    "get": "getOptoCh",
                },
        },
    },
    "sensor":  {
        "opto_cnt": {
                "chan_no": 8,
                "uom": "",
                "com": {
                    "get": "getOptoCount",
                },
        },
        "adc": {
                "chan_no": 8,
                "uom": "V",
                "com": {
                    "get": "getAdcV",
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    },
    "switch": {
        "relay": {
                "chan_no": 8,
                "com": {
                    "get": "getRelayCh",
                    "set": "setRelayCh"
                },
        }
    },
    """
    "number": {
        "power": {
                "chan_no": 1,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 1,
                "com": {
                    #"get": "__NOGET__",
                    "get": "getPower",
                    "set": "setPower"
                },
                "icon": {
                    "on": "mdi:fan",
                    "off": "mdi:fan-off"
                }
        },
    },
}
