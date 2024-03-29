import argparse

parser = argparse.ArgumentParser(description='ChatRoom starter')
parser.add_argument("--server", "-s", action="store_true", default=False, help="Start server")
parser.add_argument("--client", "-c", action="store_true", default=False, help="Start client")
args = parser.parse_args()


if __name__ == "__main__":
    if args.server:
        import server
        instance = server.Server()
        
