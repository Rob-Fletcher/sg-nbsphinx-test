# SG_test

This repo is just to reproduce the error that happens when building sphinx-gallery with 
nbsphinx.

I am testing this on Windows11 in WSL2 (Ubuntu) and `python==3.10`

Install the requirements file
```bash
pip install -r requirements.txt
```

Then go to the `docs/` directory and run `make html`.

With the `nbsphinx` extension included in `docs/conf.py` you should see the errors:
```
/home/rob/projects/sg_test/docs/source/auto_examples/index.rst:24: WARNING: undefined label: 'sphx_glr_auto_examples_plot_searching.py' [ref.ref]
/home/rob/projects/sg_test/docs/source/auto_examples/sg_execution_times.rst:35: WARNING: undefined label: 'sphx_glr_auto_examples_plot_searching.py' [ref.ref]
/home/rob/projects/sg_test/docs/source/auto_examples/index.rst:24: WARNING: undefined label: 'sphx_glr_auto_examples_plot_searching.py' [ref.ref]
/home/rob/projects/sg_test/docs/source/sg_execution_times.rst:35: WARNING: undefined label: 'sphx_glr_auto_examples_plot_searching.py' [ref.ref]
```

If you point your browser at the built index file at `docs/build/html/index.html` you should see 
that the link to the example page is broken. Then if you navigate to the example file at
`docs/build/html/auto_examples/index.html` you should see that the map widget is rendered correctly.

Now comment out `nbsphinx` from the `conf.py` and rebuild with `make clean && make html`. Now 
the main index page should have a working link that takes you to the example page. The example page
now only shows text output for the map widget however.