from setuptools import setup
import setup_translate

pkg = 'Extensions.PPanel'
setup(name='enigma2-plugin-extensions-ppanel',
       version='0.1',
       description='PPanel',
       package_dir={pkg: 'PPanel'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
