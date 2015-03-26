from openerp import models, fields, api

class services(models.Model):
    _name = 'ait_tools.services'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    server = fields.Many2one('ait_tools.server',required=False)

    server_services = fields.Many2one('ait_tools.server_services')

    @api.onchange('server')
    def _onchange_course(self):
        if not self.name:
            self.name = self.server.name
