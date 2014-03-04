from distutils.core import setup
desc = """
DiffbotMW

This library makes a GET HTTP request to the DiffbotMW web API ex: "http://api.diffbot.com/v2/articles"
and gives a JSON object back of the result.

"""
setup(name='diffbot_mw',
      version='1.0',
      py_modules=['diffbot_mw'],
      author='Islam Bahnasy',
      author_email='islam@cybertechlab.com',
      url='http://cybertechlab.com',
      description='Handles DiffbotMW APIs fetching and returns JSON object of the result',
      long_description=desc,
      license='GPL-V3'
      )
