import dns.resolver

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

answers = dns.resolver.query(<addr>, 'PTR')
for rdata in answers:
    print(rdata)
#
from dns import resolver
from dns import reversename
addr = reversename.from_address("40.199.61.32")
resolver.query(addr, "PTR")[0]
<DNS IN PTR rdata: dfw06s16-in-f18.1e100.net.>    