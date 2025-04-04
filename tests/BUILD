# gazelle:resolve py src.service //src

load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "service_test",
    srcs = ["service_test.py"],
    deps = [
        "//src",
        "@pip//falcon",
        "@pip//httpx",
    ],
)
