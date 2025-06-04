from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[{time.strftime('%H:%M:%S')}] Request from {self.client_address[0]}")
        # Simulate processing delay to mimic real server load
        time.sleep(0.1)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Server is running. Hello!")

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
