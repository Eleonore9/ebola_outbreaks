#!/home/eleonore/virtenvs/cartodb/bin/python2.7
# -*- coding: utf-8 -*-
import sys
from cartodb import CartoDBAPIKey, CartoDBException

if __name__ == "__main__":
    api_key, cartodb_domain = sys.argv[1], sys.argv[2]
    cartodb_api = CartoDBAPIKey(api_key, cartodb_domain)
    import_data = cartodb_api.req("https://" + cartodb_domain +
                                  ".cartodb.com/api/v2/sql?q=", http_method="GET",
                                  files="ebola_outbreaks_before_2014")
    import_data.run()
    print import_data.success
