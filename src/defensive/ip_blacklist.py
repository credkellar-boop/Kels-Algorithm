class LocalBlacklist:
    def __init__(self):
        self._banned_ips = set()

    def add_ip(self, ip_address: str):
        self._banned_ips.add(ip_address)
        print(f"[LOCKDOWN] IP {ip_address} permanently severed from web topology.")

    def is_banned(self, ip_address: str) -> bool:
        return ip_address in self._banned_ips
      
