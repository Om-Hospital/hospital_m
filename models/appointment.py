# models/patient.py

from odoo import models, fields

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('hospital.patient', string='patient')
    age = fields.Integer(string='Age', related='patient_id.age')
    gender = fields.Selection(string='Gender', related='patient_id.gender', readonly=False)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)

