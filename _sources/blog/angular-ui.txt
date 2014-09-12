.. post:: Sep 11, 2014
    :tags: angular.dart.ui
    :category: device, bootstrap

.. |ad| replace:: ``angular.dart``
.. |adui| replace:: ``angular.dart.ui``
.. |bs| replace:: ``bootstrap``
.. |js| replace:: ``javascript``
.. |mf| replace:: ``mobile-first``
.. |pg| replace:: Pinegrow_


Device Layout, Part 2
======================

*This is the second post on this topic, where we apply a bootstrap layout to an angular.dart project,
and test it on various devices.*

Review
---------

From the last time, we used |pg| to build a three-button layout which we hope to make
usable on a variety of devices.

To get started, review the `device layout`_ post, and have your ``new.html`` file
ready to extract from.

.. _device layout: /blog/device-layout/index.html

If you haven't already, download, install and configure the `Dart Editor`_.

.. _Dart Editor: https://www.dartlang.org/tools/editor/

Because we are interacting with so many potentially bleeding-edge system
components, I strongly recommend you install using the |mf|_
makefile command::

    $ make dart-install


This will install both the *release* and the *dev* version of dart.
If you run into problems with one, you should try the other.
Libraries are changing rapidly.
What is found broken in the release may first be corrected in the ``dev`` releast.
Conversly, what is update in the ``dev`` release may break dependencies,
may work in the ``release``.
In the case of new changes or features, it can take some time to sort
out the cross-dependencies, and your spotting a problem and reporting it
may accelerate its resolution.


Bootstrap in Dart
------------------

Start the DartEditor.
I also start a programming editor (``vim``); you may like to do this also.

As of this writing, DartEditor ``1.7`` is not producing results, so stick with the ``1.6`` release.
In the |mf| scripts repository, you'll find the ``active-dart`` script,
which will report which release of dart you have active for ``CLI``.
You can also change which the currently active one is (assumes you used ``make dart-install``).


.. TODO:: work on this post is continuing...



.. _bootply: http://www.bootply.com/96266
.. _bootstrapzero: http://www.bootstrapzero.com/
.. _pinegrow: http://pinegrow.com/
.. _divshot: https://divshot.com/features

.. _ad: https://angulardart.org/
.. _adui: http://www.angulardartui.com/
.. _angular dart tutorial: https://angulardart.org/tutorial/
.. _bs: http://getbootstrap.com/
.. _android from the dart GUI: https://www.dartlang.org/tools/editor/mobile.html
.. _cordova emulators: http://cordova.apache.org/docs/en/3.5.0/guide_cli_index.md.html#The%20Command-Line%20Interface
.. _dart editor: https://www.dartlang.org/tools/editor/
.. _dart2js: https://www.dartlang.org/tools/dart2js/
.. _mf: https://github.com/yarko/mobile-first


