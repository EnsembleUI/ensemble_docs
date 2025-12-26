# Server-Sent Events (SSE)

Server-Sent Events (SSE) is a web standard that allows a server to push real-time updates to a client over a single HTTP connection. Unlike WebSockets, SSE is **unidirectional (server → client)** and includes **automatic reconnection**.

For a complete working example demonstrating SSE functionality including connection management, event handling, error handling, and UI integration, see the [SSE Kitchen Sink example](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/rAmWKmUWonS4rWiHuhte) in Ensemble Studio.


## Key Features

* **Unidirectional**: Server pushes data to the client
* **Auto-reconnect**: Automatically reconnects on connection loss
* **HTTP-based**: Uses standard HTTP (`text/event-stream`)
* **Event-driven**: Supports event types, IDs, and payloads
* **Simple API**: Easy to configure and manage

## Common Use Cases

* Real-time notifications and alerts
* Live data feeds (stocks, sports scores)
* Progress updates for long-running tasks
* One-way chat or messaging
* Live dashboards and monitoring
* News feeds and social updates

## Define an SSE API

To use SSE in Ensemble, define an API with `type: sse` and provide the SSE endpoint along with optional connection settings.

```yaml
API:
  sseEvents:
    type: sse                    # Required
    url: https://sse.dev/test    # SSE endpoint
    sseOptions:
      autoReconnect: true        # Automatically reconnect
      reconnectDelay: 1000       # Delay (ms) before reconnect
      maxReconnectAttempts: 5    # Max retry attempts

    onResponse:                 # Fired for each SSE event
      executeCode:
        body: |
          // Process event data
          var eventData = response.body.data;

    onError:                    # Fired on connection error
      executeCode:
        body: |
          console.error('SSE error:', response);
```

## Configuration Options

| Option                            | Description                                    |
| --------------------------------- | ---------------------------------------------- |
| `type: sse`                       | **Required** – Enables SSE                     |
| `url`                             | SSE endpoint (`text/event-stream`)             |
| `sseOptions.autoReconnect`        | Auto-reconnect on disconnect (default: `true`) |
| `sseOptions.reconnectDelay`       | Delay between retries in ms (default: `1000`)  |
| `sseOptions.maxReconnectAttempts` | Max reconnect attempts (default: `5`)          |
| `onResponse`                      | Executed for each received event               |
| `onError`                         | Executed on SSE errors                         |

## Event Response Structure

Each event received in `onResponse` contains:

```js
response.body.event   // Event name (default: "message")
response.body.id      // Event ID (if provided)
response.body.data    // Event payload (text or JSON)
```

## Disconnect from SSE

Use the built-in action to disconnect from an SSE connection:

```yaml
disconnectSSE:
  apiName: sseEvents
```

```javascript
ensemble.disconnectSSE({apiName: "sseEvents"});
```

## Summary

Ensemble's SSE support provides:

* Simple real-time data streaming
* Automatic reconnection
* Built-in lifecycle management
* Easy UI integration
* Clean event handling

This makes SSE ideal for **live dashboards, notifications, and streaming updates** without the complexity of WebSockets.
