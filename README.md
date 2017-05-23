# Example Project for Serverless Package Python Functions Plugin

This is an example project for the [Serverless Package Python Functions Plugin](https://www.npmjs.com/package/serverless-package-python-functions)

The project comprises of the below files

```
.
├── README.md
├── common_files # Service modules (common code)
│   ├── common1.py
│   └── common2.py
├── jinja2Func  # Lambda function that requires jinja2 template and common1.py
│   ├── function.py
│   └── requirements.txt # Function level requirements
├── simplejsonFunc  # Lambda function that requires simplejson library and common2.py
│   ├── function.py
│   └── requirements.txt # function level requirements
├── package.json
├── globalRequirements.txt # Service level requirements file that adds requests library to all functions
└── serverless.yml
```

# Setup
To use this example project you need
- An AWS Account and a locally configured AWS Profile named `serverless-admin`. See [here](https://serverless.com/framework/docs/providers/aws/guide/credentials/) for setup instructions

Once the account is configured, clone this repository then run serverless deploy as shown below

```
$ git clone git@github.com:ubaniabalogun/serverless-package-python-functions-demo.git
$ cd serverless-package-python-functions-demo
$ serverless deploy --verbose
```
This will deploy the test functions to your AWS environment.

The test functions simply import their packaged dependencies and return a string to confirm they work.

You can test them either by logging into the AWS Console and executing them manually, or using the Serverless CLI tool as shown below

```
$ serverless invoke --function simplejsonFunc
$ serverless invoke --function jinja2Func
```

# Cleanup
To clean up the test, run

```
$ serverless remove
```

You can learn more about the serverless-package-python-functions plugin on [NPM](https://www.npmjs.com/package/serverless-package-python-functions) or [Github](https://github.com/ubaniabalogun/serverless-package-python-functions)

May your Serverless programming be merry and fruitful.
