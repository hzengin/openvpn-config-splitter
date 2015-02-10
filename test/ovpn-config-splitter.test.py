import unittest
import lib.splitter as splitter
from lib.exceptions import InvalidConfigFile


class TestOpenVPNConfigSplitter(unittest.TestCase):
    def setUp(self):
        self.source = open("fixtures/client.ovpn", mode="r").read()

    # splitter should return a new valid config file which contains new entries
    def test_config_output(self):
        output = splitter.split(self.source, {})["configOutput"]
        self.assertIn("ca ca.crt", output, msg="failed: output should contain caCert entry")
        self.assertIn("cert user.crt", output, msg="failed: output should contain userCrt entry")
        self.assertIn("key private.key", output, msg="failed: output should contain privateKey entry")
        self.assertIn("tls-auth tls.key 1", output, msg="failed: output should contain tls-auth entry with direction")

    # new file contents should have correct length
    def test_parts(self):
        output = splitter.split(self.source, {})
        self.assertEqual(len(output["caCert"]), 1004, msg="caCert size is not correct")
        self.assertEqual(len(output["userCert"]), 1016, msg="userCrt size is not correct")
        self.assertEqual(len(output["privateKey"]), 1703, msg="privateKey size is not correct")
        self.assertEqual(len(output["tlsAuth"]), 650, msg="tlsAuth size is not correct")

    # splitter should raise an exception for non-valid source content
    def test_with_non_valid_content(self):
        source = "Lorem ipsum dolor sit amet,<consectetu>r </adipiscing> elit. Mauris sed"
        self.assertRaises(InvalidConfigFile, splitter.split, source=source, paths={})

