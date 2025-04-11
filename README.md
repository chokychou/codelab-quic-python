# About codelab
Implements a python quic server using falcon framework.

Exposed endpoint
`/hello/${echo}`

Start the server
` bazel run //src/http:service`

Client call:
`curl --http3 -k https://localhost:8443/hello/smart`

