.. post:: Sep 10, 2014
    :tags: layout
    :category: device, bootstrap

.. |ad| replace:: ``angular.dart``
.. |adui| replace:: ``angular.dart.ui``
.. |bs| replace:: ``bootstrap``
.. |js| replace:: ``javascript``


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

We'll start with a simple example.

Let's layout three different colored buttons for a selector.
We'll start with pinegrow_'s desktop visual editor to layout some grids
for the buttons, and test them.





.. _bootply: http://www.bootply.com/96266
.. _bootstrapzero: http://www.bootstrapzero.com/
.. _pinegrow: http://pinegrow.com/
.. _divshot: https://divshot.com/features

----

.. [#] One such review is `here`_.
