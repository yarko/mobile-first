
### Startup Tasks / Status:

##### Decisions:

- [x] Select client app framework (angular.dart);
- [x] Select deployment mechanism (standard mobile, using cordova/phonegap)
- [ ] Select angular.dart - to cordova integration / UI methods
  - [x] ~~Rikolu?~~
  - [x] ~~Ionic w/ angular.dart changes (ours);~~
  - [x] ~~Ionic w/ app back-porting (angular.dart => angular.js)~~
  - [x] manual / other methods:
    - [ ] scripts to wrap dart2js output in relevant cordova CSS+JS;
    - [ ] integrate / test dart.angular.ui (use bs3, UI elements is/as needed);
    - [ ] if needed:  port any ionic UI elements (e.g. menubars), individually;

##### Process:

- [x] bringup methods / tutorials for angular.dart
- [x] bringup methods / tutorials for cordova (w/ ios & android emulation)
- [x] ~~bringup methods / tutorials for integrating Rikolu~~
- [x] ~~agile tracking (huboard.com w/ waffle.io image tags for now, plus github issues, PRs)~~
- [ ] bring tutorial app thru full cycle:
  - [x] dart-dev (browser)
  - [ ] cordova (2 mobiles)
    - [x] emulator
      - [x] iOS
      - [x] android (problem solved;)
        - [ ] include scanning for host/mac problem in makefiles (debug port hogging)
    - [ ] physical devices
      - [ ] iOS
        - [x] iPad mini
        - [ ] iPhone (5+)
        - [ ] iPad
      - [ ] android
        - [x] phone (android 4.4+)
        - [ ] phone (android 4.0+)
        - [ ] tablet (android 4.0+)
- [ ] establish test methods & coverage tracking;
- [ ] establish test & build tracking (jenkins / drone.io);
- [ ] establish deployment activity to android store;
- [ ] establish deployment activity to Apple store;
  - [x] developer's acct (approved);
  - [ ] test submission
- [ ] establish server / web access deployment;
- [x] documentation: wiki: markdown or restructuredText; docs: sphinxdoc.org
  - [ ] add documents directory here (move wiki into eventually);
  - [ ] see below: ~~add blog using ablog, much as blog.readthedocs.org is now doing;~~


##### Development:

- [ ] angular.dart tutorial, modify for single event `sens` instance
  - [x] browser
  - [x] mobile emulators
  - [x] mobile hardware / team review, initial reactions;
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

- [ ] when converting wiki / md documentation, create sphinx-doc (for readthedoc)
- [x] developer (ongoing / evolution);
- [ ] end user (test administrator);
- [ ] manager / site admin docs;
- [ ] devops / deployment instructions (for future / other projects);
- [ ] blog / article writup about forking, using this project for other targets & state of the art of single-development mobile apps;
  - [ ] use ablog, example as blog.readthedocs.org is now using;
