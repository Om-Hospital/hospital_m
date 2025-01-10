# models/patient.py

from odoo import models, fields, api

from server.odoo.api import depends


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='patient', required=True)
    age = fields.Integer(string='Age', related='patient_id.age')
    gender = fields.Selection(string='Gender', related='patient_id.gender', readonly=False)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    prescription = fields.Html(string='Prescription', placeholder='Enter your prescription here .')


    #---- single onchange in one function
    # @api.onchange('age')
    # def onchange_age(self):
    #     self.age = self.patient_id.age

    # two onchange in one function
    @api.onchange('patient_id', 'age')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
        self.age = self.patient_id.age



