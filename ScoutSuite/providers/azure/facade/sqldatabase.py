from msrestazure.azure_exceptions import CloudError

from azure.mgmt.sql import SqlManagementClient
from ScoutSuite.providers.utils import run_concurrently
from ScoutSuite.core.console import print_exception


class SQLDatabaseFacade:
    def __init__(self, credentials, subscription_id):
        self._client = SqlManagementClient(credentials, subscription_id)

    async def get_database_blob_auditing_policies(self, resource_group_name, server_name, database_name):
        try:
            return await run_concurrently(
                lambda: self._client.database_blob_auditing_policies.get(
                    resource_group_name, server_name, database_name)
            )
        except Exception as e:
            print_exception('Failed to retrieve database blob auditing policies: {}'.format(e))
            return []

    async def get_database_threat_detection_policies(self, resource_group_name, server_name, database_name):
        try:
            return await run_concurrently(
                lambda: self._client.database_threat_detection_policies.get(
                    resource_group_name, server_name, database_name)
            )
        except Exception as e:
            print_exception('Failed to retrieve database threat detection policies: {}'.format(e))
            return []

    async def get_databases(self, resource_group_name, server_name):
        try:
            return await run_concurrently(
                lambda: list(self._client.databases.list_by_server(resource_group_name, server_name))
            )
        except Exception as e:
            print_exception('Failed to retrieve databases: {}'.format(e))
            return []

    async def get_database_replication_links(self, resource_group_name, server_name, database_name):
        try:
            return await run_concurrently(
                lambda: self._client.replication_links.list_by_database(
                    resource_group_name, server_name, database_name)
            )
        except Exception as e:
            print_exception('Failed to retrieve database replication links: {}'.format(e))
            return []

    async def get_server_azure_ad_administrators(self, resource_group_name, server_name):
        try:
            return await run_concurrently(
                lambda: self._client.server_azure_ad_administrators.get(resource_group_name, server_name)
            )
        except CloudError as e:
            # No ad admin configured returns a 404 error:
            if e.status_code != 404:
                print_exception('Failed to retrieve server azure ad administrators: {}'.format(e))
        except Exception as e:
            print_exception('Failed to retrieve server azure ad administrators: {}'.format(e))
        finally:
            return []

    async def get_server_blob_auditing_policies(self, resource_group_name, server_name):
        try:
            return await run_concurrently(
                lambda: self._client.server_blob_auditing_policies.get(resource_group_name, server_name)
            )
        except Exception as e:
            print_exception('Failed to retrieve server blob auditing policies: {}'.format(e))
            return []

    async def get_server_security_alert_policies(self, resource_group_name, server_name):
        try:
            return await run_concurrently(
                lambda: self._client.server_security_alert_policies.get(resource_group_name, server_name)
            )
        except Exception as e:
            print_exception('Failed to retrieve server security alert policies: {}'.format(e))
            return []

    async def get_servers(self):
        try:
            return await run_concurrently(
                lambda: list(self._client.servers.list())
            )
        except Exception as e:
            print_exception('Failed to retrieve servers: {}'.format(e))
            return []

    async def get_database_transparent_data_encryptions(self, resource_group_name, server_name, database_name):
        try:
            return await run_concurrently(
                lambda: self._client.transparent_data_encryptions.get(
                    resource_group_name, server_name, database_name)
            )
        except Exception as e:
            print_exception('Failed to retrieve database transparent data encryptions: {}'.format(e))
            return []
