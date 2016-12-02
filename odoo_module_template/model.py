# -*- coding: utf-8 -*-

#    Bashir Idirs (Alsuty)
#    Copyright (C) 2016.
#
#    This Code is free: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openerp import models,fields

class FirstModel(models.Model):
	_name= 'template.firstmodel'

	image = fields.Binary('Image')
	name = fields.Char('Name', required=True)
	
	select_field = fields.Selection(string="Type", 
						selection=[('type1', 'Type1'), 
						('type2', 'Type2'), 
						('type3', 'Type3'),], required=True)
	boolean_field = fields.Boolean('Check')
	integer_field = fields.Integer('Integer Number')
	float_field = fields.Float('Float Value')

	many2one_field = fields.Many2one('template.secondmodel', 'Many2one')
	many2many_ids = fields.Many2many('template.thirdmodel', 
						'many2many_relation', 'firstmodel_id', 
						'thirdmodel_id', string='Many2many')
	ony2many_fields = fields.One2many('template.forthmodel', 
						'firstmodel_id', string='One2many')

class SecondModel(models.Model):
	_name = 'template.secondmodel'

	name = fields.Char('Name')

class ThirdModel(models.Model):
	_name = 'template.thirdmodel'

	name = fields.Char('Name')

class ForthModel(models.Model):
	_name = 'template.forthmodel'

	name = fields.Char('Name')
	firstmodel_id= fields.Many2one('template.firstmodel')


