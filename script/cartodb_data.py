from cartodb import CartoDBAPIKey, CartoDBException, FileImport

API_KEY ='YOUR_CARTODB_API_KEY'
cartodb_domain = 'YOUR_CARTODB_DOMAIN'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)

fi = FileImport("test.csv", cl)
fi.run()
