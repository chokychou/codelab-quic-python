# Add python dependencies to requirements.in
#
# Build the project:
# bazel run //:requirements.update && bazel run //:gazelle_python_manifest.update && bazel run //:gazelle
#
# Below are customized packages in addition to those loaded into bazel registry,

# # # # # # # # # #
# loads env files #
load("//third_party/rules_envfile:def.bzl", "envfile")

envfile(
    name = "envfile",
    files = [
        "//:.env",
    ],
)
