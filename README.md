## occ_order_status_notification

#### Set Environment:
```
python3 env.py
```

#### Run Script
```
python3 occ_order_status_notification.py
```

#### STATUS

* APPROVED
* PENDING
* REJECTED
* REMOVED
* SENT
* DELIVERED
* READY

#### EMAIL TEMPLATE
* TEMPLATE - Order Payment Initiated
```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Order Payment Initiated Email Template</title>

</head>
<body>

      <b>MY STORE</b>
      <br>
      <br>
      Hello, <b>${data.shopper.firstName} </b>
      <br>
      <br>
      Order Status: <br>

      <#if data.orderLocation == 'APPROVED'>
          Seu pedido foi aprovado
      <#elseif data.orderLocation == 'REJECTED'>
          Pagamento reprovado
      <#elseif data.orderLocation == 'FAILED'>
          Falha no pagamento
      <#elseif data.orderLocation == 'PENDING'>
          Pagamento pendente
      <#elseif data.orderLocation == 'SENT'>
          Seu pedido foi enviado
      <#elseif data.orderLocation == 'DELIVERED'>
          Pedido entregue
      <#elseif data.orderLocation == 'REMOVED'>
          Seu pedido foi cancelado
      <#elseif data.orderLocation == 'READY'>
          Pronto para retirada
      </#if>

      <br>
      TOTAL: ${data.total}

</body>
</html>
```
