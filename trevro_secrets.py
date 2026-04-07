import node_config

# This file is where you keep secret settings, passwords, and tokens!
# If you put them in the code you risk committing that info or sharing it

secrets = {
    "ssid": "IASTATE",
    "password": "",  # Leave blank for IASTATE
    "timezone": "America/Chicago",  # http://worldtimeapi.org/timezones
    "mqtt_username": "",
    "mqtt_key": "",  # Found on Adafruit IO web portal
    "mqtt_broker": "10.26.44.131",
    "port": 1883,
    "primary_node_ip": "",
    "secondary_node_ip": "",
}

node_type = node_config.NODE_TYPE_PRIMARY
