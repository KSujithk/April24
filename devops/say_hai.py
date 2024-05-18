"""This is ansible module
"""

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # the below are module arguments
    module_args = dict(name=dict(type="str", required=True))

    result = dict(changed=False, original_message="", message="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    name = module.params["name"]
    result["original_message"] = f"Hai  {name}"
    result["message"] = f"Hai  {name}"
    result["changed"] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
