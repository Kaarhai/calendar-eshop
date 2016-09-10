# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings

from pdfdocument.document import mm


class InvoiceStationery(object):

    def __call__(self, canvas, pdfdocument):
        font_name = settings.PLATA_PDF_FONT_NAME

        left_offset = 28.6 * mm

        canvas.saveState()
        canvas.setFont('%s-Bold' % font_name, 10)
        canvas.drawString(26 * mm, 284 * mm, 'Draci.info')
        canvas.setFont(font_name, 10)
        canvas.drawString(26 * mm + left_offset, 284 * mm, u'Faktura za kalendáře')
        pdfdocument.draw_watermark(canvas)
        canvas.restoreState()

        canvas.saveState()
        canvas.setFont('%s' % font_name, 6)
        for i, text in enumerate(reversed([
                pdfdocument.doc.page_index_string()])):
            canvas.drawRightString(190 * mm, (8 + 3 * i) * mm, text)

        for i, text in enumerate(reversed(['Draci.info'])):
            canvas.drawString(26 * mm + left_offset, (8 + 3 * i) * mm, text)

        logo = getattr(settings, 'PDF_LOGO_SETTINGS', None)
        if logo:
            canvas.drawImage(
                os.path.join(
                    settings.APP_BASEDIR,
                    'metronom',
                    'reporting',
                    'images',
                    logo[0]),
                **logo[1])

        canvas.restoreState()
