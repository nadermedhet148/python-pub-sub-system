# DefinitionDefinition

Pub/sub is shorthand for publish/subscribe messaging, an asynchronous communication method in which messages are exchanged between applications without knowing the identity of the sender or recipient.

## Overview
Four core concepts make up the pub/sub model:

- Topic – An intermediary channel that maintains a list of subscribers to relay messages to that are received from publishers
- Message – Serialized messages sent to a topic by a publisher which has no knowledge of the subscribers
- Publisher – The application that publishes a message to a topic
- Subscriber – An application that registers itself with the desired topic in order to receive the appropriate messages

### Advantages and disadvantages of pub/sub
As with all technology, using pub/sub messaging comes with advantages and disadvantages. The two primary advantages are loose coupling and scalability.

### Loose coupling
Publishers are never aware of the existence of subscribers so that both systems can operate independently of each other. This methodology removes service dependencies that are present in traditional coupling. For example, a client generally cannot send a message to a server if the server process is not running. With pub/sub, the client is no longer concerned whether or not processes are running on the server.

### Scalability
Pub/sub messaging can scale to volumes beyond the capability of a single traditional data center. This level of scalability is primarily due to parallel operations, message caching, tree-based routing, and multiple other features built into the pub/sub model.

Scalability does have a limit though. Increasing the number of nodes and messages also increases the chances of experiencing a load surge or slowdown. On top of that, the advantages of the pub/sub model can sometimes be overshadowed by the message delivery issues it experiences, such as:

A publisher may only deliver messages for a certain period of time regardless of whether the message was received or not.
Since the publisher does not have a window into the subscriber it will always assume that the appropriate subscriber is listening. If the subscriber isn’t listening and misses an important message it can be disastrous for production systems


## Components
The system consists in:
- register-service
- profile-service
- address-book-service
- Rabbitmq

# Demo

## Runinng

### create docker images : 
- `cd /register-service` -> `docker build . -t python-register-service`
- `cd /profile-service` -> `docker build . -t python-profile-service`
- `cd /address-book-service` -> `docker build . -t python-address-book-service`
- `docker-compose -f docker-compose.yml up -d`
