## Bond Insurance

Frappe development test app

### Installation
#### Requires xmltodict

```
cd ~/frappe-bench #go to bench folder

/usr/local/bin/pip3 install xmltodict
```
 #### Get app and Install to site
 
```
bench get-app https://github.com/the-bantoo/bondinsurance.git

bench --site sitename.com install-app bondinsurance
```

#### REST API Samples

Setup REST API with [this guide](https://frappeframework.com/docs/user/en/api/rest). I'm using [Humao's REST client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for VSCode for testing.

```
GET https://sitename.com/api/resource/insurancePolicyTemplate HTTP/1.1
Accept: application/json
Authorization: token token keyapi_key:api_secret
###

GET https://sitename.com/api/resource/insurancePolicyTemplate/POLICY-2021-00008 HTTP/1.1
Accept: application/json
Authorization: token token keyapi_key:api_secret


###

POST https://sitename.com/api/method/bondinsurance.api.make_policy_entry HTTP/1.1
Content-Type: application/json
Authorization: token keyapi_key:api_secret
        
{ 
    "payload": "'first_name': 'adam'"
}
```

### License

MIT
