from marshmallow import fields
# from datamodel.core import Datamodel
from odoo.addons.datamodel.core import Datamodel # type: ignore

class customer_invoice_input(Datamodel):
   _name = "customer.invoice.input"
   
   invoice_date = fields.Date(required=True)