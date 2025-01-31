# models/patient.py
from datetime import date
from odoo import models, fields, api, _

from dateutil.utils import today
from email.policy import default


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True, tracking=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string='Gender', tracking=True,
                              default='male')

    medical_history = fields.Text(string='Medical History', tracking=True)
    emergency_contact = fields.Char(string='Emergency Contact', tracking=True)
    active = fields.Boolean(string='Active', default='True', tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0