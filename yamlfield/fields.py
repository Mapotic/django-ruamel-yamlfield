from django.core.exceptions import ValidationError
from django.db import models
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from ruamel.yaml.composer import ComposerError
from ruamel.yaml.parser import ParserError


class RuamelYAML(YAML):
    def dump(self, data, stream=None, **kw):

        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()


yaml = RuamelYAML()


class YAMLField(models.TextField):

    def from_db_value(self, value, expression, connection, context=None):
        return self.to_python(value)

    def to_python(self, value):
        """
        Convert our YAML string to a Python object
        after we load it from the DB.
        """
        if value == "":
            return None
        try:
            if isinstance(value, str):
                return yaml.load(value)
        except ValueError:
            raise ValidationError("Enter valid YAML")
        except ParserError as e:
            raise ValidationError(e)
        except ComposerError:
            return ''
        return value

    def get_prep_value(self, value):
        """
        Convert our Python object to a string of YAML before we save.
        """
        if not value or value == "":
            return ""
        if isinstance(value, (dict, list)):
            value = yaml.dump(value)
        return value

    def value_from_object(self, obj):
        """
        Returns the value of this field in the given model instance.

        We need to override this so that the YAML comes out properly formatted
        in the admin widget.


        This method are override because of allow_unicode param!
        """
        value = getattr(obj, self.attname)
        if not value or value == "":
            return value

        return yaml.dump(value)
