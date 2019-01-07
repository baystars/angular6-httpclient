# Angular6Httpclient

## Set up

generate

    $ mkdir angular6-httpclient
    $ cd angular6-httpclient
    $ ng new frontend

ng

    $ ng generate class Customer
    $ ng generate service Customer
    $ ng generate component Customer
    $ ng generate component CustomerDetails
    $ ng generate component AddCustomer
    $ ng generate module AppRouting

install bootstrap 4

    $ npm install bootstrap jquery --save

angular.json

    ...
     
    "styles": [
      "src/styles.css",
      "node_modules/bootstrap/dist/css/bootstrap.min.css"
    ],
    "scripts": [
      "node_modules/jquery/dist/jquery.min.js",
      "node_modules/bootstrap/dist/js/bootstrap.min.js"
    ]
    ...
