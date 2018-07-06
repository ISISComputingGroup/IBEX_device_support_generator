""" Paths to use for template files """
from os.path import join, dirname, abspath

ROOT = dirname(abspath(__file__))
OPI = join(ROOT, "gui", "blank.opi")
EMULATOR_TEMPLATE = join(ROOT, "emulator")
DB = join(ROOT, "ioc", "basic.db")
CONFIG_XML = join(ROOT, "ioc", "config.xml")
CONFIG_XML_NOT_0 = join(ROOT, "ioc", "config_not_0.xml")
TESTS_TEMPLATE = join(ROOT, "ioc_test_framework", "tests.py")
SUPPORT_MAKEFILE = join(ROOT, "support", "Makefile")
SUPPORT_README = join(ROOT, "support", "README.md")
SUPPORT_GITIGNORE = join(ROOT, "support", ".gitignore")
