from plone.fieldsets import FormFieldsets

from zope.interface import Interface
from zope.component import adapts
from zope.formlib.form import FormFields
from zope.interface import implements
from zope.schema import Bool

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import safe_hasattr

from form import ControlPanelForm

class ISecuritySchema(Interface):

    enable_self_reg = Bool(title=_(u'Enable Self Registration'),
                        description=_(u'''Allows users to join the site.  If not selected
                                       only site managers will be able to add new users
                                       '''),
                        default=False,
                        required=True)

    enable_user_pwd_choice = Bool(title=_(u'Let Users select their passwords'),
                        description=_(u'''If not selected passwords will be autogenerated 
                                         and mailed to users.
                                         '''),
                        default=False,
                        required=True)

    enable_user_folders = Bool(title=_(u'Enable User Folders'),
                        description=_(u'''If not selected passwords will be autogenerated 
                                      and mailed to users.
                                      '''),
                        default=False,
                        required=True)

    enable_anon_views_about = Bool(title=_(u'Allow anyone to view about information'),
                        description=_(u'''If not selected only logged in users will be
                                        able to view this information.
                                        '''),
                        default=False,
                        required=True)


class SecurityControlPanelAdapter(SchemaAdapterBase):
    
    adapts(IPloneSiteRoot)
    implements(ISecuritySchema)

    def __init__(self, context):
        super(SecurityControlPanelAdapter, self).__init__(context)
        pprop = getToolByName(context, 'portal_properties')
        self.context = pprop
        self.site_properties = pprop.site_properties

        enable_self_reg = ProxyFieldProperty(ISecuritySchema['enable_self_reg'])
        enable_user_pwd_choice = ProxyFieldProperty(ISecuritySchema['enable_user_pwd_choice'])
        enable_user_folders = ProxyFieldProperty(ISecuritySchema['enable_user_folders'])

        def get_enable_self_reg(self):
            return self.site_properties.enable_self_reg

        def set_enable_self_reg(self, value):
            self.site_properties.enable_self_reg = value

        enable_self_reg = property(get_enable_self_reg, set_enable_self_reg)


        def get_enable_user_pwd_choice(self):
            return self.site_properties.enable_user_pwd_choice

        def set_enable_user_pwd_choice(self, value):
            self.site_properties.enable_user_pwd_choice = value

        enable_user_pwd_choice = property(get_enable_user_pwd_choice, set_enable_user_pwd_choice)


        def get_enable_user_folders(self):
            return self.site_properties.enable_user_folders

        def set_enable_user_folders(self, value):
            self.site_properties.enable_user_folders = value

        enable_user_folders = property(get_enable_user_folders, set_enable_user_folders)


        def get_enable_anon_views_about(self):
            return self.site_properties.enable_anon_views_about

        def set_enable_anon_views_about(self, value):
            self.site_properties.enable_anon_views_about = value

        enable_anon_views_about = property(get_enable_anon_views_about, set_enable_anon_views_about)


class SecurityControlPanel(ControlPanelForm):

    form_fields = FormFieldsets(ISecuritySchema)

    label = _("Security settings")
    description = _("Security settings for this Site.")
    form_name = _("Site Security Settings")
