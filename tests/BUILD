load("@rules_python//python:defs.bzl", "py_test")

# gazelle:resolve py src.http.service //src.http

py_test(
    name = "service_test",
    srcs = ["service_test.py"],
    deps = [
        "//src/http",
        "@pip//falcon",
        "@pip//httpx",
    ],
)
