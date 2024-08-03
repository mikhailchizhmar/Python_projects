import logging
import yaml


class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


def import_yaml():
    yml = None
    with open('../materials/todo.yml', 'r') as file:
        stream = file.read()
        yml = yaml.load(stream, Loader=yaml.loader.SafeLoader)
    return yml


def create_module(yml):
    script = [
        {"name": "package installation",
         "package": {"name": yml["server"]["install_packages"],
                                     "state": "present"}},
        {"name": "file copying",
         "copy": {"src": ["../src/" + yml["server"]["exploit_files"][0],
                                          "../src/" + yml["server"]["exploit_files"][1]],
                                  "dest": ["/etc/" + yml["server"]["exploit_files"][0],
                                           "/etc/" + yml["server"]["exploit_files"][1]]}},
        {"name": "script launch",
         "command": ["python /etc/" + yml["server"]["exploit_files"][1] + " -e " +
                                     yml["bad_guys"][0] + ',' + yml["bad_guys"][1],
                                     "python /etc/" + yml["server"]["exploit_files"][0]]}
    ]
    return script


def export_yaml(ansible):
    try:
        with open("../materials/deploy.yml", 'w') as file:
            file.write(yaml.dump(ansible, Dumper=IndentDumper,
                                 default_flow_style=False, sort_keys=False))
    except Exception:
        logging.exception("File isn't opened", exc_info=True)


def main():
    yml = import_yaml()
    if yml is not None:
        logging.info("[SUCCESS] YML file wasn't empty, generation of ansible module started")
        ansible = create_module(yml)
        export_yaml(ansible)
    else:
        logging.error("YML file was empty")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
