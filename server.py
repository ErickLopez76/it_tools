from openerp import models, fields, api

class server(models.Model):
    _name = 'it_tools.server'

    name = fields.Char(string='Title', requiered=True)
    description =  fields.Text()
    cores = fields.Integer(string="Numero de cores")
    memory = fields.Integer(string="Memoria")
    os = fields.Char(string="OS")
    hdd = fields.Integer(string="Capacidad Disco")

