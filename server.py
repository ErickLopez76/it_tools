from openerp import models, fields, api

class server(models.Model):
    _name = 'ait_tools.server'

    name = fields.Char(string='Title', required=True)
    description =  fields.Text()
    cores = fields.Integer(string="Numero de cores")
    memory = fields.Integer(string="Memoria")
    os = fields.Char(string="OS")
    hdd = fields.Integer(string="Capacidad Disco")
    ip = fields.Char(string="Direccion IP")

    capacity = fields.Many2one('ait_tools.capacity', requiered=False)

    @api.onchange('capacity')
    def _onchange_course(self):
        if not self.name:
            self.name = self.capacity.name
