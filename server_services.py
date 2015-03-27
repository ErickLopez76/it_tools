from openerp import models, fields, api

class server_services(models.Model):
    _name = "ait_tools.server_services"
    _description="Union entre servidor y servicios"

    service  = fields.One2many('ait_tools.services', 'server_services')
    server   = fields.One2many('ait_tools.server', 'server_services')

    name = fields.Many2one('ait_tools.services')
    servers  = fields.Many2one('ait_tools.server')

