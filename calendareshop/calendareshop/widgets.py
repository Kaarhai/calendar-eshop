import os
import urllib2
import mimetypes
from urlparse import urlparse

from django.forms.widgets import FileInput, CheckboxInput, TextInput
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.html import escape, conditional_escape
from django.utils.translation import ugettext_lazy
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

FILE_INPUT_CONTRADICTION = object()


class URLFileInput(FileInput):

    """
    Taken from https://djangosnippets.org/snippets/2520/
    """
    initial_text = ugettext_lazy('Currently')
    input_text = ugettext_lazy('Upload from local repository')
    clear_checkbox_label = ugettext_lazy('Clear')
    url_text_label = ugettext_lazy('Upload from URL address')
    or_text = ugettext_lazy('OR')

    template_with_initial = u'<p class="file-upload">%(initial_text)s: %(initial)s %(clear_template)s<strong>%(or_text)s</strong><br />%(url_template)s<br />%(input_text)s: %(input)s</p>'
    template_only_url = u'<p class="file-upload">%(url_template)s<strong>%(or_text)s</strong><br />%(input_text)s: %(input)s</p>'

    template_with_clear = u'<span class="clearable-file-input">%(clear)s <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label></span>'
    template_with_url = u'%(url_text_label)s: %(url)s'

    def clear_checkbox_name(self, name):
        """
        Given the name of the file input, return the name of the clear checkbox
        input.
        """
        return name + '-clear'

    def clear_checkbox_id(self, name):
        """
        Given the name of the clear checkbox input, return the HTML id for it.
        """
        return name + '_id'

    def url_text_name(self, name):
        """
        Given the name of the file input, return the name of the url text
        input.
        """
        return name + '-url-clear'

    def url_text_id(self, name):
        """
        Given the name of the url text input, return the HTML id for it.
        """
        return name + '_url_id'

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
            'url_text_label': self.url_text_label,
            'or_text': self.or_text
        }

        template = self.template_only_url
        substitutions['input'] = super(URLFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = (u'<a href="%s">%s</a>'
                                        % (escape(value.url),
                                           escape(force_unicode(value))))
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        text_name = self.url_text_name(name)
        text_id = self.url_text_id(text_name)
        substitutions['url_text_name'] = conditional_escape(text_name)
        substitutions['url_text_id'] = conditional_escape(text_id)
        substitutions['url'] = TextInput().render(text_name, "", attrs={'id': text_id, "class": "form-control"})
        substitutions['url_template'] = self.template_with_url % substitutions

        return mark_safe(template % substitutions)

    def value_from_datadict(self, data, files, name):
        upload = super(URLFileInput, self).value_from_datadict(data, files, name)
        if not self.is_required and CheckboxInput().value_from_datadict(
                data, files, self.clear_checkbox_name(name)):
            if upload:
                # If the user contradicts themselves (uploads a new file AND
                # checks the "clear" checkbox), we return a unique marker
                # object that FileField will turn into a ValidationError.
                return FILE_INPUT_CONTRADICTION
            # False signals to clear any existing value, as opposed to just None
            return False

        url = TextInput().value_from_datadict(data, files,
                                              self.url_text_name(name))
        if url:
            validate = URLValidator()
            try:
                validate(url)
            except ValidationError:
                return ''

            parsed_url = urlparse(url)
            name = os.path.basename(parsed_url[2])
            ext = os.path.splitext(parsed_url[2])[1]

            if url and ext in [".png", ".gif", ".jpg"]:
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                try:
                    ze_file = opener.open(url).read()
                except IOError:
                    return ''
                upload = SimpleUploadedFile(name=name, content=ze_file, content_type=mimetypes.guess_type(name))

        return upload

