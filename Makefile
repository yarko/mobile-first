# Makefile for mobile-first
#

# You can set these variables from the command line.
JSOPTS        = --minimize
JSBUILD       = dart2js
BUILDDIR      = _build
CORDOVADIR    =

## User-friendly check for build tools and setup
# here, check:
# - dart2js and installation;
# - cordova
# - xcode for iOS builds
# - android sdk for android builds
# - blocking app(s) for android;

.PHONY: help clean dart-install

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  dart-install       to initially install release and dev dart editors"
	@echo "  cordova-install    to initially install cordova"
	@echo "  android-sdk        to initially install android-sdk"
	@echo "  check-installs     to check various systems settings, and potential blocking apps"


check-installs:
	@echo "(not yet) check-installs ..."
	@echo

clean:  # start app directory again;
	rm -rf $(BUILDDIR)/*
    # want to think about what to do w/ cordova dir also - really-clean?

android-sdk-install:
	@echo "(not yet) android-sdk-install ..."
	@echo

cordova-install:
	# link things up
	# setup activate / deactivate bash functions in .bash_login, or...

dart-install:
	# get both released and dev editions
	./scripts/dart-install

cordova-proj:
	@echo "(not yet) cordova-proj ..."
	@echo

ios-sim:
	@echo "(not yet) ios-sim ..."
	@echo

android-sim:
	@echo "(not yet) android-sim ..."
	@echo

ios:
	@echo "(not yet) ios ..."
	@echo

android:
	@echo "(not yet) android ..."
	@echo
