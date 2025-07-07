import json
import ldap3
import asyncio
from ldap3 import Server, Connection, AUTO_BIND_NO_TLS, SUBTREE, BASE, ALL_ATTRIBUTES, ObjectDef, AttrDef, Reader, Entry, Attribute, OperationalAttribute
from walkoff_app_sdk.app_base import AppBase


class ADLDAP(AppBase):
    __version__ = "1.0.0"
    app_name = "AD LDAP"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    # Write your data inside this function
    def search_samaccountname(self, domain_name, server_name, user_name, password, samaccountname, search_base, port, use_ssl):

        user = '{}\\{}'.format(domain_name, user_name)
        port = int(port)
        use_ssl = False if use_ssl.lower() == "false" else True

        conn = Connection(Server(server_name, port=port, use_ssl=use_ssl), auto_bind=AUTO_BIND_NO_TLS, user=user, password=password)

        print(conn,
            search_base,
            sep='\n')

        conn.search(
            search_base=search_base,
            search_filter=f'(samAccountName={samaccountname})',
            attributes=ALL_ATTRIBUTES
        )

        return json.loads(conn.response_to_json())['entries']

if __name__ == "__main__":
    ADLDAP.run()
