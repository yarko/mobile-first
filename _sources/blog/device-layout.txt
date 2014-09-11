.. post:: Sep 10, 2014
    :tags: layout
    :category: device, bootstrap

.. |ad| replace:: ``angular.dart``
.. |adui| replace:: ``angular.dart.ui``
.. |bs| replace:: ``bootstrap``
.. |js| replace:: ``javascript``
.. |pg| replace:: Pinegrow_


Device Layout
=============

*This is the first post on this topic, looking at some loayout tools (and their potential limitations).*

Let's say you've created one of the examples
(e.g. one of the |ad|_ tutorials)
all the way through the cycles of building and running:

- dart in chromium via the `dart editor`_
- `dart2js`_ result in a browser
- on `android from the dart GUI`_
- `cordova emulators`_ for iOS and android (through several size devices)
- cordova built apps on target iOS and android devices.

You will have noticed that (for example) the |ad| `tutorial`_
might look fine in a browser, and on a phone, but is too small to
use on a tablet.

There's already enough to learn.
Now, we're going to add |adui|_, a dart implementation of ``twitter`` |bs|_
which will use dart written components with |bs| ``CSS`` (and grids).

If you haven't felt overwhelmed yet, you might now.
We need some help with basic layout for our devices.

.. _ad: https://angulardart.org/
.. _tutorial: https://angulardart.org/tutorial/
.. _adui: http://www.angulardartui.com/
.. _bs: http://getbootstrap.com/
.. _android from the dart GUI: https://www.dartlang.org/tools/editor/mobile.html
.. _dart editor: https://www.dartlang.org/tools/editor/
.. _dart2js: https://www.dartlang.org/tools/dart2js/
.. _cordova emulators: http://cordova.apache.org/docs/en/3.5.0/guide_cli_index.md.html#The%20Command-Line%20Interface



Tools Overview
---------------

There are two things to note:

- we will avoid using any more than the ``CSS`` parts of |bs|;
- for any |js| introduced, we'll look for |adui| equivalents;

  * where we can't readily, remember that calling |js| from dart is ok.


You can search for reviews [#]_ for bootsrap visual editors.
The few that initially impressed me are bootply_, pinegrow_, and divshot_.
You can find some starting point layouts for websites at bootstrapzero_,
free templates which you can view in bootply and interactively code online with bootply_.

.. _here: http://tutsme-webdesign.info/best-bootstrap-visual-editor/

Working an Example
------------------

We'll start with a simple example.

Let's layout three different colored buttons for a selector.
We'll start with pinegrow_'s desktop visual editor to layout some grids
for the buttons, and test them [#]_.

.. image:: /_static/pinegrow-blank.png


Next, by clicking / dragging from the left pallete, add in order:

- a container
- a row
- three columns

Note that you can duplicate an item,
such as the column,
by clicking it's double-page icon.

The result should resemble this:

.. image:: /_static/pinegrow-3columns.png

Delete the column paragraphs by selecting them in the right tree.
Once selected, you can either use your delete key, or the *trash can* icon
of the selected item in the middle pane.

For now, let's keep the column headings, but rename them.
You can select the headings in the right tree,
and edit using item's ``Actions > Edit content`` menu.
You can also simply double-click
the text of the heading in the middle pane.

Here's my resulting layout.
I've made the buttons large,
and searched for a ``center`` CSS class in bootstrap -
I found ``.center-block`` which works for me.

.. image:: /_static/pinegrow-buttons.png


Notice in the middle panel, the menu at the top.
You can change the aspect in the middle pane's layout
by, for example, changing (from the pulldown) to ``phone / 320px``.
You can change the zoom of your view from the top |pg| menu (near the right).

.. image:: /_static/pinegrow-phone.png

The code is relatively straightforward.
You can get to it from the ``Page > Edit code`` menu.

.. image:: /_static/pinegrow-codeview.png


Angular Dart UI
---------------

Comparing it to a version of the *button demo* of
|adui| (a port of bootstrap),
it doesn't look like we have too much work to do
to combine what we developed with |pg| with |ad|.
We have ``ng-model`` to add to the buttons, but
otherwise the button properties from Pingrow should be useable.
I'll guess that putting the grid ``div``\s inside
the ``buttons-ctrl`` ``div`` will be all that remains.

.. image:: /_static/pinegrow-codewdart.png

We have no javascript (the defaults which |pg| inserted
aren't needed), and we're not using any css beyond |bs|.


``bootply`` Preview
--------------------

To show the output of |pg| in bootply_,
I started with the ``Basic starter`` in bootply_
and then added the container from |pg|.
Here is the result:

.. image:: /_static/pinegrow-inbootply.png


Next Steps
----------

Here is the |pg| generated source.
Note that ``line 18`` shows a link to the new css file,
which, in our case, is empty.

.. literalinclude:: /_static/new.html
    :language: html
    :linenos:


Pinegrow also leaves behind some artifacts which you'll want to be aware of:

- a directory of backups, ``_pgbackup``
- a configuration file, ``pinegrow.json``
- a directory of the bootstrap you used, ``bootstrap``

In the next post, I'll look at using this with |adui|
and testing in various targets, including trying to run
on various sized mobile devices.


Let's see how that goes.


.. _bootply: http://www.bootply.com/96266
.. _bootstrapzero: http://www.bootstrapzero.com/
.. _pinegrow: http://pinegrow.com/
.. _divshot: https://divshot.com/features

----

.. [#] One such review is `here`_.
.. [#] I started with |pg| release 1.15, but have moved to the beta release - 1.2b1.

