.. post:: Sep 5, 2014
   :tags: documentation
   :category: setup

Documentation Setup
====================

This is how I setup the project blog for this document.
If you create your own mobile-first project based on this repository,
you can simply add or replace items in these docs to your liking.
Then you won't need to setup the orphaned gh-pages branch.

If you'd like to setup docs / notes (blog) within your application
then you might find this helpful.

Settup
------

This blog uses sphinx-docs_ and ablog_, just as http://blog.readthedocs.com now does.

I setup a `virtualenv`_ in the ``docs`` direectory, and::

    $ pip install -r requirements.txt

then activate the environment when working on docs.

To set your docs to appear as project github pages, a separate output directory was made for
sphin-docs, named (in this case) after the repository, ``mobile-first``.

To make this output directory hold the rendered documentation,
first make sure it does not exist in the docs area.

Then, make a git-submodule to the main directory, thus::

    $ git submodule add -b gh-pages git@github.com:yarko/mobile-first.git ./docs/mobile-first


where ``mobile-first`` (repository and target) is replaced with your repository name.
This makes the repository a git-submodule to itself.
Now, similarly as shown on https://help.github.com/articles/creating-project-pages-manually,
do the following::

    $ cd docs/mobile-first
    $ git checkout --orphan gh-pages
    $ git rm -rf .
    # Note: the new branch won't appear in the branch list until your first commit
    $ touch .nojekyll


You'll notice in the ``Makefile`` (under the ``build`` command),
``mobile-first`` is the output directory.
Modify your ``Makefile`` to output to your sphinx-docs output directory.

Now::

    $ make build
    $ git add --all
    $ git commit -a -m 'first ablog build to gh-pages'
    # the first time, set the default upstream, so we can 'git push` from here on
    $ git push --set-upstream origin gh-pages

Give it a few minutes, then you should be able to navigate to your equivalent path of
``http://{{your-github-account}}.github.io/{{your-project-repository}}``, e.g.
http://yarko.github.io/mobile-first.

After this initial step, you should be able to simply edit an entry, and then::

    $ make build    # to compile the html
    $ make show     # to see the output locally
    # Then, once you're happy, commit the source; then:
    $ make publish  # to commit & push the generated results

and view your results at your equivalent of
http://yarko.github.io/mobile-first.

Feel free to `file an issue`_.


.. _ablog: http://ablog.readthedocs.org
.. _file an issue: https://github.com/yarko/mobile-first/issues
.. _Mobile First README: https://github.com/yarko/mobile-first/blob/master/README.md
.. _sphinx-docs: http://sphinx-doc.org
.. _virtualenv: http://virtualenv.readthedocs.org
.. |green| image:: http://img.shields.io/badge/Docs-latest-green.svg
.. |red| image:: http://img.shields.io/badge/Docs-release--1.6-red.svg
.. |yellow| image:: http://img.shields.io/badge/Docs-No%20Builds-yellow.svg
.. |nbsp| unicode:: 0xA0 
   :trim:

