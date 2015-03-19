#!/usr/bin/env python
import os
import sys

activate_this = \
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "..", "venv-poketeambuilder", "bin", "activate_this.py"
        )
    )
execfile(activate_this, dict(__file__=activate_this))

if __name__ == "__main__":
    if "test" in sys.argv:
        settings_name = "test"
    else:
        settings_name = "development"

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "project.settings." + settings_name
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
