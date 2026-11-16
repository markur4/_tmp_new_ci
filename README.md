# CI policy smoke test

This public repository contains a tiny arithmetic example and two small
GitHub Actions workflows. It has no PersoDB, AppRC, or Buildben application
source, dependencies, credentials, or release assets.

The CI workflow checks main pushes and pull requests, uses one Python version,
and cancels older work for the same ref or pull request. The tag workflow
exercises the RELEASE_REQUIRE_CI branch with dummy steps; it does not create a
GitHub Release or publish anything.

The repository exists only to confirm GitHub accepts and runs these workflow
patterns with ordinary dummy code.
