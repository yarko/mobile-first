<!--
A nice reference:
http://code.tutsplus.com/articles/team-collaboration-with-github--net-29876
-->
*This is a work-in-progress, at this point not usable by
any but the most ardent.*
*Follow developments on the [blog](https://yarko.github.io/mobile-first).*
*Find setup guides on the [wiki](https://github.com/yarko/mobile-first/wiki).*

# Mobile Test app (`sens`)

This is an exploration to create mobile-first, disconnected
applications for field tests which can be run from a server,
or installed on mobile devices.

Some of the things of interest:

 * putting useful logic simply into a single-page app and allow disconnected function;
 * exploring the 5M data limit (size, off-line validation, etc.) in an installable app;
 * cordova deployment to mobiles (e.g. iOS, Android, ...);

Some colleagues have commented on the (bleeding) edginess
of both angular.dart and cordova.
I expect most of the dart2js results will stay in a mostly central
area of cordova - I don't expect any significant trouble.
As for angular.dart on a cordova target - I have no idea.
Angular dart tutorials seem to work fine.
I think that what trouble may come will be
from mixing dart libraries.
Angular.dart 0.12 seems ok, 0.13 seems to be coming along.
Note that cordova's stated goal is to obsolete itself,
so that all device-special
API points will gradually show up in HTML5.
Since, at the outset, we are not using any device specific features,
I am satisfied to use cordova as an execution and installation shell.
As for dart - ECSMA-6 seems influenced by aspects of dart which
feel like a modern language.
The dart team is working to get dart accepted as an standard.
In the meantime, I am more than happy to minimze or eliminate
dealing with the messy javascript ecosphere.

I have several goals here:

 1. To establish a toolchain and workflow to get from
    [angular.dart app](https://angulardart.org) to mobile
    running application, with testing and debugging in between.
    Follow the [wiki](https://github.com/yarko/mobile-first/wiki)
    for help in setting up your development environments.
    Look at the [blog](https://yarko.github.io/mobile-first)
    for ongoing developments and hints.

 2. Identify libraries for managing
    the various sizes of target devices. Examples are
    included as git submodules, including
    [angular.dart.ui](http://akserg.github.io/angular.dart.ui.demo/build/index.html),
    a pure dart port of twitter bootstrap.
    Other examples for your testing are the
    [angular.dart.tutorial](https://angulardart.org/tutorial)
    and [paper.elements](https://github.com/dart-lang/paper-elements),
    a polymer.dart library which initially had some conflicts
    in running under angular.dart projects.

 3. An example application, which can be used as a starting point for your own
    mobile-first, which can operate network-disconnected.  To this end, the example
    will show use of the
    [`lawndart` library](http://blog.sethladd.com/2013/02/lawndart-helps-you-write-offline-web.html) to select the local storage based on
    the capability of your client device.  The example will also include deferred
    data binding with a server (a django example is planned).


For starters, the *Recipe Book AngularDart application* from the
[angular-dart-tutorial](https://angulardart.org/tutorial)
is a good starting point and trial app to flush out your developmenet setup.

See the repository [wiki](https://github.com/yarko/mobile-first/wiki)
for information on setting up a working environment.

----
**Note:** Cloning this repository clones the wiki pages as a submodule.

Developer notes may be useful to have locally.
For OS X, [Atom](https://atom.io/) and [Mou](http://mouapp.com)
provide markdown rendering.

Feel free to update the wiki thru git.
Simply `cd` to `mobile-first.wiki`, and `git commit` from there.

Note: I use git submodules here.
It's simple, but takes a little getting used to.
The key to remember, submodules are separate git clones - in general,
think of them
as if they were separate clones (pulling, editing, commiting, pushing from them).
Committing from this repository (the containing repository) will also
require updating the submodule, but only to keep indexes consistent.
You will get used to it.

To get started, make your first clone:

```
git clone --recursive git@github.com:yarko/mobile-first.git
```

To continue to get submodules automatically, either descend into the submodule
directories and `pull` (or `ftch`) from them,
or, from `mobile-first`, use the command form:

```
git pull --recurse-submodules
```

 useful cheat-sheet on git-submodules,
 see [git-submodule-cheat-shet](http://blog.jacius.info/git-submodule-cheat-sheet/)
