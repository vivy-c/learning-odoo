from odoo.addons.base_rest import restapi # type: ignore
from odoo.addons.base_rest_datamodel.restapi import Datamodel # type: ignore
from odoo.addons.component.core import Component # type: ignore
import logging
_logger = logging.getLogger(__name__)

class customer_invoice(Component):
    _inherit = "base.rest.service"
    _name = "customer.invoice"
    _usage = "invoice"
    _collection = "customer.invoice.service"
    _description = """Customer Invoice Services"""

    def _res_invoice(self):
        return {
            'code': {'type': 'integer'},
            'status': {'type': 'string'},
            'message': {'type': 'string'},
        }

    @restapi.method(
    [(['/create'], 'POST')],
    input_param=Datamodel('customer.invoice.input'),
    output_param=restapi.CerberusListValidator('_res_invoice'),
    auth='api_key',
    )
    def create(self, body):
        customer_invoice = self.env['account.move']
        ticket_obj = self.env['helpdesk.ticket']
        res = []
        try:
            customer_invoice_id = customer_invoice.create({
                'invoice_date': body.invoice_date
            })
            ticket_id = ticket_obj.create({
                'name': 'body.subject',
                'description': 'body.description'
            })
            _logger.debug("======= customer_invoice_id =========")
            _logger.info(customer_invoice_id)
            res = [{
                'code': 200,
                'status': 'success'
            }]
        except Exception as e:
            res = [{
                'code': 404,
                'status': 'Failed',
                'message': str(e)
            }]
        return res
    
    def _get_invoice_list(self):
        return {
            # "invoice_date": {"type": "date"},
            "name": {"type": "string"},
        }
    
    @restapi.method(
        [(["/list"], "GET")],
        output_param=restapi.CerberusListValidator("_get_invoice_list"),
        auth="public",
    )
    def list(self):
        invoice = self.env["account.move"].search([])
        return [{"name": i.name} for i in invoice]