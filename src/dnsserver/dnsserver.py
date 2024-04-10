#!/usr/bin/env python3
import argparse
from dnslib.server import DNSServer, DNSLogger
from dnslib import DNSRecord, QTYPE, RR

def handle_dns_request(request):
    # Implement logic to respond to A queries for cs5700cdn.example.com
    reply = request.reply()
    qname = request.q.qname
    qtype = request.q.qtype
    if qtype == QTYPE.A and str(qname) == "cs5700cdn.example.com":
        # Respond with the IP address of the closest replica server
        # Replace 'replica_ip_address' with the actual IP address of the replica server
        reply.add_answer(RR(qname, QTYPE.A, rdata=dnslib.A("replica_ip_address")))
    return reply

def main():
    parser = argparse.ArgumentParser(description="DNS Server")
    parser.add_argument("-p", "--port", type=int, help="Port number for DNS server")
    args = parser.parse_args()

    # Create DNS server
    dns_server = DNSServer(handle_dns_request, port=args.port)
    dns_server.start_thread()

    print(f"DNS server started on port {args.port}")

    try:
        dns_server.wait()
    except KeyboardInterrupt:
        dns_server.stop()

if __name__ == "__main__":
    main()
