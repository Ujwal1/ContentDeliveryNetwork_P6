import socket
import requests
import math

# none of these work well, reach limit quickly

GEO_SERVICE_API_1 = 'https://ipapi.co/' # usage: GEO_SERVICE_API + ip + '/json/'
GEO_SERVICE_API_2 = 'https://freegeoip.app/json/' # usage: GEO_SERVICE_API + ip

REPLICA_SERVERS = [
    "cdn-http3.khoury.northeastern.edu", 
    "cdn-http4.khoury.northeastern.edu", 
    "cdn-http7.khoury.northeastern.edu", 
    "cdn-http11.khoury.northeastern.edu", 
    "cdn-http14.khoury.northeastern.edu", 
    "cdn-http15.khoury.northeastern.edu", 
    "cdn-http16.khoury.northeastern.edu"
]


class GeoInfo:
    def __init__(self):
        self.name_to_ip = {}
        self.ip_to_cord = {}
        self.client_to_replica = {}
    
    def get_closest_replica(self, client_ip):
        if client_ip in self.client_to_replica:
            return self.client_to_replica[client_ip]
        
        min_distance = float('inf')
        closest_server = None
        for server_name in REPLICA_SERVERS:
            # get server ip
            server_ip = self.name_to_ip.get(server_name, None)
            if not server_ip:
                server_ip = socket.gethostbyname(server_name)
                self.name_to_ip[server_name] = server_ip # cache the ip

            # get distance
            distance = self.get_distance(client_ip, server_ip)
            if distance < min_distance:
                min_distance = distance
                closest_server = server_name
        
        # cache best server
        if closest_server:
            self.client_to_replica[client_ip] = (closest_server, min_distance)
        return closest_server, min_distance
    
        
    def get_cord(self, ip):
        '''get latitude and longitude of an ip address, cache result'''
        if ip in self.ip_to_cord:
            return self.ip_to_cord[ip]
        
        # get cord from api
        res = requests.get(f'{GEO_SERVICE_API_1}{ip}/json/')
        print(f'Got response: {res.status_code}, {res.text}')
        if res.status_code != 200:
            res = requests.get(f'{GEO_SERVICE_API_2}{ip}')
        if res.status_code == 200:
            data = res.json()
            latitude, longitude = data['latitude'], data['longitude'] 
            self.ip_to_cord[ip] = (latitude, longitude) # cache cord
            return latitude, longitude
        
        print(f'Failed to get data for IP: {ip}')
        return None, None
    
    def get_distance(self, ip1, ip2):
        lat1, lon1 = self.get_cord(ip1)
        lat2, lon2 = self.get_cord(ip2)
        if lat1 and lon1 and lat2 and lon2:
            return haversine(lat1, lon1, lat2, lon2)
        return float('inf')


def haversine(lat1, lon1, lat2, lon2):
    '''get distance between two points'''
    # reference: https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/#

    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c     

