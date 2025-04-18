load("@aspect_bazel_lib//lib:transitions.bzl", "platform_transition_filegroup")
load("@rules_oci//oci:defs.bzl", "oci_load")
load("//third_party/py_layer:py_layer.bzl", "py_oci_image")

platform(
    name = "aarch64_linux",
    constraint_values = [
        "@platforms//os:linux",
        "@platforms//cpu:aarch64",
    ],
)

platform(
    name = "x86_64_linux",
    constraint_values = [
        "@platforms//os:linux",
        "@platforms//cpu:x86_64",
    ],
)

##########################
# service binary         #
##########################

py_oci_image(
    name = "service_image",
    base = "@python",
    binary = "//src/http:service",
    entrypoint = ["/src/http/service"],
)

platform_transition_filegroup(
    name = "platform_image",
    srcs = [":service_image"],
    target_platform = select({
        "@platforms//cpu:arm64": ":aarch64_linux",
        "@platforms//cpu:x86_64": ":x86_64_linux",
    }),
)

# To build the image and load it into it into a local runtime:
# $ bazel run //mpm:service_image_load --platforms=//mpm:x86_64_linux
# $ docker run -p 8000:8000 -p 8443:8443 --rm service:latest --platform linux/x86_64_linux
oci_load(
    name = "service_image_load",
    image = ":platform_image",
    repo_tags = ["service:latest"],
)
