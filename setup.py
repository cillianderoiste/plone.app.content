from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='plone.app.content',
      version=version,
      description="Content Views for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Plone",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
      ],
      keywords='plone content views viewlet',
      author='Jeroen Vloothuis',
      author_email='jeroen.vloothuis@xs4all.nl',
      url='http://svn.plone.org/svn/plone/plone.app.content',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages = ['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
            'zope.publisher',
            'zope.testing',
            'Products.PloneTestCase',
          ]
      ),
      install_requires=[
        'setuptools',
        'plone.i18n',
        'plone.memoize',
        'plone.navigation',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.component',
        'zope.event',
        'zope.lifecycleevent',
        'zope.schema',
        'zope.viewlet',
        'zope.app.container',
        'zope.app.pagetemplate',
        'Products.CMFCore',
        'Products.CMFDefault',
        'Acquisition',
        'Zope2',
      ],
      )
