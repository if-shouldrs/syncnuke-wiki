---
layout: default
title: Sync client
parent: Specification
nav_order: 4
permalink: /spec/sync-client/
---
# Sync client

Synchronization protocol implementations extend `SyncClient` to connect playback
observations and controls with a synchronized session.

## Implementation responsibilities

Each implementation supplies these methods:

| Operation | Responsibility |
| --- | --- |
| `getNetClient()` | Return the transport client used for protocol communication. |
| `login(username, room, password)` | Implement the protocol's login and room-joining behavior. |
| `getRoomInfo()` | Return the room name and participant list as `RoomInfo`. |
| `onStatusChange(status)` | Handle observed local playback changes and decide what to send. |
| `handleResponse(data)` | Interpret incoming protocol messages and apply their effects. |
| `sendKeepAlive()` | Supply the protocol's periodic keep-alive communication. |

The constructor passes a `PlayerManager` and a keep-alive interval in milliseconds to the
base class. The implementation supplies its transport and codec, then calls
`connect(host, port, codec)` to establish communication.

### Working with playback state

The base class exposes its supplied `PlayerManager` for playback observations and controls.
The implementation decides how to filter local changes, represent them as messages, and
interpret incoming updates. Any expected state used to track what the server expects belongs to the
protocol implementation; the base class does not maintain it.

See [Player management in Core]({{ '/spec/media-player/' | relative_url }}#player-management-in-core)
for observation and control behavior, and [Coordination]({{ '/spec/coordination/' | relative_url }}#playback-information-flow)
for the flow between components.

### Room information

`RoomInfo` contains a room name and a list of users. The implementation maintains this
information as participants join and leave. The base class does not store membership
information or interpret room messages.

### Sending and receiving

Use the inherited `send(data)` method for outgoing messages so successful sends update the
base class's keep-alive tracking. Incoming decoded messages reach `handleResponse(data)`
through the listener registered by `connect()`.

Network responses, local state callbacks, and scheduled keep-alives can run on different
threads. Implementations need to coordinate access to their own shared state.

See [Establishing a connection]({{ '/spec/coordination/' | relative_url }}#establishing-a-connection)
for how Core selects and starts a synchronization implementation.

## Client management in Core

This section describes the behavior supplied by the base class for contributors working
on SyncNuke Core.

### Connection and message dispatch

`connect()` delegates connection setup to `getNetClient()` with the host, port, and codec,
then registers `handleResponse()` as a receive listener. The transport performs encoding
and decoding through that codec.

`send()` ignores null messages. For other messages, it delegates to the transport and records
the current time after the send returns successfully. A failed send does not update that
timestamp; the exception propagates to the caller.

### Keep-alive scheduling

A positive constructor interval schedules checks at that interval, with the first check
occurring after one interval. Zero or a negative interval disables scheduling.

At each check, the base class compares the current time with the last successful outgoing
send. Once the elapsed time reaches the interval, it calls `sendKeepAlive()`. Incoming
messages do not reset this timer. The callback defines the message to send; for example,
[DataSaver]({{ '/spec/data-saver/' | relative_url }}#state-updates) sends a projected playback state.

The base class catches and logs exceptions from the scheduled callback so later checks can
continue. `getCurrentTime()` obtains milliseconds from the supplied `TimingService`; the
constructor overload accepting that service allows timing to be controlled in tests.

### Releasing resources

`close()` cancels the keep-alive task and closes the transport, logging exceptions from
transport cleanup. An implementation with protocol-specific departure messages or resources
can override `close()` and call `super.close()` to retain the base cleanup.

Closing a sync client does not close its supplied player manager. See
[Lifecycle]({{ '/spec/coordination/' | relative_url }}#lifecycle) for how Core manages their lifetimes.

## Reference material

SyncNuke Core's [SyncClient](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/SyncClient.java) and
[RoomInfo](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/RoomInfo.java).

[DataSaverClient](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/internal/protocol/datasaver/DataSaverClient.java)
provides a concrete synchronization implementation.
