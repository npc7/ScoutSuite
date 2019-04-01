import os

from ScoutSuite.providers.oci.configs.services import OracleServicesConfig
from ScoutSuite.providers.base.provider import BaseProvider


class OracleProvider(BaseProvider):
    """
    Implements provider for Azure
    """

    def __init__(self,
                 report_dir=None, timestamp=None, services=None, skipped_services=None, thread_config=4, **kwargs):

        services = [] if services is None else services
        skipped_services = [] if skipped_services is None else skipped_services

        self.metadata_path = '%s/metadata.json' % os.path.split(os.path.abspath(__file__))[0]

        self.provider_code = 'oci'
        self.provider_name = 'Oracle Cloud Infrastructure'
        self.environment = 'default'

        self.services_config = OracleServicesConfig

        self.credentials = kwargs['credentials']
        self.account_id = 'TODO'  # FIXME

        super(OracleProvider, self).__init__(report_dir, timestamp, services, skipped_services, thread_config)

    def get_report_name(self):
        """
        Returns the name of the report using the provider's configuration
        """
        return 'oracle'

    def preprocessing(self, ip_ranges=None, ip_ranges_name_key=None):

        super(OracleProvider, self).preprocessing()
