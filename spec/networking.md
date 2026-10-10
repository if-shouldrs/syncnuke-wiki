---
layout: default
title: Networking
parent: Specification
nav_order: 5
permalink: /spec/networking/
---
# Networking

SyncNuke is defined at the Application Layer. Transport can be defined either by the synchronisation protocol or overriden by SyncNuke separate from the sync protocol itself.

All connections started by SyncNuke are routed through our master server `master.syncnuke.com:65344`. When you choose a synchronization protocol and connect, the master server looks at the protocols it supports, then redirects to an appropriate synchronization server.

## Reference behavior

Our internal `NetClient` abstraction supports connecting with a codec,
sending messages, registering receive listeners, and closing the connection. A codec isolates
message encoding and decoding.

Currently, TCP and QUIC are our supported transport protocols, with matching codec implementations.

## Reference material

SyncNuke Core's [NetClient (internal)](https://github.com/syncnuke/syncnuke-core/tree/main/src/main/java/io/github/syncnuke/client/internal/net/NetClient.java).

[Reference deployment notes](https://github.com/syncnuke/syncnuke-core/blob/main/README.md#basic-usage).
