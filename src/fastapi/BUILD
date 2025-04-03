load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_binary(
    name = "service",
    srcs = ["service.py"],
    visibility = ["//:__subpackages__"],
    deps = [
        ":fastapi",
        "@pip//aioquic",
        "@pip//fastapi",
        "@pip//hypercorn",
        "@pip//pydantic_core",
    ],
)

py_library(
    name = "fastapi",
    srcs = [
        "api/api_router/api.py",
        "api/endpoints/logs.py",
        "core/config.py",
        "core/security.py",
        "schemas/logs.py",
        "service.py",
    ],
    visibility = ["//:__subpackages__"],
    deps = [
        "@pip//aioquic",
        "@pip//fastapi",
        "@pip//hypercorn",
        "@pip//pydantic",
        "@pip//pydantic_core",
        "@pip//python_dotenv",
    ],
)
