# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ./addons/garaje(models.Model):
#     _name = './addons/garaje../addons/garaje'
#     _description = './addons/garaje../addons/garaje'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# from email.policy import default
# import string
# from attr import field
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class aparcamiento(models.Model):
  _name = "garaje.aparcamiento"
  _description = "Permite defininir las caracteristicas de un aparcamiento"

  name = fields.Char('Dirección', required=True)
  plazas = fields.Integer(string="Plazas", required=True)

  #relaciones entre tablas
  coche_ids = fields.One2many('garaje.coche', 'aparcamiento_id', string='Coches')

class coche(models.Model):
  _name = 'garaje.coche'
  _description = 'Permite defininir las caracteristicas de un coche'
  _order = 'name'

  name = fields.Char(string='Matricula', required=True, size=7)
  modelo = fields.Char(string='Modelo', required=True)
  construido = fields.Date(string='Fecha de construcción')
  consumo = fields.Float('Consumo', (4,1), default=0.0, help='Consumo promedio de cada 100km')
  averiado = fields.Boolean(string='Averiado', default= False)
  annos = fields.Integer('Años', compute='_get_annos', )
  description = fields.Text('Descripción')

  #relaciones entre tablas
  aparcamiento_id = fields.Many2one('garaje.aparcamiento', string='Aparcamiento')
  mantenimiento_ids = fields.Many2many('garaje.mantenimiento', string='Mantenimientos')

  @api.depends('construido')
  def _get_annos(self):
    #TODO: lo dejamos para más adelante
    for coche in self:
      hoy = date.today()
      coche.annos = relativedelta(hoy, coche.construido).years
  
  #restricciones, no permitir registrar la misma matricula varias veces en la db
  _sql_constraints=[('name_uniq', 'unique(name)', 'Esta matricula ya existe')]

class mantenimiento(models.Model):
  _name = 'garaje.mantenimiento'
  _description = 'Permite definir monatenimientos rutinarios sobre conjuntos de coches'
  _order = 'fecha'

  #name = fields.Char()
  fecha= fields.Date('Fecha', required=True, default=fields.date.today())
  tipo= fields.Selection(string='Tipo', selection=[
    ('l','Lavar'),('r','Revisión'),('m','Mecánica'),('p','Pintura')], default='l')
  coste= fields.Float('Coste', (8,2), help='Coste total del mantenimiento')

  #relaciones entre tablas
  coche_ids = fields.Many2many('garaje.coche', string='Coches')

  def name_get(self):
    result = []
    for mantenimiento in self:
      description = f'{len(mantenimiento.coche_ids)} coches - {mantenimiento.coste} $'
      result.append((mantenimiento.id, description))
    return result

