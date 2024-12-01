#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()





"""
This is document for of the application for development stages only:

Admin panel credentials:
Username: lia
Email: pse.coliahabib@gmail.com
Password: 123
"""


"""
Template pages of customer_app:
1. customer_app/signup.html
2. customer_app/customer_profile.html
3. customer_app/customer_dashboard.html

Template pages of vendor_app:
1. vendor_app/vendor_signup.html
2. vendor_app/vendor_profile.html
3. vendor_dashboard.html
4. vendor_app/create_service.html

Templates pages of core_app:
1. core_app/home.html
2. core_app/service_list.html
3. core_app/service_detail.html
"""


"""
Dummy Data:
username: sakib
password: Zx1b3N+WH:rE)V4S

Vendor Data:
username: Tamim
password: NPkepzSMyV&!W12'
"""



