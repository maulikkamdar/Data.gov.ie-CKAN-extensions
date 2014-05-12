'''plugin.py
'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class IrishThemePlugin(plugins.SingletonPlugin):
  '''The first Irish Data Gov CKAN Template
  '''
  plugins.implements(plugins.IConfigurer)
  plugins.implements(plugins.IRoutes, inherit=True)
 
  def update_config(self,config):
    toolkit.add_template_directory(config, 'templates')
    toolkit.add_public_directory(config, 'public')
    toolkit.add_resource('fantastic', 'irish_theme')

  def before_map(self, m):
    m.connect('contact', '/contact', controller='ckanext.irish_theme.controller:IrishThemeController', action='contact')
    m.connect('freedomofinformation', '/freedomofinformation', controller='ckanext.irish_theme.controller:IrishThemeController', action='foi')
    m.connect('publicsectorinformation', '/publicsectorinformation', controller='ckanext.irish_theme.controller:IrishThemeController', action='psi')
    return m

