load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_binary(
    name = "service",
    srcs = ["service.py"],
    visibility = ["//:__subpackages__"],
    deps = [
        ":http",
        "@pip//aioquic",
        "@pip//falcon",
        "@pip//hypercorn",
    ],
)

py_library(
    name = "http",
    srcs = [
        "api/api_router/api.py",
        "api/endpoints/hello.py",
        "api/middleware/auth.py",
        "core/config.py",
        "core/logging.py",
        "service.py",
    ],
    visibility = ["//:__subpackages__"],
    deps = [
        "@pip//aioquic",
        "@pip//falcon",
        "@pip//hypercorn",
    ],
)
