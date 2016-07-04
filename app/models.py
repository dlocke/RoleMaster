from flask.ext.appbuilder import Model
#from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Organization(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)
    description = Column(Text, unique = False, nullable = False)

    def __repr__(self):
        return self.name

class RolemasterRole(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable = False)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    organization = relationship("Organization")

    def __repr__(self):
        return self.name

class Accountability(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    description = Column(String(250), unique = False, nullable = False)
    role_id = Column(Integer, ForeignKey('rolemaster_role.id'))
    role = relationship("RolemasterRole")

class Domain(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    description = Column(String(250), unique = False, nullable = False)
    role_id = Column(Integer, ForeignKey('rolemaster_role.id'))
    role = relationship("RolemasterRole")

class RoleFilling(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('rolemaster_role.id'))
    role = relationship("RolemasterRole")
    user_id = Column(Integer, ForeignKey('ab_user.id'))
    user = relationship(User)