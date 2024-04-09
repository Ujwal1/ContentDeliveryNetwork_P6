.PHONY: target 

target : dnsserver httpserver

dnsserver: src/dnsserver/dnsserver.py
	chmod +x src/dnsserver/dnsserver.py
	ln -sf src/dnsserver/dnsserver.py dnsserver

httpserver: src/httpserver/httpserver.py
	chmod +x src/httpserver/httpserver.py
	ln -sf src/httpserver/httpserver.py httpserver