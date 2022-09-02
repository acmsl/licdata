<!--
title: 'AWS Simple HTTP Endpoint example in Python'
description: 'This template demonstrates how to make a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework.'
layout: Doc
framework: v3
platform: AWS
language: python
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->

# licdata

## Usage

### New license

To ensure a new license (as well as the client and pc) is created, send a POST request to
https://lic.acm-sl.com/licenses , with Content-Type application/json, and the following payload:

```json
{
  "email": "[client email]",
  "product": "[product name]",
  "productVersion": "[product version]",
  "installationCode": "[installation code]",
  "description": "[pc description]"
}
```

#### Test

```bash
curl -v -X POST -d @licenses/post.json -H 'Content-Type: application/json' https://lic.acm-sl.com/licenses
```

### Check a license is valid

Similarly, the endpoint is https://lic.acm-sl.com/licenses/isValid and the payload is the same as before.

#### Test

```bash
curl -v -X POST -d @licenses/isValid.json -H 'Content-Type: application/json' https://lic.acm-sl.com/licenses/isValid
```

### Send an email

This POST endpoint, https://lic.acm-sl.com/email, uses the payload as message body.

#### Test

```bash
curl -v -X POST -d @common/mail.txt  https://lic.acm-sl.com/email
```

`
