# gazelle:resolve py src.fastapi.service.app //src/fastapi:fastapi

load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "service_test",
    srcs = ["service_test.py"],
    deps = [
        "//src/fastapi",
        "@pip//fastapi",
        "@pip//httpx",
    ],
)
