[![Stories in Ready](https://badge.waffle.io/yarko/mobile-first.png?label=ready&title=Ready)](https://waffle.io/yarko/mobile-first)

[![Stories in Ready](https://badge.waffle.io/yarko/mobile-first.png?label=in-progress&title=In+Progress)](https://waffle.io/yarko/mobile-first)
# Olfactory Test app (`sens`)

This is an exploratory app to create a mobile-first
app for application of field tests for researchers.

Some of the things of interest:

 * how much useful logic can be put into a single-page app thus allowing disconnected function;
 * what are the data limits (size, and otherwise, e.g. off-line validation);
 * how can  a single page app be deployed to disconnectecd mobiles (e.g. iOS, Android, WinMobile);

Initially, the *Recipe Book AngularDart application* from the
[angular-dart-tutorial](https://angulardart.org/tutorial) is the starting point.

See the repository [wiki](https://github.com/yarko/mobile-first/wiki) for more information.


### Startup Tasks / Status:

##### Decisions:

- [x] Select client app framework (angular.dart);
- [x] Select deployment mechanism (standard mobile, using cordova/phonegap)
- [ ] Select angular.dart - to cordova integration / UI methods
  - [ ] Rikolu?
  - [ ] Ionic w/ angular.dart changes (ours);
  - [ ] Ionic w/ app back-porting (angular.dart => angular.js)
  - [ ] manual / other methods

##### Process:

- [x] bringup methods / tutorials for angular.dart
- [x] bringup methods / tutorials for cordova (w/ ios & android emulation)
- [ ] bringup methods / tutorials for integrating Rikolu
- [x] agile tracking (waffle.io for now, plus github issues, PRs)
- [ ] bring tutorial app thru full cycle:
  - [x] dart-dev (browser)
  - [ ] cordova (2 mobiles)
  - [ ] physical devices (android phone, iOS tablet, iOS phone)
- [ ] establish test methods & coverage tracking;
- [ ] establish test & build tracking (jenkins / drone.io);
- [ ] establish deployment activity to android store;
- [ ] establish deployment activity to Apple store;
- [ ] establish server / web access deployment;
- [x] documentation: wiki: markdown or restructuredText; docs: sphinxdoc.org

##### Development:

- [ ] angular.dart tutorial, modify for single even `sniffin sticks` instance
  - [ ] browser
  - [ ] mobile emulators
  - [ ] mobile hardware / team review, initial reactions;
- [ ] angular.dart: add suitable input UI methods (clickable / touchable);
- [ ] full single instance logic
- [ ] rotating RGB indicators to administrator;
- [ ] implementation of 7 turning points;
- [ ] local data storage (no network checks);
- [ ] remote data storage (assume network present);
- [ ] rudimentary server work;
- [ ] integrate local/connected storage (include data stroage limit checks);
- [ ] sync logic & functions:  disconnected - then - connected situations;
- [ ] server: add pandas, basic monitoring, transfer and analysis functions;
- [ ] server: accounts, tester & admin level permissions;

##### Documentation:

- [x] developer (ongoing / evolution);
- [ ] end user (test administrator);
- [ ] manager / site admin docs;
- [ ] devops / deployment instructions (for future / other projects);
- [ ] blog / article writup about forking, using this project for other targets & state of the art of single-development mobile apps;



 
