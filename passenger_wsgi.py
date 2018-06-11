import sys, os
INTERP = "/home/optcfpah/virtualenv/optcfp/3.5/bin/python"
#INTERP is present twice so that the new python interpreter
#knows the actual executable path 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/optcfp')  #You must add your project here

sys.path.insert(0,cwd+'/optcfp/bin')
sys.path.insert(0,cwd+'/optcfp/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "optcfp.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()