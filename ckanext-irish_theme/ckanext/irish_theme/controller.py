import os
import ckan.plugins as p
from ckan.lib.base import BaseController

class IrishThemeController(BaseController):
  def contact(self):
    return p.toolkit.render('home/contactInfo.html')

  def foi(self):
    return p.toolkit.render('home/foi.html')

  def psi(self):
    return p.toolkit.render('home/psi.html')
