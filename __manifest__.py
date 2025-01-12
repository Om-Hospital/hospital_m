# __manifest__.py

{
    'name': 'Hospital Patient Management',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Manage patient records in the hospital system.',
    'author': 'MD. Sabbir Hossain',
    'website': 'https://www.xsellencebdltd.com',
    'depends': ['base','mail','product'],  # Dependencies, base is always needed
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
