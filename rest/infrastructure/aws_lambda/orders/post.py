import sys

sys.path.insert(0, "common")

import json

import params
import clientrepo
import orderrepo
import mail
import params
import resp


def handler(event, context):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = buildResponse(status, respBody, event, context)
    else:
        clientId = params.retrieveClientId(body, event)
        productName = params.retrieveProduct(body, event)
        productVersion = params.retrieveProductVersion(body, event)
        duration = params.retrieveDuration(body, event)
        orderDate = datetime.datetime.now()

        order = order.findByClientIdProductAndProductVersion(
            clientId, productName, productVersion
        )
        if order:
            orderId = order["id"]
            orderData = json.dumps(order, indent=4, sort_keys=True, default=str)
            status = 200
            respBody = orderData
            response = resp.buildResponse(status, respBody, event, context)
            try:
                mail.send_email(
                    f"Existing order: {orderId}",
                    f"""<html>
  <body>
    <h1>Existing order requested</h1>
    <ul>
      <li>id: {orderId}</li>
      <li>clientId: {clientId}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>orderData: <pre>{orderData}</pre></li>
    </ul>
  </body>
</html>
""",
                    "html",
                )
            except:
                print(f"Error sending existing-order email")
        else:
            status = 201
            orderId = orderrepo.insert(
                clientId, productName, productVersion, duration, orderDate
            )
            respBody = {
                "orderId": orderId,
                "clientId": clientId,
                "productName": productName,
                "productVersion": productVersion,
                "duration": duration,
                "orderDate": orderDate,
            }
            response = resp.buildResponse(status, respBody, event, context)
            headers = event.get("headers", {})
            host = headers.get("host", event.get("host", ""))
            response["headers"].update({"Location": f"https://{host}/orders/{orderId}"})
            try:
                mail.send_email(
                    f"New order: {orderId}",
                    f"""<html>
  <body>
    <h1>New order: {orderId}</h1>
    <ul>
      <li>orderId: {orderId}</li>
      <li>clientId: {clientId}</li>
      <li>productName: {productName}</li>
      <li>productVersion: {productVersion}</li>
      <li>duration: {duration}</li>
      <li>orderDate: {orderDate}</li>
    </ul>
  </body>
</html>
""",
                    "html",
                )
            except:
                print(f"Error sending new-order email")

    return response
