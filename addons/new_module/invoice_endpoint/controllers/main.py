from odoo.addons.base_rest.controllers import main 

class CustomerInvoiceController(main.RestController):
   _root_path = '/api/customer/'
   _collection_name = "customer.invoice.service"