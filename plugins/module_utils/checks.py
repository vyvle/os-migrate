"""
This file centralizes the dependency check LOGIC for the os_migrate collection.
It imports status variables from dependencies.py and raises the appropriate failure.
"""

from ansible.module_utils.basic import missing_required_lib
from ansible_collections.os_migrate.os_migrate.plugins.module_utils.dependencies import (
    HAS_YAML,
    YAML_IMPORT_ERROR,
    HAS_OPENSTACK,
    OPENSTACK_IMPORT_ERROR,
)


def check_plugin_dependencies():
    """
    Checks all common dependencies for a PLUGIN.
    Raises AnsibleError if a dependency is missing.
    """

    from ansible.errors import AnsibleError

    if YAML_IMPORT_ERROR:
        raise AnsibleError(
            "yaml must be installed to use this plugin"
        ) from YAML_IMPORT_ERROR

    if OPENSTACK_IMPORT_ERROR:
        raise AnsibleError(
            "openstack must be installed to use this plugin"
        ) from OPENSTACK_IMPORT_ERROR


def check_module_dependencies(module):
    """
    Checks all common dependencies for a MODULE.
    Calls module.fail_json if a dependency is missing.
    """

    if not HAS_YAML:
        module.fail_json(msg=missing_required_lib("yaml"), exception=YAML_IMPORT_ERROR)

    if not HAS_OPENSTACK:
        module.fail_json(
            msg=missing_required_lib("openstack"), exception=OPENSTACK_IMPORT_ERROR
        )
