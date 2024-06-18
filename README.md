# python-bazel-docker-app

To run the flask app with Bazel:

```bash
bazel run //fibonacci:start_flask
```

To build the Docker image with Bazel:

```bash
bazel build //fibonacci:image
```

To run the Docker image locally:

```bash
bazel run //fibonacci:image <-- This doesn't at the moment.
docker run --rm bazel/fibonacci:image <-- This doesn't at the moment.
```
## Issues at the moment
When packaging the sh_binary target, not every external dependency is copied over to the final bundle which is `//fibonacci:app_bundle`.