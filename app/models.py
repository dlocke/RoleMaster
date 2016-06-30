from flask.ext.appbuilder import Model
#from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Organization(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)
    #description = Column(String(250), unique = False, nullable = False)

class Role(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable = False)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    organization = relationship("Organization")

class Accountability(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    description = Column(String(250), unique = False, nullable = False)
    role_id = Column(Integer, ForeignKey('role.id'))

class Domain(Model):
    """TODO: Document me"""
    id = Column(Integer, primary_key=True)
    description = Column(String(250), unique = False, nullable = False)
    role_id = Column(Integer, ForeignKey('role.id'))
