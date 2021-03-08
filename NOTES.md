# nbdev template

Use this template to more easily create your [nbdev](https://nbdev.fast.ai/) project.

_If you are using an older version of this template, and want to upgrade to the theme-based version, see [this helper script](https://gist.github.com/hamelsmu/977e82a23dcd8dcff9058079cb4a8f18) (more explanation of what this means is contained in the link to the script)_.



Following the tutorial:

1. Edit the [settings.ini file](./settings.ini).
2. Install git hooks to avoid and handle conflicts with respect to notebooks metadata. Run `nbdev_install_git_hooks`. If there are any conflicts later then you can run `nbdev_fix_merge filename.ipynb`
3. `nbdev_build_lib` -- this builds the python library from the notebooks.
4. `nbdev_build_docs` -- builds the documentation and creates a README.md
5. `nbdev_test_nbs` -- performs all of the tests in the notebooks.

Created a docker image to run the documentation locally. This docker script can be run through the make command:

``` bash
make docker_docs_serve
```

The [MANIFEST.in](https://packaging.python.org/guides/using-manifest-in/) file is used by the Python package manager to include/exclude files from the source distribution when packaging this software.