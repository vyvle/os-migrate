import traceback

try:
    import yaml  # pylint: disable=unused-import

    HAS_YAML = True
    YAML_IMPORT_ERROR = None
except ImportError:
    HAS_YAML = False
    YAML_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_YAML = True
    YAML_IMPORT_ERROR = None

try:
    import openstack  # pylint: disable=unused-import

    HAS_OPENSTACK = True
    OPENSTACK_IMPORT_ERROR = None
except ImportError:
    HAS_OPENSTACK = False
    OPENSTACK_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_OPENSTACK = True
    OPENSTACK_IMPORT_ERROR = None
