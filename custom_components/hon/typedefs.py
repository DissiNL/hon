from typing import Union, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
  pass

HonButtonType = Union[
    "HonButtonEntity",
    "HonDataArchive",
    "HonDeviceInfo",
]

HonEntityDescription = Union[
    "HonBinarySensorEntityDescription",
    "HonControlSwitchEntityDescription",
    "HonSwitchEntityDescription",
    "HonConfigSwitchEntityDescription",
    "HonSensorEntityDescription",
    "HonConfigSelectEntityDescription",
    "HonConfigNumberEntityDescription",
    "HonACClimateEntityDescription",
    "HonClimateEntityDescription",
    "HonNumberEntityDescription",
    "HonSelectEntityDescription",
    "HonConfigSensorEntityDescription",
    "FanEntityDescription",
    "LightEntityDescription",
    "LockEntityDescription",
    "ButtonEntityDescription",
    "SwitchEntityDescription",
    "SensorEntityDescription",
    "SelectEntityDescription",
    "NumberEntityDescription",
]

HonOptionEntityDescription = Union[
    "HonConfigSelectEntityDescription",
    "HonSelectEntityDescription",
    "HonConfigSensorEntityDescription",
    "HonSensorEntityDescription",
]

T = TypeVar(
    "T",
    "HonBinarySensorEntityDescription",
    "HonControlSwitchEntityDescription",
    "HonSwitchEntityDescription",
    "HonConfigSwitchEntityDescription",
    "HonSensorEntityDescription",
    "HonConfigSelectEntityDescription",
    "HonConfigNumberEntityDescription",
    "HonACClimateEntityDescription",
    "HonClimateEntityDescription",
    "HonNumberEntityDescription",
    "HonSelectEntityDescription",
    "HonConfigSensorEntityDescription",
    "FanEntityDescription",
    "LightEntityDescription",
    "LockEntityDescription",
    "ButtonEntityDescription",
    "SwitchEntityDescription",
    "SensorEntityDescription",
    "SelectEntityDescription",
    "NumberEntityDescription",
)
