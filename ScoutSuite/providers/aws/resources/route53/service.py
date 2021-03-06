from ScoutSuite.providers.aws.facade.facade import AWSFacade
from ScoutSuite.providers.aws.resources.regions import Regions
from ScoutSuite.providers.aws.resources.resources import AWSResources
from ScoutSuite.providers.utils import get_non_provider_id


class Route53Domains(AWSResources):
    async def fetch_all(self, **kwargs):
        raw_domains = await self.facade.route53.get_domains(self.scope['region'])
        for raw_domain in raw_domains:
            id, domain = self._parse_domain(raw_domain)
            self[id] = domain

    def _parse_domain(self, raw_domain):
        domain_id = get_non_provider_id(raw_domain['DomainName'])
        raw_domain['name'] = raw_domain.pop('DomainName')
        return domain_id, raw_domain


class Route53(Regions):
    _children = [
        (Route53Domains, 'domains')
    ]

    def __init__(self, facade: AWSFacade):
        super(Route53, self).__init__('route53domains', facade)
