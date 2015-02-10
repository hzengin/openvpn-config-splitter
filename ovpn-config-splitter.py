import lib.splitter as splitter
import lib.utilities as utilities
import sys

from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description="Split OpenVPN client configuration files, create required files to import your vpn connection to Gnome")
    parser.add_argument('source', help='Source OpenVPN client configuration file')
    parser.add_argument('--output-config')
    parser.add_argument('--ca-certificate')
    parser.add_argument('--user-certificate')
    parser.add_argument('--private-key')
    parser.add_argument('--tls-auth')
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()

    paths = {
        "caCert": args.ca_certificate,
        "userCert": args.user_certificate,
        "privateKey": args.private_key,
        "tlsAuth": args.tls_auth,
        "configOutput": args.output_config,
    }
    paths = utilities.initialize_paths(paths)
    if not utilities.file_exist(args.source):
        print("Input file not found: " + args.source)
        sys.exit(2)

    if not args.overwrite:
        for path in paths.values():
            if utilities.file_exist(path):
                print("File already exists:" + path)
                sys.exit(1)

    source = open(args.source).read()
    output = splitter.split(source, paths)
    utilities.write_to_files(paths, output)
