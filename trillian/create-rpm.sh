#!/usr/bin/env bash
# Only run on Fedora
spectool -g ./trillian.spec
fedpkg -v -d --release f$(lsb_release -s -r) mockbuild
