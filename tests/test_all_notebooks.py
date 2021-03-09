import nbdev.test

def test_run():
    nbdev.test.test_nb('./module_notebooks/00_api.ipynb')
    nbdev.test.test_nb('./module_notebooks/01_test_helper.ipynb')