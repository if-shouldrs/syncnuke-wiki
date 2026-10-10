---
layout: default
title: Coordination
parent: Specification
nav_order: 6
permalink: /spec/coordination/
---
# Coordination

SyncNuke coordinates media playback through three common abstractions: `MediaPlayer`,
`SyncClient`, and `NetClient`. They connect a media player implementation, a synchronization
protocol implementation, and a transport implementation.

## Component responsibilities

| Abstraction | Implementation responsibility |
| --- | --- |
| [MediaPlayer]({{ '/spec/media-player/' | relative_url }}#reference-behavior) | Media player integrations implement playback controls and state observation. |
| [SyncClient]({{ '/spec/sync-client/' | relative_url }}) | Synchronization protocol implementations extend the client abstraction to coordinate playback within a session. |
| [NetClient]({{ '/spec/networking/' | relative_url }}#reference-behavior) | Transport implementations provide connection and message communication, using a codec for encoding and decoding. |

The synchronization implementation defines how exchanged information is interpreted and
used to coordinate playback. These abstractions let it work with media players and transports
through common controls, observations, and communication operations.

## Playback information flow

Local playback changes are observed through the media player abstraction and passed to the
synchronization implementation. That implementation decides what information to exchange,
using its codec and transport to communicate with the synchronization server.

Incoming messages are decoded and handled by the synchronization implementation. It uses
the player controls to apply playback changes, with subsequent observations reporting the
player's actual state.

## Coordination in SyncNuke Core

Coordinating these core components is the main responsibility of SyncNuke.

For managing media players, SyncNuke Core's `PlayerManager` uses polling to observe an arbitrary `MediaPlayer` implementation and detect
playback changes. It also translates a desired playback state into the player's controls,
providing a common way for synchronization implementations to work with different players.

See [Player management in Core]({{ '/spec/media-player/' | relative_url }}#player-management-in-core) for details.

For synchronizing playback state, SyncNuke Core's `SyncManager` coordinates the `PlayerManager` and manages `SyncClient` instances.
It passes the player manager to the selected sync client and forwards observed local state
changes to that client.

The two directions of playback information flow are:

```text
Local changes:
MediaPlayer → PlayerManager → SyncManager → SyncClient → NetClient

Incoming updates:
NetClient → SyncClient → PlayerManager → MediaPlayer
```

### Establishing a connection

When an application requests a connection through `SyncManager`, Core first uses the master
server protocol to find a synchronization server for the requested protocol.

1. `SyncManager` uses `MasterClient` to request a connection through the master server.
2. The master server returns `ConnectData`, containing the server's host and port along
   with the synchronization protocol and version.
3. `SyncManager` passes those details and the `PlayerManager` to `SyncClientFactory`.
4. The factory creates the matching `SyncClient` implementation, which connects to the
   synchronization server. `SyncManager` then asks it to log in to the session.

See [Networking]({{ '/spec/networking/' | relative_url }}) for the master server and transport details.

### Transport selection

Currently, the synchronization implementation defines its `NetClient` and codec.
Exposing transport selection to applications would require additional support in
`SyncClientFactory` and `SyncManager`.

### Lifecycle

`SyncManager` starts and stops the synchronization client while retaining the player manager.
Closing the manager stops the session and releases the player manager and its resources.

## Reference material

SyncNuke Core's [SyncManager](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/SyncManager.java),
[PlayerManager](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/player/internal/PlayerManager.java), and
[SyncClientFactory](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/SyncClientFactory.java).

[MasterClient](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/internal/protocol/master/MasterClient.java) and
[ConnectData](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/internal/protocol/master/data/ConnectData.java) define the reference master-server connection flow.
