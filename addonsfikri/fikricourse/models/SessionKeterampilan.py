from odoo import fields, models, api


class SessionKeterampilan(models.Model):
    _name = 'fikricourse.sessionketerampilan'
    _description = 'Description'
    name = fields.Char(string='Nama')
    nama_kursus = fields.Many2one(
        comodel_name='fikricourse.keterampilan',
        string='Nama kursus',
        required=False)
    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama_tutor',
        required=False,
        domain=[('function', '=', 'Tutor Keterampilan')])
    tgl_mulai = fields.Datetime(
        string='Tgl_mulai',
        required=False,
        default=fields.Datetime.now())
    peserta_keterampilan_ids = fields.One2many(
        comodel_name='fikricourse.pesertaketerampilan',
        inverse_name='session_id',
        string='Peserta',
        required=False)
    jml_siswa = fields.Integer(
        compute='_compute_peserta',
        string='Jml Siswa',
        required=False)

    @api.model
    def _compute_peserta(self):
        for record in self:
            a = self.env['fikricourse.pesertaketerampilan'].search([('session_id', '=', record.id)]).mapped(
                'display_name')
            b = len(a)
            record.jml_siswa = b
            record.nama_kursus.jml_siswa_ket = b

class PesertaKeterampilan(models.Model):
    _name = 'fikricourse.pesertaketerampilan'
    _description = 'PesertaKeterampilan'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Keterampilan',
        required=False,
        domain=[('is_peserta', '=', True), ('jenis_kursus', '=', 'keterampilan')])
    session_id = fields.Many2one(
        comodel_name='fikricourse.sessionketerampilan',
        string='Session_id',
        required=False)
