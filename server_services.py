from openerp import models, fields, api

class server_services(models.Model):
    _name = "ait_tools.server_services"

    name = fields.Char(
