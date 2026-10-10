---
layout: default
title: Contributing
nav_order: 3
permalink: /contributing/
---
# Contributing

Contributions go to the repository responsible for the part of SyncNuke you want to improve.

## Where to contribute

| Contribution | Repository |
| --- | --- |
| Specification documentation & Site changes | [syncnuke-wiki](https://github.com/syncnuke/syncnuke-wiki) |
| Synchronization protocol support | [syncnuke-core](https://github.com/syncnuke/syncnuke-core) |
| Media application support (Desktop) | [syncnuke-desktop](https://github.com/if-shouldrs/syncnuke-desktop) |

SyncNuke Core provides the common library and synchronization abstractions. Desktop player
integrations belong in SyncNuke Desktop, which connects media programs to that library.

For other contributions, consult the [roadmap]({{ '/roadmap/' | relative_url }}).

## When starting

Please open a ticket in the relevant repository to discuss your proposed contribution before
starting a pull request, so the scope can be defined and we can avoid overlap in contributions.

Contributions that have not been approved in a ticket may take a long time to merge,
as additional validation and testing are needed before merging.

Every contribution to `syncnuke-core` should include an associated `syncnuke-wiki` pull
request documenting the change. Please link both pull requests and the discussion ticket so
the implementation and documentation can be reviewed together.

## Deployment & Testing

For deployment steps, please check the expected repository's README, as it walks you through local deployment steps along with other details relevant for contribution.
