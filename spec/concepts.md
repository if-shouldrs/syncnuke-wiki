---
layout: default
title: Concepts
parent: Specification
nav_order: 1
permalink: /spec/concepts/
---
# Concepts

SyncNuke divides a synchronized playback system into three main responsibilities.

| Component | Responsibility |
| --- | --- |
| [Player integration]({{ '/spec/media-player/' | relative_url }}) | Observe playback state and expose player controls. |
| [Synchronization client]({{ '/spec/sync-client/' | relative_url }}) | Coordinate a session using a synchronization protocol. |
| [Networking layer]({{ '/spec/networking/' | relative_url }}) | Handle communication separately from player and synchronization logic. |

A protocol defines how synchronization information is exchanged. A transport carries that
information. Sharing a player abstraction does not imply that two wire protocols interoperate.

## Reference material

[Architecture overview](https://github.com/syncnuke/syncnuke-core/tree/main/README.md) and
[SyncManager](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/SyncManager.java).
