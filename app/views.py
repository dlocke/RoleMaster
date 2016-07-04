from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db

from .models import Organization, OrganizationMembership, RolemasterRole, Accountability, Domain, RoleFilling

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

class RM_OrganizationModelView(ModelView):
    """TODO: Document me"""
    datamodel = SQLAInterface(Organization)

    list_columns = ['name', 'description']

    #related_views = []
    #label_columns = {}
    #show_fieldsets = []

class RM_OrganizationMembershipModelView(ModelView):
    """TODO: Document me"""
    datamodel = SQLAInterface(OrganizationMembership)

    list_columns = ['organization', 'user']

class RM_RoleModelView(ModelView):
    """TODO: Document me"""
    datamodel = SQLAInterface(RolemasterRole)

    list_columns = ['name', 'organization']

class RM_AccountabilityModelView(ModelView):
    """TODO: Document me"""
    datamodel = SQLAInterface(Accountability)

    list_columns = ['role', 'description']

class RM_DomainModelView(ModelView):
    """TODO: Document me"""
    datamodel = SQLAInterface(Domain)

    list_columns = ['role', 'description']

class RM_RoleFillingModelView(ModelView):
    """TODO: Document me"""
    datamodel = SQLAInterface(RoleFilling)

    list_columns = ['role', 'user']

db.create_all()

appbuilder.add_view(RM_OrganizationModelView, "List Organizations")
appbuilder.add_view(RM_OrganizationMembershipModelView, "List Organization Members")
appbuilder.add_view(RM_RoleModelView, "List Roles")
appbuilder.add_view(RM_AccountabilityModelView, "List Accountabilities")
appbuilder.add_view(RM_DomainModelView, "List Domains")
appbuilder.add_view(RM_RoleFillingModelView, "List Roles Filled")


