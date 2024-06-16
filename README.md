# Content Delivery Network Implementation - ContentDeliveryNetwork_P6

Contributors: Ujwal Gupta, Shujun Chen

## High-level Approach

Our implementation consists of two main components: a DNS server and an HTTP server. The DNS server resolves domain names to IP addresses, directing client requests to the appropriate HTTP server. The HTTP server fetches and caches content from the origin server, serving it to clients upon request.

## DNS Server

### Implementation

- The DNS server is implemented in Python, utilizing the `dnslib` library for DNS message parsing and construction.
- It listens for DNS queries on a specified port and resolves domain names to IP addresses.
- To determine the best HTTP server to handle a request, it uses active measurement with Scamper to measure latency to each replica server and selects the server with the lowest latency.

### Challenges

- Implementing the DNS server required understanding the DNS protocol and message format.
- Integrating Scamper for latency measurement introduced complexity, especially in handling subprocesses and parsing command output.

## HTTP Server

### Implementation

- The HTTP server is implemented using Python's built-in `http.server` module.
- It listens for incoming HTTP requests on a specified port and fetches requested content from the origin server.
- Content caching is implemented in both memory and disk caches, using an LRU (Least Recently Used) cache eviction strategy.
- Cached content is served directly from memory or disk cache, reducing latency and load on the origin server.

### Challenges

- Managing the memory and disk caches required careful consideration of space limitations and cache eviction strategies.
- Ensuring consistency between cached content and the origin server posed challenges, especially in handling cache updates and cache expiration.

### Work Division

Shujun Chen:

- DNS server: basic struture, request handling
- HTTP server: cache management
- scripts

Projects for CS 5700 Computer Networks by Christo Wilson class, Spring 2024.

Ujwal Gupta:

- DNS server: add mechanism to find best replica server
- HTTP server: cache management
- scripts
