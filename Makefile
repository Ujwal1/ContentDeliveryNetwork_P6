# all: deployCDN runCDN stopCDN httpserver

# CDN: deployCDN runCDN stopCDN

# # dnsserver: src/dnsserver/dnsserver.py
# # 	chmod +x src/dnsserver/dnsserver.py
# # 	ln -sf src/dnsserver/dnsserver.py dnsserver

# # httpserver: src/httpserver/httpserver.py
# # 	chmod +x src/httpserver/httpserver.py
# # 	ln -sf src/httpserver/httpserver.py httpserver

# deployCDN:
# 	chmod +x deployCDN

# runCDN:
# 	chmod +x runCDN

# stopCDN:
# 	chmod +x stopCDN

# httpserver: 
# 	chmod +x httpserver

all: deployCDN runCDN stopCDN httpserver

deployCDN: deployCDN
	chmod +x deployCDN

runCDN: runCDN
	chmod +x runCDN

stopCDN: stopCDN
	chmod +x stopCDN

