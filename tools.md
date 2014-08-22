Overview
================

We use the following tools to build our mobile-first app and get it running on the iPad.

* Dart
* AngularDart
* Cordova
* XCode

Dart is an open source programming language from Google. It is, among other
things, intended as a javascript replacement. It can be compiled to javascript,
which is how we intend to use it.

AngularDart is a Dart port of the AngularJS web framework. You can find some of
the philosophy behind the AngularJS framework
[here](https://docs.angularjs.org/guide/introduction).

"[Apache Cordova](http://cordova.apache.org) is a platform for building native
mobile applications using HTML, CSS, and Javascript." This is what lets deploy
our web application, developed in Dart/AngularDart and compiled to javascript,
as a native app on iOS (and, in the future, Android).

XCode is Apple's IDE for building Mac and iOS apps.

Installation
=================

Dart
----------

The IDE (a modified version of Eclipse) and command line tools can be found
[here](https://www.dartlang.org/tools/editor/). To "install", just unzip the
archive and move the `dart` directory to `/Applications/dart/`. To launch the
DartEditor, just open `/Applications/dart/DartEditor` like any other
application. The command line tools are located in
`/Applications/dart/dart-sdk/bin/`.

AngularDart
-------------

I don't believe that AngularDart needs to be installed -- we should just need
to include it as a dependency in the Dart project that we're working on. But to
make sure that things are working properly, you can download the
[tutorials](https://github.com/angular/angular.dart.tutorial) and open the
directory in DartEditor. Make sure the files browser is showing (click the
Tools->Files menu item if necessary). Select
`angular.dart.tutorial-master/Chapter_03/web/main.dart` and click the Run->Run
menu item. This should launch the chapter 3 tutorial app (a simple 5 star
rating example) in Chromium.

Cordova 
--------------

Follow the "Installing the Cordova CLI" located
[here](https://cordova.apache.org/docs/en/3.0.0/guide_cli_index.md.html). Note
that you'll first need to install node.js in order to use the `npm` package
manner.. I installed it using homebrew and that worked fine.

	$ brew install node
	$ sudo npm install -g cordova
	$ sudo npm install -g ios-sim

Xcode
---------------

Install XCode via the Mac App store.

Build Process
=====================================================

In this section, we'll demonstrate how to build a Dart app and run it in the
iOS Simulator (which is included as part of XCode). We will use chapter 3 of
the Dart tutorials as our example. These tutorials are included as a submodule
of our mobile-first repository.

For the moment, you will need to have your github account configured to use
public key authentication in order to checkout the repository with all of its
submodules.

Assuming that is the case, use the following commands to clone the mobile-first
repository and all of its submodules.

	$ git clone --recursive git@github.com:yarko/mobile-first.git

And now build the dart app (chapter 3 tutorial in this case):

	$ cd mobile-first/examples/angular.dart.tutorial/Chapter_03/
	$ /Applications/dart/dart-sdk/bin/pub build

The "pub" tool is a command line package manager included with the Dart SDK.
The "pub build" sub-command packages a Dart app for deployment. Currently, that
means compiling the dart app down to html and javascript. If you look under
`Chapter_03`, there should now be a `web/build` subdirectory. This directory
contains the html and javascript necessary to run the Chapter 3 dart tutorial
app. You can see this by opening `web/build/index.html` in a web browser.

Next, we will create a new Cordova app, move the html and javascript generated
by `pub build` into this app, and finally

