import unittest
from textwrap import dedent

from http_request_translator import (
    plugin_manager as pmgr,
    script
)


class TestPluginManager(unittest.TestCase):

    ###
    # plugin_manager.get_script_class
    ###
    def test_get_script_class(self):
        self.assertEqual(pmgr.get_script_class("ruby"), script.RubyScript)
        self.assertRaises(ValueError, pmgr.get_script_class, "lua")

    ###
    # plugin_manager.generate_script
    ###
    def test_generate_script(self):
        script = pmgr.generate_script(
            "bash",
            headers=["host:github.com"],
            details=dict(path="file.txt", method="GET")
        )
        result = dedent("""
            #!/usr/bin/env bash
            curl -v --request GET http://file.txt  --header "host:github.com"  --include
        """).strip()
        self.assertEqual(script, result)
